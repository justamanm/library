import os
import sys
from flask import Flask, request

# 配置模块查找路径，在环境变量中添加根路径
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

# from modules import create_app
# from config.config_flask import pattern
from ncp import WeWillWin
# "dev": DevConfig；"prod": ProdConfig；日志的level：dev-DEBUG,prod-CRITICAL
# app = create_app(pattern)
app = Flask(__name__)


@app.route("/")
def map():
    data = request.args
    province = data.get("p")
    city = data.get("c")
    print(province, city)

    www = WeWillWin(province, city)
    html_data = www.run_map()
    return html_data


@app.route("/line")
def line():
    data = request.args
    type = data.get("type")
    www = WeWillWin()
    html_data = www.run_line(type)
    return html_data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)




