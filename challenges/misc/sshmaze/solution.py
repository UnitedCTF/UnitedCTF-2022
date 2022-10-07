import ipaddress
import os
import random

from pwn import *

# Increase this value if the scripts exits early
TIMEOUT = 0.25


class Crawler:
  def __init__(self, ssh_args):
    self.ssh_args = ssh_args

    self.probes = {}

    self.flag = b""
    self.depth = []
    self.visited = set()

  def find_flag(self) -> str:
    # Keep trying until we find the flag
    while not self.flag:
      session = ssh(**self.ssh_args)

      try:
        # Create a shell
        self.channel = session.shell("/bin/sh", tty=False)

        # We can reset the visited state here, since unprobed nodes are priotized
        self.visited = set()

        # Mark the start node as visited
        hostname = self.__exec("hostname")
        self.depth = [hostname]

        self.visited.add(hostname)
        print(hostname)

        def dfs(probe):
          # grep the flag in the home directory
          self.flag = self.__exec(f"grep -iR 'FLAG-' .")
          if self.flag:
            raise Exception(self.flag)

          for neighbor in probe["neighbors"]:
            # For every neighbor, probe it and execute the DFS algorithm on it
            self.__enter(neighbor)
            neighbor_probe = self.__probe(neighbor)

            # Skip the neighbor if it has already been visited
            if neighbor_probe["hostname"] in self.visited:
              self.__leave()
              continue
            self.visited.add(neighbor_probe["hostname"])

            dfs(neighbor_probe)
            self.__leave()

        # Probe the start probe and find the neighbors
        probe = self.__probe(hostname)
        for neighbor in probe["neighbors"]:
          # For every neighbor, probe it and execute the DFS algorithm on it
          self.__enter(neighbor)
          neighbor_probe = self.__probe(neighbor)
          self.visited.add(neighbor)

          dfs(neighbor_probe)
          self.__leave()

      except Exception as e:
        if "FLAG-" in str(e):
          return str(e)

        if str(e) == "Failed to receive data..":
          print(
              "Timed out without finding flag, retrying from root..")
          print("You can try connecting back to it using")
          print(f"ssh -i {self.ssh_args['keyfile']} -p {self.ssh_args['port'] or 22} {self.ssh_args['user']}@{self.ssh_args['host']} 'ssh " +
                " ssh ".join(self.depth[1:]) + "'")
          continue

        raise e
      finally:
        self.channel.close()
        session.close()

  def __exec(self, command: str) -> str:
    self.channel.clean()
    marker = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=8))

    # print(">", command)
    self.channel.sendline(f"{command}; echo '{marker}';".encode())
    resp = self.channel.recvuntil(f"{marker}\n".encode(), timeout=30)
    # print("<", resp)

    if resp == b'':
      self.channel.close()
      raise Exception(f"Failed to receive data..")

    return resp[:-10].decode()

  def __sort_probe(self, probe):
    # Sort the networks and neighbors to priotize the ones never visited
    probe = {**probe}
    probe["neighbors"] = sorted(
        probe["neighbors"], key=lambda neighbor: neighbor in self.probes)
    return probe

  def __probe(self, hostname):
    if hostname in self.probes:
      return self.__sort_probe(self.probes[hostname])

    # Extract network info from ifconfig
    lines = self.__exec("ifconfig | grep 'addr:10.'").strip().split("\n")
    networks = []
    for line in lines:
      _, addr, bcast, mask = [line for line in line.strip().split(" ") if line]
      addr = addr.split(":")[1]
      bcast = bcast.split(":")[1]
      mask = mask.split(":")[1]

      cidr = ipaddress.IPv4Network(f"0.0.0.0/{mask}").prefixlen
      mask_range = 2 ** (32 - cidr)
      subnet = ipaddress.IPv4Address(bcast) - (mask_range - 1)

      networks.append({
          "addr": addr,
          "subnet": f"{subnet}/{cidr}",
          "bcast": bcast,
          "gateway": f"{subnet+1}",
          "hosts": [f"{subnet+i+2}" for i in range(mask_range - 3) if f"{subnet+i+2}" != addr],
      })

    # Ping the hosts for each network
    neighbors = []
    for network in networks:
      for ip in network["hosts"]:
        resp = self.__exec(
            f"dig +noall +answer +tries=1 +time=1 -x {ip}")
        if "IN\tPTR" not in resp:
          continue

        # Only need to find one since networks only contain two nodes
        # and we already have one
        neighbors.append(resp.split("sshmaze_")[1].split(".")[0])
        break

    self.probes[hostname] = {
        "hostname": hostname,
        "networks": networks,
        "neighbors": neighbors
    }

    return self.__sort_probe(self.probes[hostname])

  def __enter(self, host) -> None:
    print("." * len(self.depth) + host)
    self.channel.sendline(f"ssh -T {host} /bin/sh".encode())
    self.channel.clean(TIMEOUT)
    self.depth.append(host)

  def __leave(self) -> None:
    self.channel.sendline(b"exit")
    self.channel.clean(TIMEOUT)
    if len(self.depth) == 0:
      raise Exception("closed connection")

    self.depth.pop()


crawler = Crawler({
    "user": "cell",
    "host": "sshmaze.ctf.unitedctf.ca",
    "port": 2222,
    "keyfile": "./id_ed25519"
})

print(crawler.find_flag())
