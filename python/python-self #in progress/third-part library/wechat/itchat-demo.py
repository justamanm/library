import itchat


itchat.auto_login(enableCmdQR=False,hotReload=True)

# 获取所有好友的头像
# num = 0
# friends = itchat.get_friends(update=True)[0:]
# for i in range(len(friends)):
#     head_img = itchat.get_head_img(userName=friends[i]["UserName"])
#     print(type(head_img))
    # with open("res/%d-%s-head_img.jpg" % (num,friends[i]["NickName"]),"wb") as img:
    #     img.write(head_img)
    # num += 1

# users = itchat.search_friends(name=u'~')
# userName = users[0]['UserName']
# itchat.send_image("res/1.jpg", toUserName=userName)
# itchat.send('Hello,Star', toUserName=userName)

# get_chatrooms()返回群聊的列表；[{"memberlist":[{},{},{}],"":xx，"":xx},{"memberlist":[{},{},{}],"":xx，"":xx}...]
# itchat.search_chatrooms()，返回{"memberlist":[{},{},{}],"":xx，"":xx}
# 群信息:UserName.../self/为字典的元素

itchat.dump_login_status()
itchat.update_chatroom('')
room_list = itchat.get_chatrooms()
# print(room_list)chatroomUserName=
chat_room = itchat.search_chatrooms("")
# print(chat_room)
member_list = chat_room[0]["MemberList"]
print(member_list)
i = 1
for user_dict in member_list:
    chat_room_imgs = itchat.get_head_img(user_dict["UserName"],)
    print(user_dict["NickName"])
    print(type(chat_room_imgs))
#     chat_room_img=str(chat_room_img).encode()
#     with open("res/%s.jpg" % user_dict["NickName"], "wb") as img:
#         img.write(chat_room_img)
#     i += 1

# itchat.logout()



# 回复消息
# from itchat.content import *
# @itchat.msg_register(TEXT)
# def reply(msg):
#     itchat.send("收到的信息为%s" % msg["Text"],toUserName=msg["FromUserName"])
#     return "T reveived: 再来啊"
#
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text
# itchat.run()

# 退出及登陆完成后会调用的特定方法
#import time
# def lc():
#     print('finish login')
# def ec():
    # print('exit')

# 登录后的操作和退出登录时的操作
# itchat.auto_login(loginCallback=lc, exitCallback=ec,hotReload=True)
# time.sleep(3)
# itchat.logout()
# 若不设置loginCallback的值，则将会自动删除二维码图片并清空命令行显示。

