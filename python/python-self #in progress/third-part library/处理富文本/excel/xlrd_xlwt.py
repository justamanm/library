import xlrd
import xlwt
from xlutils.copy import copy


class ReadExcel:
    def open(self):
        #打开excel
        self.wb = xlrd.open_workbook('input.xlsx')

        # 获取sheet
        sheet_names = self.wb.sheet_names()
        print(sheet_names)
        self.sheet = self.wb.sheet_by_name("Sheet1")

    # 属性和方法
    def attribut(self):
        # 获取行列数
        self.cols_num = self.sheet.ncols
        self.rows_num = self.sheet.nrows
        print(self.cols_num, self.rows_num)

    def read_cell(self):
        # 获取单元格内容，索引从0开始
        cell_A1 = self.sheet.cell(0, 0).value   # 方式一
        cell_A1 = self.sheet.cell_value(0, 0)   # 方式二，不用加value
        cell_A1 = self.sheet.row(0)[0].value    # 方式三
        print(cell_A1)

    def read_rows_cols(self):
        # 通过索引获取，索引从0开始；返回列表
        row_01 = self.sheet.row_values(0)
        col_01 = self.sheet.col_values(0)
        print(row_01)
        print(col_01)

        # 循环遍历各行
        for curr_row in range(self.rows_num):
            row_value = self.sheet.row_values(curr_row)
            print('row%s value is %s' % (curr_row, row_value))

        for curr_col in range(self.cols_num):
            col_value = self.sheet.col_values(curr_col)
            print('col%s value is %s' % (curr_col, col_value))

    def copy_xlrd(self):
        # 将xlrd对象拷贝转化为xlwt对象
        self.wb_new = copy(self.wb)
        print(type(self.wb_new))

    def run(self):
        self.open()
        self.copy_xlrd()
        new_sheet = self.wb_new.get_sheet(0)
        new_sheet.write(0, 0, '第一行，第一列')
        self.wb_new.save("test.xls")


class WriteExcel:
    def create(self):
        self.wb = xlwt.Workbook()
        # 创建表格并指定位置
        self.sheet = self.wb.add_sheet('sheet1')

    def write_cell(self):
        self.sheet.write(0, 0, 'test')

    def save(self):
        self.wb.save('output.xlsx')

    def run(self):
        self.create()
        self.write_cell()
        self.save()


if __name__ == '__main__':
    write = WriteExcel()
    # write.run()

    read = ReadExcel()
    read.run()
