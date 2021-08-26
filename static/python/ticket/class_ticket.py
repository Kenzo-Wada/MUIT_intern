# チケットを表すクラス
class Ticket():
    def __init__(self, ticketId, userId, name, valid):
        self.ticketId = ticketId # チケットID（識別番号）
        self.userId = userId # ユーザID（識別番号）
        self.name = name # ライブ名
        self.valid = valid # 有効か否か

    # チケットID（識別番号）を返すメソッド
    def get_id(self):
        return self.ticketId

    # ユーザID（識別番号）を返すメソッド
    def get_id(self):
        return self.userId

    # ライブ名を返すメソッド
    def get_name(self):
        return self.name

    # 有効か否かを返すメソッド
    def get_point(self):
        return self.valid