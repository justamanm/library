# pip install pycryptodome
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64


class Encrypt:
    def __init__(self,message="password"):
        self.message = message.encode()
        random_generator = Random.new().read
        rsa = RSA.generate(1024, random_generator)
        # 生成公钥和密钥
        self.rsa_private_key = rsa.exportKey()
        self.rsa_public_key = rsa.publickey().exportKey()

    def encrypt(self):  # 用公钥加密
        rsakey = RSA.importKey(self.rsa_public_key)
        cipher = PKCS1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(self.message))
        print(cipher_text)
        return cipher_text

    def decrypt(self,cipher_text):  # 用私钥解密
        rsakey = RSA.importKey(self.rsa_private_key)
        cipher = PKCS1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(cipher_text), None)
        print(text.decode())
        return text


if __name__ == '__main__':
    # 要加密的字符串
    to_enc_str = "xxx"
    enc = Encrypt(to_enc_str)
    crypt_text = enc.encrypt()
    enc.decrypt(crypt_text)





