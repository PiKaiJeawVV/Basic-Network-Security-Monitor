#!/bin/bash

### Update && Install Snort
apt update
apt install snort -y

### make Dir
mkdir -p /home/snort-monitor/log/

