import pandas as pd


class Excel:
    # 打开文件
    def open(self):
        # 方式一：默认获取第一个sheet的内容
        self.df1 = pd.read_excel("input1.xlsx")
        self.df2 = pd.read_excel("final.xlsx")

        # 方式二：获取指定sheet
        # df = pd.read_excel("input.xlsx", sheet_name="Sheet1")
        # df = pd.read_excel("input.xlsx", sheet_name=0)
        # head_5 = df.head()
        # print(type(head_5))
        # print(head_5)

        # 方式三：获取多个sheet
        # df = pd.read_excel("input.xlsx", sheet_name=["Sheet1", "Sheet2"])
        # print(df.values)

    # 属性和方法
    def attribut(self):
        # 获取行数和列数：
        print(self.df1.shape)

    def run(self):
        self.open()
        self.attribut()


if __name__ == '__main__':
    excel = Excel()
    excel.run()