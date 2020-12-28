from pdf2image import convert_from_path,convert_from_bytes
import fitz

pdf_bin_data = b''
pdf_path = ""

# pip install pdf2image
# 支持字节数据和文件转图片
def bytes_file2img():
    images = convert_from_bytes(pdf_bin_data)
    for i, image in enumerate(images):
        image.save("第%d页.png" % i, "PNG")

    # pdf文件转图片
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image.save("第%d页.png" % i, "PNG")


# pip install PyMuPDF
# 支持文件转图片
def pyMuPDF_fitz():
    pdfPath = "1.pdf"
    imagePath = "2.png"
    pdfDoc = fitz.open(pdfPath)

    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        pix.writePNG(imagePath)