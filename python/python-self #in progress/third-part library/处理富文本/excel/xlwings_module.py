# pip install xlwings

import xlwings as xw


class WriteExcel:
    def create(self):
        self.wb = xw.Book()  # 这将创建一个新的工作簿



class ReadExcel:
    def open(self):
        self.wb = xw.Book('FileName.xlsx')
        self.sheet = self.wb.sheets['Sheet1']   # 获取sheet