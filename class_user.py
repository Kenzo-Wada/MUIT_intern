# ユーザを表すのクラス
class User():
    def __init__(self, id, name, point, history, reserve):
        self.id = id # ユーザID（識別番号）
        self.name = name # 名前
        self.point = point # ポイント
        self.history = history # チケット履歴
        self.reserve = reserve # 予約情報

    # ユーザID（識別番号）を返すメソッド
    def get_id(self):
        return self.id

    # 名前を返すメソッド
    def get_name(self):
        return self.name

    # ポイントを返すメソッド
    def get_point(self):
        return self.point
        
    # チケット履歴を返すメソッド
    def get_history(self):
        return self.history

    # 予約情報を返すメソッド
    def get_reserve(self):
        return self.reserve