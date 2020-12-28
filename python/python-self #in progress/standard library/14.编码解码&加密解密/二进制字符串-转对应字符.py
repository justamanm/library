
# ---------------------------编码 字母----------------------------
def encode_abc():
    data = "abc"
    # 编码后返回字节数组
    data_bytes = data.encode()

    # 遍历获取每个字节码
    for i in data_bytes:
        # bin(i): '0b1100001'
        print(bin(i).strip("0b"))


# ---------------------------编码 中文----------------------------
def encode_other():
    data = "今天"
    data_bytes1 = data.encode("utf8")
    data_bytes2 = data.encode("gbk")
    for i in data_bytes1:
        # i打印处理是二进制对应的数字
        print(i)
        # bin(i):返回数字对应的二进制字符串
        # ["11100100", "10111011", "10001010", "11100101", "10100100", "10101001"]
        print(bin(i))
    print("-"*20)
    for j in data_bytes2:
        # bin(j): ["10111101", "11110001", "11001100", "11101100"]
        print(bin(j))


# ---------------------------解码 字母----------------------------
def decode_abc():
    # 字母在每种编码方式中获取的二进制都是一样的，所以用chr即可获取到原字符
    # 但像中文‘我’，在各个编码方式中对应的二进制不同，当然也就不能用chr方法了，要用decode()
    a = "1001010 1110101 1110011 1110100 1100110 1101111 1110010 1000110 1110101 1101110"
    b_list = a.split(" ")
    ret = ""
    print(b_list)
    for i in b_list:
        c = chr(int(i, 2))
        print(c)


# ---------------------------解码 中文----------------------------
def decode_other():
    # utf8编码
    ret1 = ["11100100", "10111011", "10001010", "11100101", "10100100", "10101001"]
    # gbk编码
    ret2 = ["10111101", "11110001", "11001100", "11101100"]
    # 二进制字符串转为真的二进制
    # 1.二进制字符串转数字，再转16进制
    # 2.加前缀\x，合并
    # 3.加前缀b""，解码即可
    str_hex = ""
    for i, byte in enumerate(ret2):
        num = int(byte, 2)
        char_hex = hex(num).strip("0x")
        str_hex += "\\x" + char_hex
    print(str_hex)

    # \x用来表示：这不是字符串而是二进制码
    # 只能将str_hex手动复制，加前缀\x，在解码
    ret = b"\xbd\xf1\xcc\xec".decode("gbk")
    print(ret)


if __name__ == '__main__':
    # encode_other()
    decode_other()
