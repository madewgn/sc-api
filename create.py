import subprocess
import re,json,random,base64

HOST =  subprocess.check_output('cat /etc/xray/domain', shell=True).decode("utf-8")
kota =  subprocess.check_output('cat /etc/xray/city', shell=True).decode("utf-8")
ISP =  subprocess.check_output('cat /etc/xray/isp', shell=True).decode("utf-8")
DOMAIN = HOST
exp = 60


def vmess(user,exp):
    cmd = f'printf "%s\n" "{user}" "{exp}" | addws-api'
    try:
        a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
        print("**User Already Exist**")
    else:
        #        today = DT.date.today()
        #        later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("vmess://(.*)",a)]
#           c = [x.group() for x in re.finditer("Host XrayDNS(.*)",a)]
#           d = [x.group() for x in re.finditer("Pub Key(.*)",a)]
        print(b)
#           print(d)
#           print(c)
#           xx = re.search("Pub Key      :(.*)",d[0]).group(1)
#           xxx = re.search("Host XrayDNS :(.*)",d[0]).group(1)
        z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
        z = json.loads(z)
        z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
        z1 = json.loads(z1)

        return cmd


def trojan(user,exp):
    cmd = f'printf "%s\n" "{user}" "{exp}" | addtr-api'
    try:
        a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
        print("**User Already Exist**")
    else:
        # today = DT.date.today()
        # later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("trojan://(.*)",a)]
        #        print(b)
        domain = re.search("@(.*?):",b[0]).group(1)
        uuid = re.search("trojan://(.*?)@",b[0]).group(1)
        remarks = re.search("#(.*)",b[0]).group(1)
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


def vless(user,exp):
    cmd = f'printf "%s\n" "{user}" "{exp}" | addvless-api'
    try:
        a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
        print("**User Already Exist**")
    else:
        x = [x.group() for x in re.finditer("vless://(.*)",a)]
        print(x)
        remarks = re.search("#(.*)",x[0]).group(1)
        # domain = re.search("@(.*?):",x[0]).group(1)
        uuid = re.search("vless://(.*?)@",x[0]).group(1)
        # path = re.search("path=(.*)&",x[0]).group(1)

        return {
  "meta": {
    "code": 200,
    "status": "success",
    "ip_address": DOMAIN,
    "message": "Create VLESS-WS Success"
  },
  "data": {
    "hostname": DOMAIN,
    "ISP": ISP,
    "CITY": kota,
    "username": remarks,
    "expired": exp,
    "uuid": uuid,
    "port": {
      "tls": "443",
      "none": "80",
      "any": "8080"
    },
    "path": {
      "stn": "/vless",
      "multi": "/yourbug/vless"
    },
    "link": {
      "tls": x[0],
      "none": x[1].replace(" ","")
    }
  }
}



def ssh():
    return


if __name__ == "__main__":
    print(trojan("whsvsv","1"))
