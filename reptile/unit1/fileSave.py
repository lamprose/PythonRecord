# 网络图片或视频的爬取和存储
import os
import requests
# 图片链接
url = "https://img12.360buyimg.com/n5/s54x54_jfs/t1/41104/29/5202/217626/5cebc531Ee9021f58/eb81e63fe725a946.jpg"
# 视频链接
# url = "https://vod.300hu.com/4c1f7a6atransbjngwcloud1oss/2ae2859f188242305743343617/v.f30.mp4"
root = "D://"
# 设置保存图片文件名
path = root + url.split('/')[-1]
try:
    # 如果不存在存储文件夹则创建
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, "wb") as f:
            # 以二进制形式写入文件
            f.write(r.content)
            print("保存成功")
    else:
        print("保存失败")
except Exception as e:
    print(e)
