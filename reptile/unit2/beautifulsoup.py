# beautifulsoup的简单使用
import requests
# 导入beautifulsoup库
# 安装方法pip install beautifulsoup4
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
try:
    r.raise_for_status()
    demo = r.text
    # 初始化beautifulsoup类
    soup = BeautifulSoup(demo, "html.parser")
    # 获取网页title标签
    print(soup.title)
    print(soup.a.parent.name)
    for tag in soup.body.contents:
        print(tag)
except Exception as e:
    print(e)