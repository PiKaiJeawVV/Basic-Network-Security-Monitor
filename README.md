# Basic-Network-Security-Monitor
### _Install Docker & Docker Compose_
#####    1. Install Docker-compose
- https://docs.docker.com/compose/install/standalone/

#####    2. install Docker
```sh
    sudo apt update
    sudo apt install docker -y
```
#####    3.Run Docker-file (Please Edit Password Database in docker-compose.yml)
```sh
    cd docker-file
    docker-compose up -d
```
### _Run file install.sh_
```sh
    chmod +x  install.sh
    ./install.sh
```
### _Install Lib Python_
```
    pip install -r requirements.txt
```
### _Config snort.conf_
```sh
    nano /etc/snort/snort.conf
    output alert_csv: alert.csv.list timestamp,msg,src,srcport,dst,dstport    <-- ### Put in step 6 ###
```