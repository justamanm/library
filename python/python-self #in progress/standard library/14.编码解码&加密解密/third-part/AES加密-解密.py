# pip install pycryptodome
import json

from Crypto.Cipher import AES
import base64


def pad_it(sourceStr):
    counts = 16 - len(sourceStr) % 16
    byte_to_pad = bytes([counts])
    ret = sourceStr.encode() + counts * byte_to_pad
    return ret

# AES加密
def encrypt_aes(sr):
    key = "1234567812345678".encode()
    iv = "jszwfwhanweb2016".encode()

    generator = AES.new(key, AES.MODE_CBC, iv)
    crypt = generator.encrypt(sr)
    cryptedStr = base64.b64encode(crypt).decode()
    print(cryptedStr)

# AES解密
def decrypt_aes(cryptedStr):
    key = "1234567812345678".encode()
    iv = "jszwfwhanweb2016".encode()

    generator = AES.new(key, AES.MODE_CBC, iv)
    cryptedStr = base64.b64decode(cryptedStr)
    recovery = generator.decrypt(cryptedStr)
    print(recovery)

# AES解密，对解密字符串做处理后解密
def decrypt_aes_1(self):
    key = "1234567812345678".encode()
    generator = AES.new(key, AES.MODE_ECB)

    # 密文字符串的处理：不是base64解码
    # 1.字符串每两个字符转为16进制对应的数字
    # 2.将数字转为字节数组
    half_num = len(self.encrypted) // 2
    b = bytearray(half_num)
    for i in range(half_num):
        bin_num = int(self.encrypted[i * 2:(i + 1) * 2], 16)
        b[i] = bin_num

    # 解密后的字符串会有一个奇怪的空格，java中用trim()处理，这里直接打印出来，然后用strip()
    plain_text = generator.decrypt(b).decode().rstrip("")
    ret_dict = json.loads(plain_text)
    self.token = ret_dict["member"]["token"]
    print("token：" + self.token)


if __name__ == '__main__':
    sourceStr = "123456abcd"
    # 不足16位用16-n填充，比如10为则填充之后为123456abcd6666
    # 但要注意将6转换为16进制的字符串，即123456abcd\x06\x06\x06\x06\x06\x06
    sr = pad_it(sourceStr)
