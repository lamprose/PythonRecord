# 简单requests请求
# 导入requests库
import requests
url = "http://www.baidu.com"
# 进行简单的get请求,返回response对象
r = requests.get(url)
# 返回代码是200(正常)
if (r.status_code == 200):
    # 将编码格式设为内容识别的编码格式，防止出现乱码
    r.encoding = r.apparent_encoding
    # 打印网络内容
    print(r.text)
