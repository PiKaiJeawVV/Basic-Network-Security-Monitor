#!/bin/bash

mkdir -p /home/test/log/
mkdir -p /home/test/code/

cp main.py /home/test/code/

echo */2 * * * *    /usr/bin/python3 /home/snort-monitor/code/query_snort.py >> /etc/crontab 