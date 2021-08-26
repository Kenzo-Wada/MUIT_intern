import class_live

#ライブリストを表すクラス
class LiveList():
    # ライブリストの初期化
    live_list = []

    def __init__(self):
        # ライブの作成とリストへの追加
        live1 = class_live.Live(1, "Bunp of Chicken", 7000, "横浜アリーナ(神奈川)", "17:00", "20:00", "15:30", "2021/9/20 (月)", None)
        LiveList.live_list += [live1]
        live2 = class_live.Live(2, "ONE OK ROCK", 7000, "さいたまスーパーアリーナ(埼玉)", "13:00 - 16:00", None)
        LiveList.live_list += [live2]
        live3 = class_live.Live(3, "RADWIMPS", 9000, "東京ドーム(東京)", "13:00 - 15:00", None)
        LiveList.live_list += [live3]
    
    # ライブIDが一致するインスタンスを返すメソッド
    def search_live(self,key):
        for l in LiveList.live_list:
            if l.get_id() == key:
                   #print(u.get_name())
                   return l