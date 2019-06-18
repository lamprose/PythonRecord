# 获取一个链接下所有链接
import requests
from bs4 import BeautifulSoup
import re
links = []


def getAllLink(a):
    try:
        r = requests.get(a)
        r.raise_for_status()
        demo = BeautifulSoup(r.text, "html.parser")
        # 寻找所有带有链接的a标签
        tagList = demo.find_all(
            href=re.compile("(?isu)(http\://[a-zA-Z0-9\.\?/&\=\:]+)"))
        for tag in tagList:
            # 若爬取链接个数大于100，则退出
            if (len(links) > 100):
                break
            link = tag.attrs['href']
            # 若链接爬虫已爬取则退出
            if (link not in links):
                print(link)
                links.append(link)
                if (link.split('/')[-1].find('.') == -1):
                    getAllLink(link)
    except Exception:
        print("error")


getAllLink("http://www.baidu.com/s?wd=Python")