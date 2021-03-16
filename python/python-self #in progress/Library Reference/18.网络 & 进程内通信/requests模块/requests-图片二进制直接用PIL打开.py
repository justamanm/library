import io
from PIL import Image  # 注意我的Image版本是pip3 install Pillow==4.3.0
import requests

res = requests.get('http://p1.pstatp.com/list/300x196/pgc-image/152923179745640a81b1fdc.webp', stream=True)  # 获取字节流最好加stream这个参数,原因见requests官方文档

byte_stream = io.BytesIO(res.content)  # 把请求到的数据转换为Bytes字节流(这样解释不知道对不对，可以参照[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431918785710e86a1a120ce04925bae155012c7fc71e000)的教程看一下)

roiImg = Image.open(res.content)   # Image打开Byte字节流数据

imgByteArr = io.BytesIO()     # 创建一个空的Bytes对象

roiImg.save(imgByteArr, format='PNG') # PNG就是图片格式，我试过换成JPG/jpg都不行

imgByteArr = imgByteArr.getvalue()   # 这个就是保存的图片字节流

# 下面这一步只是本地测试， 可以直接把imgByteArr，当成参数上传到七牛云
with open("./abc.png", "wb") as f:
    f.write(imgByteArr)
