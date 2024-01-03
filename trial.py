import subprocess
import re,json,random,base64

HOST =  subprocess.check_output('cat /etc/xray/domain', shell=True).decode("utf-8")
kota =  subprocess.check_output('cat /etc/xray/city', shell=True).decode("utf-8")
ISP =  subprocess.check_output('cat /etc/xray/isp', shell=True).decode("utf-8")
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
        data =  {
          "meta": {
            "code": 200,
            "status": "success",
            "ip_address": "172.105.123.98",
            "message": "Create SSH Success"
          },
          "data": {
            "hostname": HOST,
            "ISP": ISP,
            "CITY": kota,
            "username": user.strip(),
            "servername": "",
            "pubkey": "",
            "password": pw.strip(),
            "exp": exp,
            "port": {
              "tls": 443,
              "none": 80,
              "drop1": 90,
              "drop2": 69,
              "ssh1": 444,
              "ovpntcp": 1194,
              "ovpnudp": 25000,
              "slowdns": 53,
              "slowdns1": 5300,
              "sshohp": 9080,
              "sshudp": "1-65535",
              "ovpnohp": 9088,
              "squid": 3128,
              "udpcustom": "1-65535"
            },
            "payloadws": {
              "payloadcdn": "GET / HTTP/1.1[crlf]Host: [host_port][crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]",
              "payloadwithpath": "GET /worryfree/ssh HTTP/1.1[crlf]Host: BUG[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]"
            }
          }
        }

        return data


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
    print(trial_ssh())

