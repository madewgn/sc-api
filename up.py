import requests

do = "http://do.madewgn.eu.org:8000/update"
linode = "http://linode.madewgn.eu.org:8000/update"
id_linode = "http://id-linode.madewgn.eu.org:8000/update"

response_do = requests.get(do)
response_linode = requests.get(linode)
response_id_linode = requests.get(id_linode)

print("Response from do.madewgn.eu.org:8000/update:")
print(response_do.text)

print("\nResponse from linode.madewgn.eu.org:8000/update:")
print(response_linode.text)

print("\nResponse from id-linode.madewgn.eu.org:8000/update:")
print(response_id_linode.text)

