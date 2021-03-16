import hashlib


def get_str_sha1_secret_str(res:str):
    """
    使用sha1加密算法，返回str加密后的字符串
    """
    sha = hashlib.sha1(res.encode('utf-8'))
    encrypts = sha.hexdigest()
    print(encrypts)
    print(len(encrypts))
    return encrypts


def get_str_sha2_secret_str(res:str):
    """
    使用sha256加密算法，返回str加密后的字符串
    """
    sha = hashlib.sha256(res.encode('utf-8'))
    encrypts = sha.hexdigest()
    print(encrypts)
    print(len(encrypts))
    return encrypts


if __name__ == '__main__':
    get_str_sha2_secret_str("asfeadfasdfasdfaew232asfd")