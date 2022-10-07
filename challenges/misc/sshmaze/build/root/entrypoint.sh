#!/bin/sh

# Give ownership of the cell user to root
chown -R root:root /home/cell

# Flush the ARP table every minute, making the challenge a bit harder >:)
while :; do 
  ip neigh flush all
  sleep 60
done &

# Start the ssh server
exec /usr/sbin/sshd -D \
  -o GatewayPorts=yes \
  -o AllowTcpForwarding=yes \
  -o AuthorizedKeysFile=.ssh/authorized_keys \
  -o KbdInteractiveAuthentication=no \
  -o PasswordAuthentication=no \
  -o AllowUsers=cell \
  "$@"
