import subprocess
import re,json,random,base64

HOST =  subprocess.check_output('cat /etc/xray/domain', shell=True).decode("utf-8")
kota =  subprocess.check_output('cat /etc/xray/city', shell=True).decode("utf-8")
ISP =  subprocess.check_output('cat /etc/xray/isp', shell=True).decode("utf-8")
DOMAIN = HOST



from datetime import datetime, timedelta
import pytz


def trojan(u,hari):
    cmd = f'printf "%s\n" "{u}" "{hari}" "2" "1000" | renewtr'
    x = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return x


if __name__ == "__main__":
    print(trojan("",""))
