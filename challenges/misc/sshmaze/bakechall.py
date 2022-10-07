#!/usr/bin/env python3

from subprocess import check_output
import os
import sys
import yaml
import ipaddress
import random
import hashlib
import hmac

from lib.maze import Maze
from lib.solver import Solver


# Set to True to randomize ips assigned to the hosts
RANDOMIZE_NODE_IPS = False

# Change the port expose to the internet
PORT = 2222


def shell_exec(cmd: str):
  check_output(cmd, shell=True)


def obfuscator(data: str):
  hm = hmac.new(" ".join(sys.argv[1:]).encode(),
                data.encode(), hashlib.sha1)
  return hm.hexdigest()[:16]


def ipgen(count: int, cidr: int, base_ip="10.0.0.0"):
  base_ip = ipaddress.IPv4Address(base_ip)
  mask_range = 2 ** (32 - cidr)
  count_skip = count * mask_range

  ip = base_ip + count_skip
  return {
      "subnet": f"{ip}/{cidr}",
      "gateway": f"{ip+1}",
      "hosts": [f"{ip+i+2}" for i in range(mask_range - 3)]
  }


# size_x size_y start_x start_y end_x end_y seed
maze = Maze(*[int(arg) for arg in sys.argv[1:]])

base_service = {
    "image": "sshmaze",
    "restart": "on-failure",
    # To flush the ARP table
    "cap_add": ["NET_ADMIN"],
    "stop_grace_period": "1s",
    "environment": ["${TZ:-UTC}"]
}

docker_compose = {
    "version": "3.9",
    "services": {},
    "networks": {
        "external": {
            "name": "external"
        }
    }
}

# Generate a network range for every open path
network_ranges = []
for x in range(maze.nx):
  for y in range(maze.ny):
    cell = maze.cell_at(x, y)
    if not cell.walls["E"]:
      network_ranges.append(ipgen(len(network_ranges), 29))
    if not cell.walls["S"]:
      network_ranges.append(ipgen(len(network_ranges), 29))

# Generate home and service for each node
for x in range(maze.nx):
  for y in range(maze.ny):
    ns_cell = obfuscator(f"{x}-{y}")
    if not os.path.exists(f"./home/{ns_cell}"):
      shell_exec(f"""
        mkdir -p "./home/{ns_cell}/.ssh";
        ln -s /dev/null "./home/{ns_cell}/.ash_history";
        yes no | ssh-keygen -q -C "" -N "" -t ed25519 -f "./home/{ns_cell}/.ssh/id_ed25519" || true;
        chmod 644 "./home/{ns_cell}/.ssh/id_ed25519";
      """)

    docker_compose["services"][ns_cell] = {
        **base_service,
        "container_name": f"sshmaze_{ns_cell}",
        "hostname": ns_cell,
        "networks": {},
        "volumes": [
            f"./home/{ns_cell}:/home/cell"
        ]
    }

# Assign IPs and SSH keys to node pairs
ips = {}
directions = {"N": "UP", "E": "RIGHT", "S": "DOWN", "W": "LEFT"}
for x in range(maze.nx):
  for y in range(maze.ny):
    cell = maze.cell_at(x, y)
    ns_cell = obfuscator(f"{x}-{y}")

    for d, neigh in maze.cell_open_neighbors(x, y):
      ns_neigh = obfuscator(f"{neigh.x}-{neigh.y}")

      network_pair_name = None
      for service_name, service in docker_compose["services"].items():
        for network_name, network in service["networks"].items():
          if ns_cell in network_name and ns_neigh in network_name:
            network_pair_name = network_name
            break
        if network_pair_name:
          break

      if not network_pair_name:
        network_pair_name = f"{ns_cell}-{ns_neigh}"
        ips[network_pair_name] = network_ranges.pop(
            random.randint(0, len(network_ranges) - 1)
        )
        docker_compose["networks"][network_pair_name] = {
            "name": network_pair_name,
            "internal": True,
            "ipam": {
                "config": [{
                    "subnet": ips[network_pair_name]["subnet"],
                    "gateway": ips[network_pair_name]["gateway"]
                }]
            }
        }

      if RANDOMIZE_NODE_IPS:
        if network_pair_name not in docker_compose["services"][ns_cell]["networks"]:
          docker_compose["services"][ns_cell]["networks"][network_pair_name] = {
              "ipv4_address": ips[network_pair_name]["hosts"].pop(
                  random.randint(0, len(ips[network_pair_name]["hosts"]) - 1)
              )
          }
        if network_pair_name not in docker_compose["services"][ns_neigh]["networks"]:
          docker_compose["services"][ns_neigh]["networks"][network_pair_name] = {
              "ipv4_address": ips[network_pair_name]["hosts"].pop(
                  random.randint(0, len(ips[network_pair_name]["hosts"]) - 1)
              )
          }
      else:
        docker_compose["services"][ns_cell]["networks"][network_pair_name] = {}
        docker_compose["services"][ns_neigh]["networks"][network_pair_name] = {}

      direction = directions[d]
      with open(f"./home/{ns_neigh}/.ssh/authorized_keys", "a") as ak:
        with open(f"./home/{ns_cell}/.ssh/id_ed25519.pub", "r") as pub:
          ak.write(pub.read())

# Expose the start node to the internet
ns_start = obfuscator(f"{maze.sx}-{maze.sy}")
docker_compose["services"][ns_start]["ports"] = [f"{PORT}:22"]
docker_compose["services"][ns_start]["networks"]["external"] = {}

# Create a SSH key for the internet to go into the start node
shell_exec("yes no | ssh-keygen -q -C "" -N "" -t ed25519 -f 'id_ed25519' || true;")
with open(f"./home/{ns_start}/.ssh/authorized_keys", "a") as ak:
  with open(f"./id_ed25519.pub", "r") as pub:
    ak.write(pub.read())

# Add the flag to the end node
ns_end = obfuscator(f"{maze.ex}-{maze.ey}")
with open(f"./home/{ns_end}/flag.txt", "w") as flag_remote:
  with open(f"./flag.txt", "r") as flag_local:
    flag_remote.write(flag_local.read())

# Dump the docker-compose configuration
with open("docker-compose.yml", "w+") as f:
  f.write(yaml.dump(docker_compose))

solver = Solver(maze)
path = solver.aStar()
for x, y in path:
  maze.cell_at(x, y).marker = "#"

print(maze)
print(f"Maze solvable in {len(path)+1} steps")
print(f"S:{ns_start} E:{ns_end}")
print()
print("SSH using the following private key with the command 'ssh -iid_ed25519 -p13722 cell@PUBLIC_IP'")
with open(f"./id_ed25519", "r") as f:
  print(f.read())
