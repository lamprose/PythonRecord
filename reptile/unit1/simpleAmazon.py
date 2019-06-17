# 简单亚马逊商品页面爬取
import requests
url = "https://www.amazon.cn/dp/B07NXT7LKF"
try:
    r = requests.get(url)
    # 模拟浏览器访问
    header = {'user-agent': 'Mozilla/5.0'}
    r.headers = header
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except Exception as e:
    print(e)
