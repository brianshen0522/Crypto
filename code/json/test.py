import json

ip_file = open("ip.json", "r")
#print(ip_file.read())
ip_list = json.loads(ip_file.read())
print(ip_list[f'{input("id:")}'])