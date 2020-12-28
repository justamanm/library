# 1.数字转二进制字符串，注意：返回的是字符串
bin(2)  # '0b10'

# 2.bytes()等价于b""，不可变
bytes(2)    # b'\x00\x00',初始化2个字节
bytes("a", "utf8") == bytes(b"a")

# 3.bytearray(长度)，可变，存放的是整型
barray = bytearray(6)
barray[0] = 13

# 不能直接构造字节，所以也就无法将二进制字符串转换为对应的字节，只能手动的复制再转换
ret2 = ["10111101", "11110001", "11001100", "11101100"]
str_hex = ""
for i, byte in enumerate(ret2):
    num = int(byte, 2)
    char_hex = hex(num).strip("0x")
    str_hex += "\\x" + char_hex
print(str_hex)
# 在手动复制，加前缀b""，解码

