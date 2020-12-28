from PIL import Image


class ImageProcess:
    def open(self):
        path = "../num_pic/7.png"
        self.im = Image.open(path)

    # PIL中图片有九种不同模式，参考：https://blog.csdn.net/z1314520cz/article/details/83034421
    # 直接保存的图片无法正常显示，需要转换图片
    # L-灰度模式
    def convert2model(self, path):
        self.im.convert('RGB')
        self.im.save(path, 'JPEG')

    # 压缩为280x280像素大小
    def compress_pixel(self):
        width = 280
        height = 280
        out_pic = self.im.resize((width, height), Image.ANTIALIAS)
        out_pic.save("1.jpg")

    def run(self):
        self.open()


if __name__ == '__main__':
    i = ImageProcess()
    i.run()