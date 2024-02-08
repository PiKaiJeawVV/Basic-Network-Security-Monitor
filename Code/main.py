import os
import sys
import subprocess
import mysql.connector

alert_db = mysql.connector.connect(host="172.18.0.2",user="root",password="benz4466",database="alert_snort")
insert_db = alert_db.cursor()

def close_program():
    print("close")
    sys.exit(0)

def re_service():
    subprocess.run(f"systemctl restart snort.service",shell=True,stdout=subprocess.PIPE,encoding='utf-8')

def move_log(): ### <-- copy log from /var/log/snort/ to query
    copy_file = subprocess.run(f"mv /var/log/snort/alert.csv.list /home/snort-monitor/log/ > /dev/null 2>&1",shell=True,stdout=subprocess.PIPE,encoding='utf-8')
    if copy_file.returncode == 0:
        return copy_file.returncode
    else:
        return copy_file.returncode

def remove_syntax(msg):
    word = msg.replace("'", "").replace("[","").replace("]","")
    return word

def insert_alertdb(msg):
    insert_db.execute(f"insert into alert (_alert_msg,_time) values ('{msg}',now());")

def convert_list(li):
    result = li.split()
    del result[0]
    return result

def del_duplicate(li):
    newlist = []
    for one in li:
        if one not in newlist:
            newlist.append(one)
    return newlist

def read_file():
    cat_file = subprocess.run(f"cat /home/snort-monitor/log/alert.csv.list",shell=True,stdout=subprocess.PIPE,encoding='utf-8')
    output_data = cat_file.stdout
    line = output_data.splitlines()
    newlist = []
    for li_1 in line:
        remove_index0 = convert_list(li_1)
        newlist.append(remove_index0)
        result = del_duplicate(newlist)
    return result

def main():
    check_file = os.path.getsize("/home/snort-monitor/log/alert.csv.list")
    if check_file != 0:
        code_of_func = move_log()
        if code_of_func != 0:
            for un_process in read_file():
                process = str(un_process)
                result = remove_syntax(process)
                insert_alertdb(result)
                alert_db.commit()
            re_service()
    else:
        close_program()

        
        

if __name__ == '__main__':
    main()
    alert_db.close()