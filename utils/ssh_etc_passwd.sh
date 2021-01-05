#!/bin/bash

hosts="host-a host-b"

for host in ${hosts}; do
ssh  ec2-user@$host <<EOC >>lot.log
hostname
cat /etc/passwd
EOC
done
