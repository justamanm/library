from urllib.parse import unquote, urlencode, parse_qs, quote

params = {
    "name":"哈","age":12
}
# 字典-编码
ret = urlencode(params)
print(ret)
# 字典-解码
ret = parse_qs(ret)
print(ret)

url = "name=哈&age=12"
# 字符串-编码
ret = quote(url)
print(ret)
# 字符串-解码
ret = unquote(ret)
print(ret)