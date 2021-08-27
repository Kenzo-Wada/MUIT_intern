# ユーザを表すクラス
class User():
    def __init__(self, id, name, point, history):
        self.id = id # ユーザID（識別番号）
        self.name = name # 名前
        self.point = point # ポイント
        self.history = history # チケット履歴

    # ユーザID（識別番号）を返すメソッド
    def get_id(self):
        return self.id

    # 名前を返すメソッド
    def get_name(self):
        return self.name

    # ポイントを返すメソッド
    def get_point(self):
        return self.point
        
    # チケット履歴(ticket list)を返すメソッド
    def get_history(self):
        return self.history

    # ポイントを減らし、新たにセットするメソッド
    # ０未満の場合はFalseを返す
    def decrease_point(self, point):
        new_point = self.point - point
        if new_point < 0:
            return False
        else:
            self.point = new_point

    # ポイントを増やし、新たにセットするメソッド
    def increase_point(self, point):
        self.point = self.point + point