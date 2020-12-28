import itchat
import sys

# 登陆微信，运行这句话会产生登陆二维码，扫描即可登陆
itchat.auto_login()
# 默认参数：enableCmdQR，为True则在登陆的时候使用命令行显示二维码；
# hotReload=True，为True则暂存登陆状态，退出程序后重新运行不需要再扫码
itchat.auto_login(enableCmdQR=True,hotReload=True)

# 给好友发送信息，但UserName并不是NickName，不能直接知道；
# 当不写toUserName时发送给自己
itchat.send('Hello,Star', toUserName="UserName")

# 发送文字之外的消息：分别对应有各自的方法；且msg格式为：@fil@文件路径//@img@图片路径//@vid@视频路径
itchat.send_file(xxx)


# 获取所有好友信息，返回列表；列表中每个用户为一个字典
itchat.get_friends(update=True)[0:]

# 获取单个好友的信息，返回包含一个元素的列表，这个元素包含了此好友的信息
user = itchat.search_friends(name=u'Justaman')
# 根据此列表，拿到UserName；UserName每次都不一样，所以send中必须写username而不能从user中复制写死
username = user[0]['UserName']


# 好友给自己发送消息后，回复好友
from itchat.content import *
@itchat.msg_register(TEXT)
def reply(msg):
    itchat.send("收到的信息为%s" % msg["Text"],toUserName=msg["FromUserName"])
    return "T reveived: %s" % msg["Text"]

# 退出及登陆完成后调用特定方法,lc/ec分别为登录后的操作和退出登录时的操作
itchat.auto_login(loginCallback=login_behavior, exitCallback=exit_behavior)
itchat.logout()

# 获取好友头像，返回图片对象
itchat.get_head_img(userName="UserName")

# 不写这句只显示添加到通讯录的群聊
# 另外在微信-群聊-开启成员昵称，才会获取到成员信息，否则只会有群信息
itchat.dump_login_status()

# 获取群总信息，返回列表→字典；每个群聊对应的字典中又包括：成员列表→字典/群信息的字典元素
# 每一个群是一个字典，MemberList：列表，列表中是个成员信息的字典
# 群信息:UserName.../self/为字典的元素
room_list = itchat.get_chatrooms()

# 搜索指定群聊，返回群聊列表，获得此群聊成员信息
itchat.search_chatrooms(chatroom_name)


# 群聊在首次获取中不会获取群聊的用户列表，需要这一句才能获取群聊的成员，返回群聊成员信息列表
# 不过可以不退出登录执行多次也可以获取到成员信息
itchat.update_chatroom('bcdefg67')

# 群本身作为一个成员，UserName最开始有两个@，即@@







