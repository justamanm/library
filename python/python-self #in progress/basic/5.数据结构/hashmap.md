

<img src="hashmap.png" width="40%">



hash算法

- 有很多，见布隆过滤器
- 不同的hash算法，可以获得不同的整形数字

对hash后获取的数字取余，放到对应的哈希表位置，如果多个字符串取余后的值相同，则冲突

冲突的解决：

- 开放定址法，依次探测冲突位置的下一个位置。如，在哈希表的位置2处发生了冲突，则探测位置3处，以此类推
- 链地址法，链表中存放原数字用来标定唯一性



布隆过滤器中有用到哈希表

