import subprocess
import mysql.connector

alert_db = mysql.connector.connect(host="172.18.0.2",user="root",password="benz4466",database="alert_snort")
insert_db = alert_db.cursor()

time_list = []
alert_list = []
option_list = []
scr_dst_list = []

def del_duplicate(li):
    newlist = []
    for one in li:
        if one not in newlist:
            newlist.append(one)
    return newlist

def read_file():
    cat_file = subprocess.run(f"cat /var/log/snort/alert.csv.list",shell=True,stdout=subprocess.PIPE,encoding='utf-8')
    output_data = cat_file.stdout
    line = output_data.splitlines()
    return line

def gen_message():
    for un_process in read_file():
        process = un_process.split()
        result0 = process[0]
        result1 = process[1]
        result2 = process[2]
        result3 = process[3]
        time_list.append(result0)
        alert_list.append(result1)
        option_list.append(result2)
        scr_dst_list.append(result3)
    return time_list,alert_list,option_list,scr_dst_list


def insert_alertdb():
    insert_db.excute(f"insert into alert (alert,option,scr_des,time) values (now())")
    0

def main():
    message = gen_message()
    #time = message[0], alert = message[1] ,alert2 = message[2], src_dst = message[3]
    time,alert,alert2,src_dst = message[0],message[1],message[2],message[3]
    print(del_duplicate(alert))
    #for z,x,c,v in zip (time,alert,alert2,src_dst):
    #    print(z,x,c,v)


if __name__ == '__main__':
    main()
    alert_db.close()