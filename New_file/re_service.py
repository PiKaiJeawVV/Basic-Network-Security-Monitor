import subprocess

re_service = subprocess.run(f"systemctl restart snort.service",shell=True,stdout=subprocess.PIPE,encoding='utf-8')
print(re_service.returncode)