
import re


# 如果没有 "#coding:utf-8"在第一行，下面的正则会报错:SyntaxError: Non-UTF-8 code starting with '\xe7' in file
sentence = "abc"
ret = re.sub(r"#E\-[\w]*(抱拳|傲慢|得意|蛋糕|呕吐|闭嘴|礼物|yaoping|柠檬|流泪|怒火|撇嘴|太阳|咒骂|糗|猪猪|足球|磕头|大兵|电话|灯泡|飞鸟|奋斗|高兴|击打|饥饿|咖啡|口罩|骷髅|可乐|疯狂|白眼|阴险|叹气|奸笑|发呆|害羞|飞吻|怒火|悲伤|胜利|生病|弱|可怜|咖啡|酷酷|眩晕|流泪|发抖|难过|右哼哼|惊恐|悲伤|犯困|愤怒|凋谢|哈欠|拥抱|抓狂|鄙视|时间|啤酒|勾引|左哼哼|月亮|偷笑|震惊|惊讶|跳跳|瞌睡|可爱|衰样|好|憨笑|水果|色色|黑线|微笑|流汗|握手|心碎|问号|大哭|亲亲|抠鼻|拜拜|鬼脸|香吻|米饭|花朵|尴尬|擦汗|安慰|委屈|调皮|爱心|我一定尽力为您解答的哦|很棒|鼓掌)+",
        "α", sentence)
print(ret)


# 但如果：
# 1.ctrl+d re.sub这一行，不会报错
# 2.把上面的复制到下面，且把上面的注释了，也不会报错

"""
综上所述：还是在第一行加上"#coding:utf-8"为妙，否则会出现不可预测的异常
"""


