import subprocess
import re,json

HOST =  subprocess.check_output('cat /etc/xray/domain', shell=True).decode("utf-8")
kota =  subprocess.check_output('curl -s ipinfo.io/city', shell=True).decode("utf-8")
ISP =  subprocess.check_output('curl -s ipinfo.io/org | cut -d " " -f 2-10', shell=True).decode("utf-8")




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
    print(trial_vm())

