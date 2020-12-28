from lxml import etree

import requests


headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
url = "https://www.baidu.com"

resp = requests.get(url, headers=headers)
page = resp.content.decode()

ret = etree.HTML(page)

# 使用xpath语法获取数据
doc_url = ret.xpath("//div[@class='jdtsfs_btn']/a[2]/@href")[0]



