import subprocess
import sys

def close_program():
    print("Exit Program")
    sys.exit(0)

def move_log(): ### <-- copy log from /var/log/snort/ to query
    copy_file = subprocess.run(f"mv /var/log/snort/alert.csv.list /home/snort-monitor/log/ > /dev/null 2>&1",shell=True,stdout=subprocess.PIPE,encoding='utf-8')
    if copy_file.returncode == 0:
        print("OK")
    else:
        print("Not OK")
        close_program()  


if __name__ == '__main__':
   move_log()
