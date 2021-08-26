from entity import class_live
#ライブリストを表すクラス
class LiveList():
    # ライブリストの初期化
    live_list = []

    def __init__(self):
        # ライブの作成とリストへの追加
        live1 = class_live.Live(1, "Bunp of Chicken", "¥7,000", "横浜アリーナ(神奈川)", "17:00", "20:00", "15:30", "2021/9/20 (月)", None)
        self.live_list.append(live1)
        live2 = class_live.Live(2, "ONE OK ROCK", "¥5,000", "さいたまスーパーアリーナ(埼玉)", "13:00", "16:00", "12:00", "2021/9/26 (日)",  None)
        self.live_list.append(live2)
        live3 = class_live.Live(3, "RADWIMPS", "¥9,000", "東京ドーム(東京)", "13:00", "15:00", "11:30", "2021/9/18 (土)", None)
        self.live_list.append(live3)
        live4 = class_live.Live(4, "RADWIMPS", "¥9,000", "東京ドーム(東京)", "15:00", "17:00", "13:30", "2021/9/19 (日)", None)
        self.live_list.append(live4)
        live5 = class_live.Live(5, "King Gnu", "¥7,000", "東京ドーム(東京)", "13:00", "16:00", "11:30", "2021/9/26 (日)", None)
        self.live_list.append(live5)
    # ライブIDが一致するインスタンスを返すメソッド
    def search_live(self,key):
        for l in self.live_list:
            if l.get_id() == key:
                   #print(u.get_name())
                   return l