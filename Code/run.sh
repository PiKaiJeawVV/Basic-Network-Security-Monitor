#!/bin/bash

### Update && Install Snort
apt update
apt install snort -y

### Make Dir
mkdir -p /home/snort-monitor/log/

### Add crontab every 2 minute
echo */2 * * * *    /usr/bin/python3 /home/snort-monitor/code/query_snort.py >> /etc/crontab       ## <-- Please Modify you path file "/yourpath/query_snort.py"
