import urllib.request
import json
import subprocess
import os
import uuid

JSON_URL = 'https://your_server/pcr.json'
n_name = ''
mac_addr = hex(uuid.getnode()).replace('0x', '').upper()
response  = urllib.request.urlopen(JSON_URL)
response  = response.read().decode("utf-8")
data = json.loads(response)
for row in data['pc']:
    if row['mac'] == mac_addr:
        n_name = row['name']
        n_ip = row['ip']
nic = '乙太網路'
n_mask = data['netmask']
n_gw  = data['gateway']
n_dns = data['dns']        
if n_name:
    print('MAC address {} found !'.format(row['mac']))
    print('ComputerName: ' + row['name'])
    print('IP Address: ' + row['ip'])
    print('setting DNS...')
    subprocess.call(['netsh', 'interface', 'ipv4', 'set', 'dnsservers', nic, 'static', n_dns])
    print('setting IP...')
    subprocess.call(['netsh', 'interface', 'ipv4', 'set', 'address', nic, 'static', n_ip, n_mask, n_gw, '1'])
    print('setting Computer Name...')
    subprocess.call(['powershell.exe', "Rename-Computer -NewName "  + n_name])
    print('done, please reboot the pc...')
else:
    print('data not found')