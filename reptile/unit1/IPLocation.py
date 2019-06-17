# IP地址归属地的自动查询
import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + "116.229.112.28")
    r.raise_for_status()
    print(r.text[-1000:])
except Exception as e:
    print(e)