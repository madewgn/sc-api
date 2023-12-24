import subprocess
import re,json,random,base64

HOST =  subprocess.check_output('cat /etc/xray/domain', shell=True).decode("utf-8")
kota =  subprocess.check_output('curl -s ipinfo.io/city', shell=True).decode("utf-8")
ISP =  subprocess.check_output('curl -s ipinfo.io/org | cut -d " " -f 2-10', shell=True).decode("utf-8")
DOMAIN = HOST
exp = 60




def trial_ssh():
    user = "trialX"+str(random.randint(100,1000))
    pw = "1"

    cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user} | tmux new-session -d -s {user} "trial trialssh {user} {exp}"'
    try:
        subprocess.check_output(cmd,shell=True)
    except:
        print("**User Already Exist**")
    else:
        #today = DT.date.today()
        #later = today + DT.timedelta(days=int(exp))
        msg = f"""
**━━━━━━━━━━━━━━━━━**
**🇮🇩🇮🇩 SSH OVPN ACCOUNT 🇮🇩🇮🇩**
**━━━━━━━━━━━━━━━━━**
**» Username         :** `{user.strip()}`
**» Password         :** `{pw.strip()}`
**━━━━━━━━━━━━━━━━━**
**» Host             :** `{HOST}`
**» Port OpenSSH     :** `443, 80, 22`
**» Port DNS         :** `443, 53 ,22`
**» Port Dropbear    :** `443, 109`
**» Port Dropbear WS :** `443, 109`
**» Port SSH WS      :** `80, 8080, 8081-9999 `
**» Port SSH SSL WS  :** `443`
**» Port SSL/TLS     :** `222-1000`
**» Port OVPN WS SSL :** `443`
**» Port OVPN SSL    :** `443`
**» Port OVPN TCP    :** `443, 1194`
**» Port OVPN UDP    :** `2200`
**» Proxy Squid      :** `3128`
**» BadVPN UDP       :** `7100, 7300, 7300`
**━━━━━━━━━━━━━━━━━**
**» Payload WSS      :** `GET wss://BUG.COM/ HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf][crlf]`
**━━━━━━━━━━━━━━━━━**
**» OpenVPN WS SSL   :** `https://{DOMAIN}:81/ws-ssl.ovpn`
**» OpenVPN SSL      :** `https://{DOMAIN}:81/ssl.ovpn`
**» OpenVPN TCP      :** `https://{DOMAIN}:81/tcp.ovpn`
**» OpenVPN UDP      :** `https://{DOMAIN}:81/udp.ovpn`
**━━━━━━━━━━━━━━━━━**
**» Save Link Account:** `https://{DOMAIN}:81/ssh-{user.strip()}.txt`
**» Expired Until:** `{exp} Minutes`

"""
        return msg


def trial_vl():
    cmd = f'printf "%s\n" "{exp}" | trialvless-api'
    try:
        a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
        print("**User Already Exist**")
    else:
        #today = DT.date.today()
        #later = today + DT.timedelta(days=int(exp))
        x = [x.group() for x in re.finditer("vless://(.*)",a)]
        print(x)
        remarks = re.search("#(.*)",x[0]).group(1)
        # domain = re.search("@(.*?):",x[0]).group(1)
        uuid = re.search("vless://(.*?)@",x[0]).group(1)
        # path = re.search("path=(.*)&",x[0]).group(1)
        msg = f"""
**━━━━━━━━━━━━━━━━━**
**⭐ XRAY / VLESS ⭐**
**━━━━━━━━━━━━━━━━━**
**» Remarks     :** `{remarks}`
**» Host Server :** `{HOST}`
**» Host XrayDNS:** `{HOST}`
**» User Quota  :** `Unlimited`
**» Port DNS    :** `443, 53`
**» port TLS    :** `222-1000`
**» Port NTLS   :** `80, 8080, 8081-9999`
**» NetWork     :** `(WS) or (gRPC)`
**» User ID     :** `{uuid}`
**» Path Vless  :** `(/multi path)/vless `
**» Path Dynamic:** `http://BUG.COM/vless `
**━━━━━━━━━━━━━━━━━**
**» Link TLS   : **
`{x[0]}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link GRPC  :**
`{x[2].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Expired Until :** `{exp} Minutes`
"""
        return msg



def trial_vm():
    exp = 60
    cmd = f'printf "%s\n" "{exp}" | trialws-api'
    try:
        a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
        print("**User Already Exist**")
    else:
        #        today = DT.date.today()
        #        later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("vmess://(.*)",a)]
        print(b)
        z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
        z = json.loads(z)
        z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
        z1 = json.loads(z1)
        msg = f"""
**━━━━━━━━━━━━━━━━━**
**⭐ XRAY / VMESS ⭐**
**━━━━━━━━━━━━━━━━━**
**» Remarks      :** `{z["ps"]}`
**» Domain       :** `{z["add"]}`
**» XRAY DNS     :** `{HOST}`
**» User Quota   :** `Unlimited`
**» Port DNS     :** `443, 53`
**» port TLS     :** `222-1000`
**» Port NTLS    :** `80, 8080, 8081-9999`
**» Port GRPC    :** `443`
**» User ID      :** `{z["id"]}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `(/multi path)/vmess`
**» Path NLS     :** `(/multi path)/vmess`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `vmess-grpc`
**━━━━━━━━━━━━━━━━━**
**» Link TLS     :** 
`{b[0].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS    :** 
`{b[1].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link GRPC    :** 
`{b[2].strip("'")}`
**━━━━━━━━━━━━━━━━━**
**» Format OpenClash :** https://{HOST}:81/vmess-{z["ps"]}.txt
**━━━━━━━━━━━━━━━━━**
**» Expired Until:** `{exp} Minutes`
"""
        return msg

def trial_tr():
    exp = 60
    cmd = f'printf "%s\n" "{exp}" | trialtr-api'
    try:
        a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
        print("**User Already Exist**")
    else:
        #today = DT.date.today()
        #later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("trojan://(.*)",a)]
        print(b)
        remarks = re.search("#(.*)",b[0]).group(1)
        domain = re.search("@(.*?):",b[0]).group(1)
        uuid = re.search("trojan://(.*?)@",b[0]).group(1)

        return {
  "meta": {
    "code": 200,
    "status": "success",
    "ip_address": domain,
    "message": "Create TROJAN-WS Success"

  },
    "data": {
    "hostname": domain,
    "ISP": ISP,                                              
    "CITY": kota,
    "username": remarks,
    "expired": exp,
    "uuid": uuid,
    "port": {
      "tls": "443"
    },
    "path": {
      "stn": "/trojan",
      "multi": "/yourbug/trojan"
    },
    "link": {
      "tls": b[0].replace(" ",""),
      "grpc": b[1].replace(" ","")
      
    }
  }
}


if __name__ == "__main__":
    print(trial_vl())

