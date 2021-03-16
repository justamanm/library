import hashlib
import time

time_str = str(int(time.time()*1000))
data = time_str + "318qwe"
data = "aimei359250053267769" + "AndroidCSDN-APPb85fF96d-7Aa4-4Ec1-bf1D-2133c1A45656"
data = "1587023542"
data = "bb35e90c25747407ce02ff4c20bcd066" + time_str

m = hashlib.md5()
m.update(data.encode())
ret = m.hexdigest()
print(ret)
print(len(ret))