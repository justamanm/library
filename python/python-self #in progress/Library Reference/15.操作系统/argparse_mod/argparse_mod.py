import argparse


# 取出参数
# name是Namespace对象，不能转成列表
def run(name):
    print(name)
    for attr in dir(name)[-3:]:
        print(getattr(name, attr))


# 创建解析器
parser = argparse.ArgumentParser(description="used for test")

# 位置参数，没有前缀-或--，argparse使用前缀来判断是位置还是可选参数
# 不能写参数名，如myname 1，只能写1
# 顺序：命令行中的参数顺序必须与代码中的定义顺序一致
# 别名：不能有别名
# 使用：python argparse_mod.py myname参数(不能写-myname，否则报错)
parser.add_argument("myname")   # 位置参数的定义不能传require

# 必选参数
# 与位置参数比较：在命令中出现的位置可以随意，但和位置参数一样必须要有
# 必须要写上参数名，如-d 1，而不能直接写1
# 一般一个字母用-，多个字母用--，一个参数可以定义多种写法；使用多种写法在解析时可以随意切换，如args.d/args.debug
# 别名：可以有别名，别名命令行中可随意替换，但在解析时不能用，即可以用args.d，args.debug会报错
# 使用：全称写在前面，代码解析时用比较清晰；简写写在后面，用于命令行简洁传参
parser.add_argument("-s", required=True)
parser.add_argument("--debug", "-d", required=True)

# 可选参数，有前缀-或--
# 顺序，命令行可与代码定义顺序不一致，可有可无
# 使用：python argparse_mod.py --optical xx(必须写--optical)
parser.add_argument("--optical")

# 添加子命令
# 子命令可以完全不写，即使子命令中有位置参数，必选参数
# 即在使用时可以当作完全没有子命令
# 可实现： python file.py myname sub --subname xxx
subparsers = parser.add_subparsers(help="Rasa commands")


# 父解析器
# 必须设add_help为False，否则会报错
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument("--parent")
parent_parser_list = [parent_parser]


# parents，继承父parse的参数
# 使用：python xx.py xx sub --parent pa --name1 subs
parser_single = subparsers.add_parser('sub', parents=[parent_parser])
parser_single.add_argument("--name1")
# 配置命令对应的执行函数
parser_single.set_defaults(func=run)


# 执行：python argparse_mod.py abc sub --parent pa --name1 subparser
args = parser.parse_args()
print("-----------")
print(args)
# print(type(args))

if hasattr(args, "func"):
    print("have func attr")
    args.func(args)


