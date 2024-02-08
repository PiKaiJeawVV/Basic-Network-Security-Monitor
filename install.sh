#!/bin/bash

### Update && Install Snort
echo "Install Snort"
apt update
apt install snort -y
echo "Install Done !"

### Make Dir
mkdir -p /home/snort-monitor/log/
mkdir -p /home/snort-monitor/code/
echo "Make folder Done !"

### Move Python file
cp code/main.py /home/snort-monitor/code/

### Modify Crontab
echo */2 * * * *    /usr/bin/python3 /home/snort-monitor/code/main.py >> /etc/crontab