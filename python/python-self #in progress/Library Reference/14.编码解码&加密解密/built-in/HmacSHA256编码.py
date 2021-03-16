import base64
import hmac     # 内置模块
from hashlib import sha256

encrypt_str = "123456"
appsecret = "0uadsfaadnvada87s6d8f7a3n".encode()  # 秘钥
data = encrypt_str.encode()  # 加密数据
signature = base64.b64encode(hmac.new(appsecret, data, digestmod=sha256).digest())
ca_signature = signature.decode()
print(ca_signature)