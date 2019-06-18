# 爬取豆瓣评论生成词云
import re
import requests
import wordcloud
import jieba
import os


# 得到页面全部内容
def askURL(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except Exception as e:
        print(e)
        return ""


# 获取评论
def getData(baseurl):
    html = askURL(baseurl.format("0", "P"))
    # 获取看过评论数量
    p = re.search(r'>看过\((?P<ptotal>\d*)\)</', html, re.M)
    # 获取想看评论数量
    f = re.search(r'>想看\((?P<ftotal>\d*)\)</', html, re.M)
    ptotal = ftotal = 0
    if p:
        ptotal = int(p.group('ptotal'))
    if f:
        ftotal = int(f.group('ftotal'))
    total = [{'type': 'P', 'total': ptotal}, {'type': 'F', 'total': ftotal}]
    for k in total:
        # print(k['type'], k['total'])
        if k['total'] != 0:
            for i in range(0, 10 if k['total'] > 200 else k['total'] // 20):
                html = askURL(baseurl.format(i * 20, k['type']))
                # 获取页面所有评论内容
                commentlist = re.findall(r'<span.*class="short">(.*)</span>',
                                         html, re.M)
                # 将评论写入评论文件
                with open("comment.txt", "a+", encoding="utf-8") as f:
                    for comment in commentlist:
                        f.write(comment)
                        f.write('\n')


# 生成词云
def genWordCloud():
    with open("comment.txt", "r", encoding="utf-8") as f:
        # 读取评论文件内容
        txt = f.read()
        # jieba 解析词语
        txtlist = jieba.lcut(txt)
        string = " ".join(txtlist)
        # 生成词云对象
        w = wordcloud.WordCloud(width=1000,
                                height=700,
                                background_color='white',
                                font_path='msyh.ttc')
        w.generate(string)
        # 输出图片
        w.to_file('out.png')


def main():
    # 输入id
    id = input("请输入豆瓣电影id")
    baseurl = 'https://movie.douban.com/subject/' + id + '/comments?start={}&limit=20&sort=new_score&status={}'
    # 如果存在输出文件则删除
    if (os.path.exists("comment.txt")):
        os.remove("comment.txt")
    getData(baseurl)
    genWordCloud()


if __name__ == "__main__":
    main()