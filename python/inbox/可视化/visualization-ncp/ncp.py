import json
import os
import re
from urllib.parse import unquote
import requests
from pyecharts.charts import Line, BMap
import pyecharts.options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
    }


class WeWillWin:
    def __init__(self, province=None, city=None):
        self.province = province
        self.city = city

    def get_all_data(self):
        """
        :return:
        """
        url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
        resp = requests.get(url, headers=headers)
        ret = resp.content.decode()
        # print(ret)
        ret_del_trans = re.sub(r"\\\"", "\"", ret)
        ret_del_dot1 = re.sub(r"data\":\"{", "data\":{", ret_del_trans)
        ret_del_dot2 = re.sub(r"}]}\"}", "}]}}", ret_del_dot1)
        try:
            """数据格式：
            {
                "ret": 0,
                "data": {
                    "lastUpdateTime": "2020-02-10 14:28:02",
                    "chinaTotal": {
                        总计的确诊、疑似
                    },
                    "chinaAdd": {
                        增加的确诊、疑似
                    },
                    "isShowAdd": true,
                    "chinaDayList": [
                        {
                            从1.20到现在每天的
                        }],
                    "chinaDayAddList": [
                        {
                            从1.20到现在每天新增的
                        }],
                    "ereaTree":[
                        {"name":"中国"...,'children': [{'name': '湖北', 'today':{}},{'name': '浙江', 'today':{}}]}
                        {"name": "日本","today": {"confirm": 0,},"total": {"confirm": 96,}},
                    ],
                    "articleList":[]
                }
            }
            """
            data = json.loads(ret_del_dot2)["data"]
            # 总计的人数，字典
            self.chinaTotal = data["chinaTotal"]
            # 总新增人数，字典
            self.chinaAdd = data["chinaAdd"]
            # 1.20号到现在的每日数据，列表
            self.chinaDayList = data["chinaDayList"]
            # 1.20号到现在的每日新增数据，列表
            self.chinaDayAddList = data["chinaDayAddList"]
            # 全球数据，列表-各国字典
            self.ereaTree = data["areaTree"]
            # 中国数据，字典；ereaTree列表的第一个是中国
            self.china_data = self.ereaTree[0]["children"]
            print("总计的人数：" + str(self.chinaTotal))
            print("总新增人数：" + str(self.chinaAdd))
            print("1.20号到现在的每日数据：" + str(self.chinaDayList))
            print("1.20号到现在的每日新增数据：" + str(self.chinaDayAddList))
            print("-"*50)
        except Exception as e:
            print(str(e))

    def get_country_data_line(self):
        self.date_list = []
        self.confirm_list = []
        self.suspect_list = []
        self.heal_list = []
        for day_data in self.chinaDayList:
            date = re.sub(r"\.", "-", day_data["date"])
            confirm = day_data["confirm"]
            suspect = day_data["suspect"]
            heal = day_data["heal"]
            self.date_list.append(date)
            self.confirm_list.append(confirm)
            self.suspect_list.append(suspect)
            self.heal_list.append(heal)
        print(self.date_list)
        print(self.confirm_list)
        print(self.suspect_list)
        print(self.heal_list)

    def get_country_data_map(self):
        """
        国家地图中展示各省的数据
        :return:
        """
        self.map_list = []
        for province in self.china_data:
            p_name = province["name"]
            # print(province["today"])
            p_total = province["total"]
            p_confirm = province["total"]["confirm"]
            p_suspect = province["total"]["suspect"]
            self.map_list.append((p_name, p_confirm))
        print(self.map_list)

    def get_province_data(self):
        """
        省地图中展示各市的数据
        china_data格式：
              [{'name': '湖北', 'today':{}, 'total':{},
               'children':[{'name': '武汉',
                            'today': {'confirm': 13436, 'suspect': 0, 'dead': 0, 'heal': 0, 'isUpdated': True},
                            'total': {'confirm': 32994, 'suspect': 0, 'dead': 1036, 'heal': 1915, 'deadRate': 3.14, 'healRate': 5.8}},
                           {'name': '孝感'...}]
              {'name': '陕西', 'today':{}, 'total':{},'children':[]}]
        :return:
        """
        province_index = {}
        for index, province in enumerate(self.china_data):
            p_name = province["name"]
            province_index[p_name] = index

        p_index = province_index[self.province]
        city_list = self.china_data[p_index]["children"]
        self.map_list = []
        for city_data in city_list:
            if self.province in ["天津", "上海", "重庆", "北京"]:
                c_name = city_data["name"] + "区"
            else:
                c_name = city_data["name"] + "市"
            c_confirm = city_data["total"]["confirm"]
            self.map_list.append((c_name, c_confirm))

    def get_city_data(self):
        """
        城市地图中展示的是各县区的数据
        TODO 无区县数据接口
        省级：从1.28到现在每天的数据
        市级：从1.28到现在每天的数据
        :return:
        """
        url = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=陕西"
        # url = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=陕西&city=西安"
        ret_url = unquote(url)
        resp = requests.get(url, headers=headers)
        self.map_list = []


    def draw_echarts(self, area="china"):
        title = "全国" if area=="china" else area

        # 自定义分段 color，可以用取色器取色
        if any([self.province, self.city]):
            pieces = [
                {'max': 0, 'label': '0人', 'color': '#e2ebf4'},
                {'min': 1, 'max': 9, 'label': '1-9人', 'color': '#ffefd7'},
                {'min': 10, 'max': 49, 'label': '10-49人', 'color': '#ffd2a0'},
                {'min': 50, 'max': 99, 'label': '10-49人', 'color': '#ffb880'},
                {'min': 100, 'max': 499, 'label': '100-499人', 'color': '#fe8664'},
                {'min': 500, 'max': 999, 'label': '500-999人', 'color': '#e64b47'},
                {'min': 1000, 'max': 9999, 'label': '1000-9999人', 'color': '#c91014'},
                {'min': 10000, 'label': '10000人及以上', 'color': '#9c0a0d'},
            ]
        else:
            pieces = [
                {'min': 1, 'max': 9, 'label': '1-9人', 'color': '#ffefd7'},
                {'min': 10, 'max': 99, 'label': '10-99人', 'color': '#ffd2a0'},
                {'min': 100, 'max': 499, 'label': '100-499人', 'color': '#fe8664'},
                {'min': 500, 'max': 999, 'label': '500-999人', 'color': '#e64b47'},
                {'min': 1000, 'max': 9999, 'label': '1000-9999人', 'color': '#c91014'},
                {'min': 10000, 'label': '10000人及以上', 'color': '#9c0a0d'},
            ]

        # 绘制地图
        map = Map()
        map.set_global_opts(
            title_opts=opts.TitleOpts(title=f"{title}疫情地图"),
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces)
        )

        # 将数据导入到地图中，省市名称：pyecharts.datasets.map_filenames.json
        print(self.map_list)
        map.add(f"{title}确诊人数", self.map_list, maptype=area)
        self.html_data = map.render("ncp_map.html")

        # html转成图片
        # img_path = os.path.join(os.getcwd(), "ncp_map.png")
        # html_path = os.path.join(os.getcwd(), "ncp_map.html")
        # make_snapshot(snapshot, map.render("ncp_map.html"), img_path, delay=2)

    def draw_line(self, t):
        c = Line()

        c.add_xaxis(self.date_list)
        # s-疑似，c-确诊
        if t == "s":
            c.add_yaxis("疑似", self.suspect_list)
        elif t == "c":
            c.add_yaxis("确诊", self.confirm_list)
        else:
            c.add_yaxis("确诊", self.confirm_list)
            c.add_yaxis("疑似", self.suspect_list)
        c.set_global_opts(title_opts=opts.TitleOpts(title="新冠肺炎实时数据"), xaxis_opts=opts.AxisOpts(type_="category"))
        self.html_data = c.render("1.html")

    def draw_plt(self):
        pass

    def draw_baidu(self):
        BAIDU_AK = "KGjS1jSo0chPxqOdZjFwPxOamK8eIO0v"
        c = (
            BMap()
                .add_schema(
                baidu_ak=BAIDU_AK,
                center=[120.13066322374, 30.240018034923],
                )
                .add(
                "bmap",
                [list(z) for z in zip(Faker.provinces, Faker.values())],
                label_opts=opts.LabelOpts(formatter="{b}"),
                )
                .set_global_opts(title_opts=opts.TitleOpts(title="BMap-基本示例"))
        )
        c.render("ncp_baidu.html")

    def run_map(self):
        self.get_all_data()
        print(self.province, self.city)
        if self.province or self.city:
            if self.city in ["城市", "天津", "上海", "重庆", "北京", None]:
                print("province")
                self.get_province_data()
                self.draw_echarts(self.province)
            else:
                print("city")
                self.get_city_data()
                self.draw_echarts(self.city)
        else:
            print("country")
            self.get_country_data_map()
            self.draw_echarts()

        return self.html_data

    def run_line(self, t=None):
        self.get_all_data()
        self.get_country_data_line()
        self.draw_line(t)
        return self.html_data


if __name__ == '__main__':
    www = WeWillWin("陕西", )
    www.run_map()