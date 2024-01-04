import requests

base_url = 'http://172.232.250.13:8000/'

# Contoh penggunaan endpoint '/vps/trojanws'
params = {'u': 'shzbsb', 'pw': 'absbsbs', 'exp': '1'}
response_trojan = requests.post(base_url + 'vps/trojanws', params=params)
print('Response trojan:', response_trojan.text)

