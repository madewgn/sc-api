import subprocess
import re,json,random,base64

# HOST =  subprocess.check_output('cat /etc/xray/domain', shell=True).decode("utf-8")
# kota =  subprocess.check_output('cat /etc/xray/city', shell=True).decode("utf-8")
# ISP =  subprocess.check_output('cat /etc/xray/isp', shell=True).decode("utf-8")
# DOMAIN = HOST
#

#
# from datetime import datetime, timedelta
# import pytz

def ssh(u,hari):
    cmd = 'printf "%s\\n" "{}" "{}" | renewssh'.format(u, hari)
    x = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return x

def vmess(u,hari):
    cmd = 'printf "%s\\n" "{}" "{}" "2" "1000" | renewws'.format(u, hari)

    x = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return x

def vless(u,hari):
    cmd = 'printf "%s\\n" "{}" "{}" "2" "1000" | renewvless'.format(u, hari)

    x = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return x




def trojan(u,hari):
    cmd = 'printf "%s\\n" "{}" "{}" "2" "1000" | renewtr-api.sh'.format(u, hari)
    text = subprocess.check_output(cmd, shell=True).decode("utf-8")
    client_name_pattern = re.compile(r'Client Name\s*:\s*(\w+)')
    exp_date_pattern = re.compile(r'Expired On\s*:\s*(\d{4}-\d{2}-\d{2})')

    # Mencari kecocokan dalam teks
    client_name_match = client_name_pattern.search(text)
    exp_date_match = exp_date_pattern.search(text)
    client_name = client_name_match.group(1)
    exp_date = exp_date_match.group(1)
    return {"username": client_name,
            "exp": exp_date
            }

