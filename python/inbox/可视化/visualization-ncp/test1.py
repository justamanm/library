card = str(input()).split("-")
card1_str = card[0]
card1 = card[0].split(" ")
card2_str = card[1]
card2 = card[1].split(" ")
flection_dict = {}

def get_flection_dict():
    for i in range(3, 11):
        flection_dict[str(i)] = i - 3
    flection_dict["J"] = 8
    flection_dict["Q"] = 9
    flection_dict["K"] = 10
    flection_dict["A"] = 11
    flection_dict["2"] = 12
    flection_dict["joker"] = 13
    flection_dict["JOKER"] = 13
    # print(flection_dict)

get_flection_dict()

def flection(card_list):
    new_card = []
    for card in card_list:
        new_card.append(flection_dict[card])
    # print(new_card)
    return new_card

new_card1 = flection(card1)
new_card2 = flection(card2)

def compare():
    """
    两种分类：1.长度一致/不一致，2.是否有炸弹/对王
    先按照第一种
    :return:
    """
    len1 = len(new_card1)
    len2 = len(new_card2)
    # 长度一致的情况
    if len1 == len2:
        # 长度为1/2/3/4/5的情况下，都只要比较第一个即可得出结论
        if new_card1[0] >= new_card2[0]:
            print(card1_str)
        else:
            print(card2_str)
    else:
        """长度不一致：
                包含炸弹/对王
                    只有一组牌包含，则包含的大
                    同时包含，则进行比大小(不会出现同为炸弹或同为对王的情况)
                都不包含炸弹/对王，返回ERROR
        """
        if len1 == 4 or len2 == 4 or new_card1[0] == 13 or new_card2[0] == 13:
            # 同时包含，比大小
            if (len1 == 4 or new_card1[0] == 13) and (len2 == 4 or new_card2[0] == 13):
                # 找出长度为2的既是炸弹，即为结果
                if len1 == 2:
                    print(card1_str)
                else:
                    print(card2_str)
            else:
                # 只有一组牌包含，则包含的即为结果
                if len1 == 4 or new_card1[0] in [13, 14]:
                    print(card1_str)
                if len2 == 4 or new_card2[0] in [13, 14]:
                    print(card2_str)
        else:
            print("ERROR")
            
compare()