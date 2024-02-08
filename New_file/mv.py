import subprocess
import sys

def close_program():
    #print("Exit Program")
    sys.exit(0)

def re_service():
    service_snort = subprocess.run(f"systemctl restart snort.service",shell=True,stdout=subprocess.PIPE,encoding='utf-8')
 
def move_log(): ### <-- copy log from /var/log/snort/ to query
    copy_file = subprocess.run(f"mv /var/log/snort/alert.csv.list /home/snort-monitor/log/ > /dev/null 2>&1",shell=True,stdout=subprocess.PIPE,encoding='utf-8')
    if copy_file.returncode == 0:
        return copy_file.returncode
    else:
        return copy_file.returncode

if __name__ == '__main__':
    print(move_log())
    print("i")
    print("i")
    print("i")
    print("i")
    print("i")
    close_program()
    print("x")
    print("x")
    print("x")
    print("x")
    print("x")
