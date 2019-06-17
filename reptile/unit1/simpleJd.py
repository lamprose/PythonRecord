# 简单京东商品页面的爬取
import requests
url = "https://item.jd.com/100003582587.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # 只打印前1000个字符
    print(r.text[:1000])
except Exception as e:
    # 打印出错误具体信息
    print(e)
