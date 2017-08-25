import random
import os
import sys

def _d4():
    return random.randint(1,4)

def _d6():
    return random.randint(1,6)

def _d8():
    return random.randint(1,8)

def _3d6():
    return _d6()+_d6()+_d6()

def _d100():
    return random.randint(1,100)

class Character:
    def __init__(self, race):
        self.race=race
        self._str=_3d6()
        self._int=_3d6()
        self._wis=_3d6()
        self._dex=_3d6()
        self._con=_3d6()
        self._cha=_3d6()
        if (self._str==18):
            self.is_ex_str=1
            self.ex_str=random.randint(1,100)
            self.ex_str_str="/"+str(self.ex_str)
        else:
            self.ex_str_str=""
        if (self._str<=4):
            self.melee_hit=-2
            self.melee_dmg=-1
            self.carrying=-100
            self.doorbreak=1
        elif(self._str<=6):
            self.melee_hit=-1
            self.melee_dmg=0
            self.carrying=-50
            self.doorbreak=1
        elif(self._str<=9):
            self.melee_hit=0
            self.melee_dmg=0
            self.carrying=0
            self.doorbreak=2
        elif(self._str<=12):
            self.melee_hit=-0
            self.melee_dmg=0
            self.carrying=50
            self.doorbreak=2
        elif(self._str<=15):
            self.melee_hit=1
            self.melee_dmg=0
            self.carrying=100
            self.doorbreak=2
        elif(self._str==16):
            self.melee_hit=1
            self.melee_dmg=1
            self.carrying=150
            self.doorbreak=3
        elif(self._str==17):
            self.melee_hit=2
            self.melee_dmg=2
            self.carrying=300
            self.doorbreak=4
        elif(self.ex_str<=50):
            self.melee_hit=2
            self.melee_dmg=3
            self.carrying=500
            self.doorbreak=5
        elif(self.ex_str<=75):
            self.melee_hit=3
            self.melee_dmg=3
            self.carrying=600
            self.doorbreak=5
        elif(self.ex_str<=90):
            self.melee_hit=3
            self.melee_dmg=4
            self.carrying=700
            self.doorbreak=6
        elif(self.ex_str<=99):
            self.melee_hit=3
            self.melee_dmg=5
            self.carrying=900
            self.doorbreak=7
        elif(self.ex_str==100):
            self.melee_hit=4
            self.melee_dmg=6
            self.carrying=1200
            self.doorbreak=8

        if (self.doorbreak<=5):
            self.doorbreak_str="1~"+str(self.doorbreak)
        else:
            self.doorbreak_str="1~6(1~"+str(self.doorbreak-5)+")"

        if (self._int<=4):
            self.spellchance=0.2
            self.spellmin=2
            self.spellmax=3
            self.bonuslang=0
        elif(self._int<=7):
            self.spellchance=0.3
            self.spellmin=2
            self.spellmax=4
            self.bonuslang=0
        elif(self._int<=9):
            self.spellchance=0.4
            self.spellmin=3
            self.spellmax=5
            self.bonuslang=0
        elif(self._int<=12):
            self.spellchance=0.5
            self.spellmin=4
            self.spellmax=6
            self.bonuslang=self._int-10
        elif(self._int<=14):
            self.spellchance=0.65
            self.spellmin=5
            self.spellmax=8
            self.bonuslang=self._int-10
        elif(self._int<=16):
            self.spellchance=0.75
            self.spellmin=6
            self.spellmax=10
            self.bonuslang=self._int-10
        elif(self._int==17):
            self.spellchance=0.85
            self.spellmin=7
            self.spellmax=11
            self.bonuslang=self._int-10
        elif(self._int==18):
            self.spellchance=0.95
            self.spellmin=8
            self.spellmax=11
            self.bonuslang=self._int-10
        
        if (self._dex>=13):
            self.rangebonus=1
        elif(self._dex<=8):
            self.rangebonus=-1
        else:
            self.rangebonus=0
        if (self._dex>=15):
            self.dodge=self._dex-14
        else:
            self.dodge=0
        
        if (self._con>=15):
            self.hpbonus=1
        elif(self._con<=6):
            self.hpbonus=-1
        else:
            self.hpbonus=0

        if (self._cha<=4):
            self.maxnpc=1
            self.loyalty=-2
        elif(self._cha<=6):
            self.maxnpc=2
            self.loyalty=-1
        elif(self._cha<=9):
            self.maxnpc=3
            self.loyalty=0
        elif(self._cha<=12):
            self.maxnpc=4
            self.loyalty=0
        elif(self._cha<=15):
            self.maxnpc=5
            self.loyalty=1
        elif(self._cha<=17):
            self.maxnpc=6
            self.loyalty=2
        else:
            self.maxnpc=12
            self.loyalty=3
        
        self.getPrime()
        if (self.prime>=15):
            self.xpbonus=0.1
        elif (self.prime>=13):
            self.xpbonus=0.05
        elif (self.prime>=9):
            self.xpbonus=0
        elif(self.prime>=7):
            self.xpbonus=-0.1
        else:
            self.xpbonus=-0.2

        if (self.dndclass=="戰士"):
            self.hp=_d8()+self.hpbonus
        elif (self.dndclass=="盜賊"):
            self.hp=_d4()+self.hpbonus
            self.openlock=0.15
            self.trap=0.1
            self.pickpocket=0.2
            self.sneak=0.1
            self.hide=0.1
            self.listen=2
            if (self.race=="矮人"):
                self.openlock+=0.05
                self.trap+=0.15
                self.sneak+=0.05
                self.hide+=0.05
            elif (self.race=="精靈"):
                self.pickpocket+=0.05
                self.sneak+=0.1
                self.hide+=0.15
            elif (self.race=="哈比人"):
                self.openlock+=0.1
                self.trap+=0.05
                self.sneak+=0.05
                self.pickpocket+=0.05
                self.hide+=0.1
                self.listen+=1
                self.rangebonus+=1
        elif (self.dndclass=="牧師"):
            self.hp=_d6()+self.hpbonus
        elif (self.dndclass=="魔法使用者"):
            self.hp=_d4()+self.hpbonus

        self.startgold=_3d6()*10
        self.lowcap=750+self.carrying
        self.midcap=1000+self.carrying
        self.highcap=1500+self.carrying
        self.maxcap=3000+self.carrying

        self.genItems()

        self.melee_thac0=17+self.melee_hit
        self.range_thac0=17+self.rangebonus

        if (self.dndclass=="戰士"):
            self.save=[12,13,14,15,16]
        elif(self.dndclass=="魔法使用者"):
            self.save=[13,14,13,16,15]
        elif(self.dndclass=="牧師"):
            self.save=[11,12,14,16,15]
        elif(self.dndclass=="盜賊"):
            self.save=[13,14,13,16,15]

    def attbPrint(self):
        print(str(self._str)+self.ex_str_str,self._int,self._wis,self._dex,self._con,self._cha)

    def genDivineSpell(self):
        divine = 1
        return divine

    def genArcaneSpell(self):
        arcane = 1
        return arcane

    def genItems(self):
        melee_weapon_list= ['匕首　　　　　　　傷害　１Ｄ４　　價格　　３ＧＰ　　重量　２０ＧＰ',
        '硬頭鎚　　　　　　傷害　１Ｄ６　　價格　４０ＧＰ　　重量　５０ＧＰ',
        '戰斧　　　　　　　傷害　１Ｄ８　　價格　　７ＧＰ　　重量１００ＧＰ',
        '晨星鎚　　　　　　傷害　１Ｄ８　　價格　４０ＧＰ　　重量１００ＧＰ',
        '長矛　　　　　　　傷害　１Ｄ８　　價格　　５ＧＰ　　重量１５０ＧＰ',
        '長砍刀　　　　　　傷害　１Ｄ８　　價格　　７ＧＰ　　重量１５０ＧＰ',
        '連枷　　　　　　　傷害　１Ｄ８　　價格　　８ＧＰ　　重量１００ＧＰ',
        '斧槍　　　　　　　傷害１Ｄ１０　　價格　　７ＧＰ　　重量１５０ＧＰ',
        '手斧　　　　　　　傷害　１Ｄ６　　價格　　３ＧＰ　　重量　５０ＧＰ',
        '長槍　　　　　　　傷害　１Ｄ８　　價格　　４ＧＰ　　重量１５０ＧＰ',
        '長劍　　　　　　　傷害　１Ｄ８　　價格　１０ＧＰ　　重量　５０ＧＰ',
        '短劍　　　　　　　傷害　１Ｄ６　　價格　　８ＧＰ　　重量　２５ＧＰ',
        '雙手巨劍　　　　　傷害１Ｄ１０　　價格　１５ＧＰ　　重量１５０ＧＰ',
        '戰鎚　　　　　　　傷害　１Ｄ８　　價格　　７ＧＰ　　重量１００ＧＰ',
        '細劍　　　　　　　傷害　１Ｄ６　　價格　１０ＧＰ　　重量　２５ＧＰ',
        '彎刀　　　　　　　傷害　１Ｄ６　　價格　　７ＧＰ　　重量　５０ＧＰ',
        '短矛　　　　　　　傷害　１Ｄ６　　價格　　２ＧＰ　　重量１５０ＧＰ',
        '木棍　　　　　　　傷害　１Ｄ６　　價格　４０ＧＰ　　重量　５０ＧＰ',
        '赤手空拳　　　　　傷害　１　　　　價格　　０ＧＰ　　重量　　０ＧＰ',
        '＋１祖傳寶劍　　　傷害１Ｄ８　　價格　－－－　　重量　５０ＧＰ',]
        range_weapon_list= ['投石索（２０）　　傷害　１Ｄ４　　價格　　１ＧＰ　　重量　２０ＧＰ',
        '長弓（２０）　　　傷害　１Ｄ６　　價格　４０ＧＰ　　重量　５０ＧＰ',
        '短弓（２０）　　　傷害　１Ｄ６　　價格　２５ＧＰ　　重量　５０ＧＰ',
        '輕型十字弓（２０）傷害　１Ｄ６　　價格　１５ＧＰ　　重量　５０ＧＰ',
        '重型十字弓（２０）傷害　１Ｄ８　　價格　２５ＧＰ　　重量　７５ＧＰ',
        '複合弓（２０）　　傷害　１Ｄ６　　價格　５０ＧＰ　　重量　５０ＧＰ',
        '標槍（３）　　　　傷害　１Ｄ６　　價格　　２ＧＰ　　重量１００ＧＰ',
        '匕首（５）　　　　傷害　１Ｄ４　　價格　　３ＧＰ　　重量　２０ＧＰ',
        '飛斧（３）　　　　傷害　１Ｄ６　　價格　　３ＧＰ　　重量　５０ＧＰ',
        '熾火膠（３）　　　傷害　２Ｄ６　　價格　　－－－　　重量　２０ＧＰ',]
        armor_list= ['沒有盔甲　　　　　　ＡＣ　９　　　價格　　－－－　重量　　－－－',
        '皮甲　　　　　　　ＡＣ　　７　　　價格　１５ＧＰ　重量２５０ＧＰ',
        '鍊甲　　　　　　　ＡＣ　　５　　　價格　３０ＧＰ　重量５００ＧＰ',
        '板甲　　　　　　　ＡＣ　　３　　　價格　５０ＧＰ　重量７５０ＧＰ']
        shield_list= ['沒有盾牌　　　　　ＡＣ　－－　　　價格　　－－－　重量　　－－－',
        '木盾　　　　　　　ＡＣ　－１　　　價格　２５ＧＰ　重量１００ＧＰ',
        '鋼盾　　　　　　　ＡＣ　－１　　　價格　５０ＧＰ　重量１５０ＧＰ']
        item_list= ['油燈　　　　　　　價格　１０ＧＰ',
        '小瓶燈油　　　　　價格　　２ＧＰ',
        '油燈　　　　　　　價格　１０ＧＰ',
        '聖水　　　　　　　價格　２５ＧＰ',
        '軍用口糧（七天）　價格　１５ＧＰ',
        '一般口糧（七天）　價格　　５ＧＰ',
        '鐵釘（一打）　　　價格　　１ＧＰ',
        '皮製背包　　　　　價格　　５ＧＰ',
        '大麻袋　　　　　　價格　　２ＧＰ',
        '十呎長竿　　　　　價格　　１ＧＰ',
        '麻繩（５０呎）　　價格　　１ＧＰ',
        '大蒜　　　　　　　價格　１０ＧＰ',
        '顛茄　　　　　　　價格　１０ＧＰ',
        '木製十字架　　　　價格　　２ＧＰ',
        '銀製十字架　　　　價格　２５ＧＰ',
        '銀鏡　　　　　　　價格　１５ＧＰ',
        '小麻袋　　　　　　價格　　１ＧＰ',
        '火把（６支）　　　價格　　１ＧＰ',
        '酒（１袋）　　　　價格　　１ＧＰ',
        '水袋　　　　　　　價格　　１ＧＰ',
        '木樁（３根）　　　價格　　１ＧＰ',
        '鐵鎚　　　　　　　價格　　２ＧＰ',
        '附子草　　　　　　價格　１０ＧＰ',
        '鐵製撬棍　　　　　價格　１０ＧＰ',
        '睡袋　　　　　　　價格　　３ＧＰ',
        '帳篷　　　　　　　價格　１０ＧＰ',
        '薰香　　　　　　　價格　　１ＧＰ',
        '骨製骰子　　　　　價格　　１ＧＰ',
        '卡牌遊戲組　　　　價格　　５ＧＰ',
        '地圖匣　　　　　　價格　１０ＧＰ',
        '墨水和筆　　　　　價格　２５ＧＰ',
        '羊皮紙（３張）　　價格　　１ＧＰ',
        '平底鍋　　　　　　價格　　５ＧＰ',
        '燧石和鐵片　　　　價格　　１ＧＰ',
        '釣魚竿　　　　　　價格　　２ＧＰ',
        '哈比人菸草　　　　價格　２５ＧＰ',
        '家族璽戒　　　　　價格　５０ＧＰ',
        '捕獵陷阱　　　　　價格　　２ＧＰ',
        '手杖　　　　　　　價格　　１ＧＰ',
        '秘銀平底鍋　　　　價格　　－－－',
        ]
        arcane_spell_list= ['魅惑人類　　持續到解除　　距離１２０呎　　\n只對人形生物有效，目標單體，對方魔法豁免失敗時落入施法者的控制當中直到魔法被解除。依據受術者智力每隔一段時間可以重新豁免\n',
        '偵測魔法　持續２回合　　　距離　６０呎　　\n辨知範圍60呎內的人、事、物上是否有魔法作用。\n',
        '封門術　　持續２Ｄ６回合　距離　３０呎　　\n在持續時間內將門封上。解除魔法、強力的反魔法生物（如炎魔）、敲擊術可以立即結束法術效果。\n',
        '光亮術　　持續６＋１回合　距離　３０呎　　\n在施法位置發出較日光微弱的光亮照明。\n',
        '魔法飛彈　立即生效　　　　距離１５０呎　　\n射出魔法箭矢進行遠程射擊，傷害為1D6+1。每提昇5級可以一次多發射2發魔法飛彈。\n',
        '防護邪惡　持續６回合　　　距離　　自身　　\n魔法陣環繞施法者並保護施法者不會遭受魔法生物（如隱形潛伏怪、魔像）的攻擊，同時施法者在對抗邪惡生物時的豁免檢定+1，對方命中-1。此效果不與魔法盔甲或戒指疊加。\n',
        '通曉語言　持續片刻　　　　距離　　自身　　\n施法後可以解讀寶藏圖的方向等資訊，約可讀1-2個物品。\n',
        '閱讀魔法　持續片刻　　　　距離　　自身　　\n施法後可以解讀卷軸或魔法物品，約可讀1-2個物品。\n',
        '護盾術　　持續２回合　　　距離　　自身　　\n施法者和敵人之間升起自動防衛的魔法障璧，使施法者在持續時間內對遠程AC為2，對其他攻擊AC為4。\n',
        '睡眠術　　持續６回合　　　距離２４０呎　　\n範圍內2d8個1級生物、2d6個2級生物、1d6個3級生物和1d6個4級生物陷入睡眠（無豁免）。若範圍內生物數量超過擲骰結果，REF會隨機決定誰睡著。此法術對不死生物無效。\n',
        '腹語術　　持續２回合　　　距離　６０呎　　\n持續時間內施法者可以讓自己說話的聲音從60呎內任意位置發出。\n',]

        divine_spell_list= ['治療輕傷　　立即生效　　　\n治癒目標1D6+1傷害。\n',
        '偵測魔法　持續２回合　　　距離　６０呎　　\n辨知範圍60呎內的人、事、物上是否有魔法作用。\n',
        '偵測邪惡　持續６回合　　　距離１２０呎　　\n偵測範圍內生物的邪惡想法或念頭以及邪惡魔法物品。\n',
        '光亮術　　持續１２回合　　距離　３０呎　　\n在施法位置發出較日光微弱的光亮照明。\n',
        '防護邪惡　持續１２回合　　距離　　自身　　\n魔法陣環繞施法者並保護施法者不會遭受魔法生物（如隱形潛伏怪、魔像）的攻擊，同時施法者在對抗邪惡生物時的豁免檢定+1，對方命中-1。此效果不與魔法盔甲或戒指疊加。\n',
        '淨化飲食　立即生效　　　　距離　　觸碰　　\n淨化12人份的飲食，消除腐壞或毒素。\n',]

        if (self.dndclass=="魔法使用者"):
            self.primaryweapon="匕首　　　　　　　傷害１Ｄ４　　價格３ＧＰ　　　重量２０ＧＰ"
            self.secondaryweapon=""
            ar=0
            sh=0
            self.armor=armor_list[ar]
            self.shield=shield_list[sh]
        elif(self.dndclass=="牧師"):
            self.primaryweapon="硬頭鎚　　　　　　傷害１Ｄ６　　價格４０ＧＰ　　重量５０ＧＰ"
            self.secondaryweapon="投石索　　　　　　傷害１Ｄ４　　價格１ＧＰ　　　重量２０ＧＰ"
            ar=random.randint(1,3)
            sh=random.randint(0,2)
            self.armor=armor_list[ar]
            self.shield=shield_list[sh]
        else:
            p=random.randint(0,19)
            if (p==19):
                if (random.randint(0,4)!=4):
                    p=random.randint(0,18)
            s=random.randint(0,9)
            if (s==9):
                if (random.randint(0,9)!=9):
                    s=random.randint(0,8)
            self.primaryweapon=melee_weapon_list[p]
            self.secondaryweapon=range_weapon_list[s]
            if (self.dndclass=="盜賊"):
                ar=random.randint(0,1)
                sh=random.randint(0,1)
                self.armor=armor_list[ar]
                self.shield=shield_list[sh]
            else:
                ar=random.randint(1,3)
                sh=random.randint(0,2)
                self.armor=armor_list[ar]
                self.shield=shield_list[sh]
        if (ar==0):
            base_ac=9
        elif (ar==1):
            base_ac=7
        elif (ar==2):
            base_ac=5
        elif (ar==3):
            base_ac=3
        if (sh==0):
            sh_ac=0
        elif (sh>=1):
            sh_ac=-1
        self.ac=base_ac+sh_ac-self.dodge
        self.startitem=random.randint(2,8)
        self.items=[]
        for x in range(0,self.startitem):
            self.items.append(item_list[random.randint(0,39)])
        self.ability=[]
        if (self.race=="精靈"):
            self.ability.append("60呎夜視能力")
            self.ability.append("對哥布林、獸人、化獸人、食人魔、巨人、炎魔有+1命中（未計算）")
            self.ability.append("通曉大哥布林語、豺狼人語、獸人語")
            self.ability.append("精靈作為盜賊時有種族加成（已計算）")
        elif (self.race=="矮人"):
            self.ability.append("60呎夜視能力")
            self.ability.append("矮人是唯一能夠使用+3魔法戰鎚的種族")
            self.ability.append("矮人在地底建築中可以發現窄道、陷阱、活動牆面及較新的建築")
            self.ability.append("矮人通曉地珠語、狗頭人語、哥布林語")
            self.ability.append("矮人作為盜賊時擁有種族加成（已計算）")
        elif (self.race=="哈比人"):
            self.ability.append("不能被復活術復活")
            self.ability.append("哈比人使用射擊武器有+1命中（已計算）")
            self.ability.append("哈比人作為盜賊時有種族加成（已計算）")
        if (self.dndclass=="盜賊"):
            self.ability.append("開鎖技能："+'{0:.0f}%'.format(self.openlock*100))
            self.ability.append("解除陷阱："+'{0:.0f}%'.format(self.trap*100))
            self.ability.append("扒竊技能："+'{0:.0f}%'.format(self.pickpocket*100))
            self.ability.append("潛行技能："+'{0:.0f}%'.format(self.sneak*100))
            self.ability.append("躲藏技能："+'{0:.0f}%'.format(self.hide*100))
            self.ability.append("聆聽技能："+"1~"+str(self.listen))
        elif (self.dndclass=="牧師"):
            self.ability.append("驅散：骷髏　７　　　殭屍　９　　食屍鬼　１１")

        if (self.dndclass=="魔法使用者"):
            self.spell_num=0
            self.startspell=0
            self.spells=[]
            spell_got=[0]*11
            while self.spell_num<self.spellmin and self.spell_num<self.spellmax:
                for x in range(0,11):
                    if spell_got[x]==1:
                        continue
                    if _d100()<=self.spellchance*100:
                        self.spells.append(arcane_spell_list[x])
                        spell_got[x]=1
                        self.spell_num+=1
                        if self.spell_num>=self.spellmax:
                            break
        if (self.dndclass=="牧師"):
            self.spells=[]
            for x in range(0,6):
                self.spells.append(divine_spell_list[x])

    def getPrime(self):
        if(self._wis>=self._str and self._wis>=self._int and self._wis>=self._dex) and self.race=="人類":
            self.primeattb="wis"
            self.prime=int(self._wis+self._str/3+self._int/2)
            self.dndclass="牧師"
        elif(self._int>=self._str and self._int>=self._dex and self._int>=self._wis) and (self.race=="人類" or self.race=="精靈"):
            self.primeattb="int"
            self.prime=int(self._int+self._wis/2)
            self.dndclass="魔法使用者"
        elif(self._dex>=self._str and self._dex>=self._int and self._dex>=self._wis):
            self.primeattb="dex"
            self.prime=int(self._dex)
            self.dndclass="盜賊"
        else:
            self.primeattb="str"
            self.prime=int(self._str+self._int/2+self._wis/3)
            self.dndclass="戰士"

    def charPrint(self):
        print("等級：1")
        print('種族：',self.race.ljust(10),"職業：",self.dndclass.ljust(10))
        print("==============================屬性==============================")
        print("力量：",(str(self._str)+self.ex_str_str).ljust(10),"　近戰命中/傷害/破門：",('{0:+d}'.format(self.melee_hit)+"/"+'{0:+d}'.format(self.melee_dmg)+"/"+self.doorbreak_str).ljust(10))
        print("智力：",str(self._int).ljust(10),"　額外語言數量：",str(self.bonuslang).ljust(10))
        print("睿智：",str(self._wis).ljust(10))
        print("敏捷：",str(self._dex).ljust(10),"　遠程命中/閃避加成：",('{0:+d}'.format(self.rangebonus)+"/"+('{0:+d}'.format(self.dodge))).ljust(10))
        print("體質：",str(self._con).ljust(10),"　生命值加成：",str(self.hpbonus).ljust(10))
        print("魅力：",str(self._cha).ljust(10),"　雇傭上限/忠誠度加成：",(str(self.maxnpc)+"/"+('{0:+d}'.format(self.loyalty))).ljust(10))
        print("=============================其他數值============================")
        print("生命值（HP）：",str(self.hp).ljust(2),"　輕度負重：", str(self.lowcap).ljust(10))
        print("盔甲等級（AC）：",str(self.ac).ljust(2),"中度負重：", str(self.midcap).ljust(10))
        print("THAC0：",(str(self.melee_thac0)+"/"+str(self.range_thac0)).ljust(9),"　重度負重：", str(self.highcap).ljust(10))
        print("經驗加成：",('{0:.0f}%'.format(self.xpbonus*100)).ljust(6),"　極限負重：", str(self.maxcap).ljust(10))
        print("毒素豁免：",str(self.save[0]).ljust(1),"射線豁免：",str(self.save[1]).ljust(1),"麻痺豁免：",str(self.save[2]).ljust(1),"龍息豁免：",str(self.save[3]).ljust(1),"法術豁免：",str(self.save[4]).ljust(1))
        print("==============================能力==============================")
        for x in self.ability:
            print(x)
        print("==============================裝備==============================")
        print("武器：",self.primaryweapon)
        if (self.dndclass!="魔法使用者"):
            print("武器：",self.secondaryweapon)
            print("盔甲：",self.armor)
            print("盾牌：",self.shield)
        print("==============================物品==============================")
        for x in range(0,self.startitem-1):
            print(self.items[x])
        if (self.dndclass=="魔法使用者"):
            print("==============================法術==============================")
            for x in range(0,self.spell_num):
                print(self.spells[x])
        elif (self.dndclass=="牧師"):
            print("==============================法術==============================")
            for x in range(0,6):
                print(self.spells[x])
        print("\n")

for i in range(0,100):
    #race = input("1：人類　　2：精靈 　　3：矮人　　4：哈比人　　輸入種族編號：")
    #os.system('clear')
    with open('char'+str(i)+'.txt','w') as f:
        sys.stdout = f
        race=random.randint(1,4)
        if race==1:
            char = Character("人類")
            char.charPrint()
        elif race==2:
            char = Character("精靈")
            char.charPrint()
        elif race==3:
            char = Character("矮人")
            char.charPrint()
        elif race==4:
            char = Character("哈比人")
            char.charPrint()



