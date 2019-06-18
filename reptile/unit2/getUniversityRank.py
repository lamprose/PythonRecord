# 获取大学排名
import requests
import bs4
from bs4 import BeautifulSoup


# 获取指定url的HTML内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        return ''


# 爬取并填充数据
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([
                tds[0].string, tds[1].string, tds[2].string, tds[3].string,
                tds[4].string
            ])


# 格式化输出排名
# uname:查询具体学校名称排名
def printUlist(ulist, num=0, uname=""):
    str = "{0:^4}\t{1:{5}^15}\t{2:^6}\t{3:^4}\t{4:^5}"
    print(str.format("排名", "学校名称", "省市", "总分", "指标得分", chr(12288)))
    for i in range(0, len(ulist) if num == 0 else num):
        u = ulist[i]
        if (uname == ""):
            print(str.format(u[0], u[1], u[2], u[3], u[4], chr(12288)))
        else:
            if (u[1].find(uname) != -1):
                print(str.format(u[0], u[1], u[2], u[3], u[4], chr(12288)))


if __name__ == "__main__":
    uinfo = []
    url = "http://zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUlist(uinfo, uname="东华大学")
