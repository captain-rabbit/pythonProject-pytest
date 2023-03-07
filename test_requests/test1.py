import requests

#requests get的使用
r = requests.get('https://api.github.com/events')
print(r.json())  #返回json数据
print(r.status_code)  #返回状态码
print(r.text)   #返回文本