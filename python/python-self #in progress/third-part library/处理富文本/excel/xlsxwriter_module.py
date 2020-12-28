import xlsxwriter


class WriteExcel:
    def create(self):
        # 创建一个新工作簿
        self.wb = xlsxwriter.Workbook("data_new.xlsx")
        # 添加一个工作表
        self.sheet = self.wb.add_worksheet('sheet01')

    def set_style(self):
        self.sheet.set_column('B:D', 40)  # 为B-D列设置列宽为40
        self.sheet.set_row(2, 30)  # 为第二行设置行高为30

        # 添加用于突出显示单元格的粗体格式。
        self.bold = self.wb.add_format({'bold': True})

        # 为显式钱的单元格添加数字格式。
        self.money = self.wb.add_format({'num_format': '$#,##0'})

        # 设置样式
        self.formats = self.wb.add_format({
            'font_color': 'yellow',
            # 'bold': 2,
            'underline': 1,
            'font_size': 12,
            'fg_color': 'red'
        })


    def write(self):
        # 写入超链接
        self.sheet.write_url('B1', 'https://www.baidu.com/', self.bold)  # 隐式显示
        self.sheet.write_url('B2', 'https://www.baidu.com/', string='百度一下')  # 显示string
        self.sheet.write_url('B3', 'https://www.baidu.com/', tip='前往百度')  # 鼠标悬浮提示信息
        self.sheet.write_url('B4', 'https://www.baidu.com/', cell_format=self.formats)  # 按格式显示
        self.sheet.write_url('B5', 'C:/files/file')
        self.sheet.write_url(1, 2, 'https://www.baidu.com/', cell_format=self.formats, string='hello', tip='click')
        # 写入一个非超链接的URL
        self.sheet.write_string('B6', 'http://www.baidu.com/', self.money)

        self.sheet.write_blank()
        self.wb.close()