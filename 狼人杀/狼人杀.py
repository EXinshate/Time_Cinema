from random import choice
import card


# 狼人阵营
class Wolf:
    skill = '每晚和同伴一起刀杀一人'
    card = card.wolf_symbol

    def show_card(self):
        print('\n 你的身份卡是：\n')
        print(self.card)
        print("你的技能是：{} \n".format(self.skill))
# 人类阵营
class Human:
    skill = "无特殊技能！"

    def show_card(self):
        print("你的身份卡是： \n")
        print(self.card)
        print("你的技能是：{} \n".format(self.skill))


# 预言家是人类阵营
# 每晚可查验任意一名在座玩家的身份
class Prophet(Human):
    def __init__(self):
        self.card = card.prophet_symbol
        self.skill = "每晚可查验任意一名在座玩家的身份"



# 女巫是人类阵营
# 有一瓶毒药、一瓶解药
class Witch(Human):
    def __init__(self):
        self.card = card.witch_symbol
        self.skill = "有一瓶毒药、一瓶解药"


# 猎人是人类阵营
# 被投票出局或中刀身亡时，可开枪带走任意一名玩家
class Hunter(Human):
    def __init__(self):
        self.card = card.hunter_symbol
        self.skill = "被投票出局或中刀身亡时，可开枪带走任意一名玩家"


    # 村民是人类阵营
    # 没有特殊技能
class Villager(Human):
    def __init__(self):
        self.card = card.villager_symbol

# 狼人杀九人局标准配置：3 狼、3 村民、1 预言家、1 女巫、1 猎人
roles = [Wolf(), Wolf(), Wolf(),Villager(), Villager(),Villager(), Prophet(),Witch(),Hunter() ]
# 游戏开始时，你可从所有角色牌中抽取一张，作为自己的身份卡
players = choice(roles)
# 请调用 show_card() 方法，观察自己的角色卡
players.show_card()