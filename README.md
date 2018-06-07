# Get PC info

## 環境需求

* python3.x for win
* 關閉 UAC (當然可以用最高權限跑, 但是自動化就...)
* 一張網卡 (兩張會抓錯Rrr)

## 使用方式

1. 依照 pcr.sample.json 建立所需的資與網卡/IP/電腦名稱的資料
2. 把上述 json 丟在某 web server 上 ex: https://your_server/pcr.json
3. 修改 getpcinfo.py 內的 JSON_URL 上面網址
4. python getpcinfo.py 搞定收工

## 轉檔工具

* 可將 csv 檔轉為 json
* csv 範例檔為 pcr.sample.csv
* csv2json.py 內有網路的基本設定和檔名設定
* 使用方法 python csv2json.py 就會依照上述設定輸出 json (預設 pcr.json)

## 注意

* 網路介面 預設名稱為 "乙太網路" 如有不同請修改 getpcinfo.py 內的 nic = '乙太網路' 
* n_name = '' 暫勿修改, 待未來改版用聰明一點的方法
