import requests

base_url = 'http://172.232.250.13:8000/'

# Contoh penggunaan endpoint '/vps/trojanws'
# params = {'u': 'shzbsb', 'pw': 'absbsbs', 'exp': '1'}
# response_trojan = requests.post(base_url + 'vps/trojanws', params=params)
# print('Response trojan:', response_trojan.text)
# import requests

# Data yang akan dipost ke endpoint /vps/sshvpn
data_ssh = {
    "username": "user_ssh",
    "expiration": "2024-12-31"
}

# Data yang akan dipost ke endpoint /vps/trojanws
data_trojan = {
    "username": "user_trojan",
    "expiration": "1"
}

# Data yang akan dipost ke endpoint /vps/vmessws
data_vmess = {
    "username": "user_vmess",
    "expiration": "2024-12-31"
}

# Data yang akan dipost ke endpoint /vps/vlessws
data_vless = {
    "username": "user_vless",
    "expiration": "2024-12-31"
}

# Melakukan POST request ke masing-masing endpoint
# response_ssh = requests.post("http://localhost:8000/vps/sshvpn", json=data_ssh)
response_trojan = requests.post(f"{base_url}vps/trojanws", json=data_trojan)
# response_vmess = requests.post("http://localhost:8000/vps/vmessws", json=data_vmess)
# response_vless = requests.post("http://localhost:8000/vps/vlessws", json=data_vless)
#
# Menampilkan hasil dari respons
# print("Response /vps/sshvpn:", response_ssh.status_code)
print("Response /vps/trojanws:", response_trojan.status_code)
# print("Response /vps/vmessws:", response_vmess.status_code)
# print("Response /vps/vlessws:", response_vless.status_code)
#
