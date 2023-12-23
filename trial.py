import subprocess
import re

HOST =  subprocess.check_output('cat /etc/xray/domain', shell=True).decode("utf-8")

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
        msg = f"""
**━━━━━━━━━━━━━━━━━**
**🇮🇩🇮🇩 Xray/Trojan Account 🇮🇩🇮🇩**
**━━━━━━━━━━━━━━━━━**
**» Remarks     :** `{remarks}`
**» Host Server :** `{domain}`
**» Host XrayDNS:** `{HOST}`
**» User Quota  :** `Unlimited`
**» Port DNS    :** `443, 53`
**» port TLS    :** `222-1000`
**» Path Trojan :** `(/multi path)/trojan-ws`
**» User ID     :** `{uuid}`
**━━━━━━━━━━━━━━━━**
**» Link WS    :** 
`{b[0].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**» Link GRPC  :** 
`{b[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**» Expired Until:** `{exp} Minutes`
**» 🌀@LunaticTunnel**
"""


        return {
  "meta": {
    "code": 200,
    "status": "success",
    "ip_address": domain,
    "message": "Create TROJAN-WS Success"
  },                                                                            "data": {
    "hostname": domain,
    "ISP": "Akamai Connected Cloud",                                              "CITY": "Jakarta",
    "username": remarks,
    "expired": "2 Hour",
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
    print(trial_tr())

