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
    cmd = 'printf "%s\\n" "{}" "{}" | renewssh-api.sh'.format(u, hari)
    text = subprocess.check_output(cmd, shell=True).decode("utf-8")
    username_pattern = re.compile(r'Username\s*:\s*(\w+)')
    expires_on_pattern = re.compile(r'Expires on\s*:\s*(\d{2}\s\w+\s\d{4})')

    # Mencari kecocokan dalam teks
    username_match = username_pattern.search(text)
    expires_on_match = expires_on_pattern.search(text)

    username = username_match.group(1)
    expires_on = expires_on_match.group(1)

    return {"username": username,
            "exp": expires_on
            }

def vmess(u,hari):
    cmd = 'printf "%s\\n" "{}" "{}" "2" "1000" | renewws-api.sh'.format(u, hari)
    text = subprocess.check_output(cmd, shell=True).decode("utf-8")
    client_name_pattern = re.compile(r'Client Name\s*:\s*(\w+)')
    exp_date_pattern = re.compile(r'Expired On\s*:\s*(\d{4}-\d{2}-\d{2})')

    # Mencari kecocokan dalam teks
    client_name_match = client_name_pattern.search(text)
    exp_date_match = exp_date_pattern.search(text)
    client_name = client_name_match.group(1)
    exp_date = exp_date_match.group(1)
    # print(client_name)
    # print(exp_date)
    return {"username": client_name,
            "exp": exp_date
            }

def vless(u,hari):
    cmd = 'printf "%s\\n" "{}" "{}" "2" "1000" | renewvless'.format(u, hari)

    text = subprocess.check_output(cmd, shell=True).decode("utf-8")
    client_name_pattern = re.compile(r'Client Name\s*:\s*(\w+)')
    exp_date_pattern = re.compile(r'Expired On\s*:\s*(\d{4}-\d{2}-\d{2})')

    # Mencari kecocokan dalam teks
    client_name_match = client_name_pattern.search(text)
    exp_date_match = exp_date_pattern.search(text)
    client_name = client_name_match.group(1)
    exp_date = exp_date_match.group(1)
    print(client_name)
    print(exp_date)
    return {"username": client_name,
            "exp": exp_date
            }




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
    print(client_name)
    print(exp_date)
    return {"username": client_name,
            "exp": exp_date
            }


if __name__ == '__main__':
    print(ssh('wgn','1'))