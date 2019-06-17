# 简单模拟百度搜索并爬取页面
import requests
url = "http://www.baidu.com/s"
params = {'wd': 'Python'}
try:
    r = requests.get(url, params=params)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.url)
    print(r.text[:3000])
except Exception as e:
    print(e)
