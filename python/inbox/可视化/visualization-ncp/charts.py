from datetime import datetime

import pyecharts.options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Line
from pyecharts.charts import Timeline

# date = datetime(2020, 2, 10)
# date_str = date.strftime("%Y %m %d")
# print(date_str)
c = (
        Line()
        .add_xaxis([datetime(2020, 2, 10),datetime(2020, 2, 11),datetime(2020, 2, 12),datetime(2020, 2, 13)])
        .add_yaxis("商家A", [1,2,3,7])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Line-数值 X 轴"),
            xaxis_opts=opts.AxisOpts(type_="time"),

        )
    )
c.render()


