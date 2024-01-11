import subprocess

def cp_log(): ### <-- copy log from /var/log/snort/ to query
    copy_file = subprocess.run(f"cp /var/log/snort/snort.alert.fast /home/snort-monitor/log/",shell=True,stdout=subprocess.PIPE,encoding='utf-8')

def check_date():  
    cat_file = subprocess.run(f"cat /home/snort-monitor/log/snort.alert.fast | awk '!/SCAN/'",shell=True,stdout=subprocess.PIPE,encoding='utf-8')  #<-- Can Modify type !=
    unwanted_text = {'[**]',}
    output_data = cat_file.stdout
    line = output_data.splitlines()
    for i in line:
        ooo = i.split()
        delete_item = [ele for ele in ooo if ele not in unwanted_text]
        delete_item.pop(1)
        print(delete_item)


if __name__ == '__main__':
    cp_log()  # <-- Copy file and replace
    check_date() # <-- Output Data and split text for module "Notification"
