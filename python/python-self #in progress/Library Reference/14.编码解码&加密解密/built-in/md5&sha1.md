md5

- MD5由[MD4](https://zh.wikipedia.org/wiki/MD4)、MD3、[MD2](https://zh.wikipedia.org/w/index.php?title=MD2&action=edit&redlink=1)改进而来
- 输出32个十六进制的字符
- 一个字符占4位，共128bit
- 缺点：2004年，证实MD5算法无法防止[碰撞攻击](https://zh.wikipedia.org/w/index.php?title=碰撞攻击&action=edit&redlink=1)，因此不适用于安全性认证，如[SSL](https://zh.wikipedia.org/wiki/SSL)[公开密钥认证](https://zh.wikipedia.org/wiki/公開金鑰認證)或是[数字签名](https://zh.wikipedia.org/wiki/數位簽章)等用途



[SHA家族](https://zh.wikipedia.org/wiki/SHA%E5%AE%B6%E6%97%8F)

sha1

- 输出40个十六进制的字符
- 一个字符占4位，共160bit



sha2

- 包括SHA-224、SHA-256、SHA-384、SHA-512、SHA-512/224、SHA-512/256，虽然至今尚未出现对SHA-2有效的攻击，但它的算法跟SHA-1基本上仍然相似
- sha256最为通用
  - 输出64个十六进制的字符
  - 一个字符占4位，共256bit



sha3

- 与之前算法不同的，可替换的加密散列算法
- 暂未使用