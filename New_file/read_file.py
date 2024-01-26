import subprocess

cat_file = subprocess.run(f"cat /var/log/snort/alert.csv.short",shell=True,stdout=subprocess.PIPE,encoding='utf-8')
output_data = cat_file.stdout
line = output_data.splitlines()
for i in line:
    ooo = i.split()
    print(ooo)