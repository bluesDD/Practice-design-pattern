#!/bin/bash

ssh -i ec2.pem ec2-user@ec2.com <<EOC >lot.log
hostname
cat /etc/passwd
EOC
