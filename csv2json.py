import csv
import json

# 指定檔案
CSV_FILE = 'pcr.sample.csv'
JSON_FILE = 'pcr.json'

# 基本設定
netmask = "255.255.0.0"
dns = "192.168.8.8"
gateway = "192.168.8.254"

# dict, list 初始化
data={}
pc=[]

# 塞資料進 dict
data['netmask'] = netmask
data['dns'] = dns
data['gateway'] = gateway
# 讀取 csv 為 dict 塞進 pc list
with open(CSV_FILE, newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        pc.append(row)
# pc list 塞回 dict
data['pc'] = pc

# 轉 json 輸出
# print(json.dumps(data, indent=4))
with open(JSON_FILE, 'w') as outfile:
    json.dump(data, outfile, indent=4)