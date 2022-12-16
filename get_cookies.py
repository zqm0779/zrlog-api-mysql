import requests
import urllib.request
import http.cookiejar

# 1. 登录系统，获取Cookie值

cookiejar = http.cookiejar.CookieJar()  #构建一个CookieJar对象实例来保存cookie  【CookieJar是对于Cookie类的一个类似管理类的封装】
handler = urllib.request.HTTPCookieProcessor(cookiejar)     #使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
opener = urllib.request.build_opener(handler)   #通过build_opener()来构建opener

# headers、请求登录接口，传递地址和参数
headers = {
    "Content-Type": "application/json"
}
url_login = 'http://localhost:8080/api/admin/login'
FormData = {'userName': 'root', 'password': 'b2e14b919db67e50a19cc0f507f5f370', 'https': False}     #<class 'dict'>
postdata = urllib.parse.urlencode(FormData).encode()    #<class 'bytes'>

request = urllib.request.Request(url_login, postdata)
response = opener.open(request) #访问系统地址，访问之后会自动保存cookie到cookiejar中
print(response)
for item in cookiejar:
    cookie = '%s=%s' % (item.name, item.value)
    print(cookie)
# headers['Cookie'] = cookie  # 向headers中追加Cookie，没有Cookie值，系统会认为用户尚未登录

# 2. 下载模板文件
# url = 'http://xxxx.xxx.xxxx/downloadTemplate?templateName=userTemplate.xlsx'
# r = requests.get(url, headers=headers)
# with open("userTemplate.xlsx", "wb") as code:
#     code.write(r.content)