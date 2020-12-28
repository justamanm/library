import requests

url = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=重庆"
# url = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=陕西&city=西安"
resp = requests.get(url)
print(resp.content.decode())