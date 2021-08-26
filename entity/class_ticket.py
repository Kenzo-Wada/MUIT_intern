# チケットを表すクラス
class Ticket():
    def __init__(self, ticketId, userId, liveId, valid, flag):
        self.ticketId = ticketId # チケットID（識別番号）
        self.userId = userId # ユーザID（識別番号）
        self.liveId = liveId # ライブID（識別番号）
        self.valid = valid # 抽選結果
        self.flag = flag # 予約済みか否か = 所有者が存在するか否か

    # チケットID（識別番号）を返すメソッド
    def get_ticketId(self):
        return self.ticketId

    # ユーザID（識別番号）を返すメソッド
    def get_userId(self):
        return self.userId

    # ライブ名を返すメソッド
    def get_liveId(self):
        return self.liveId

    # 抽選結果を返すメソッド
    def get_valid(self):
        return self.valid

    # 有効か否かを返すメソッド
    def get_flag(self):
        return self.flag

    # ユーザID（識別番号）を設定メソッド
    def set_userId(self, userId):
        self.userId = userId

    # ライブID（識別番号）を設定メソッド
    def set_liveId(self, liveId):
        self.liveId = liveId

    # flagを設定メソッド
    def set_flag(self, flag):
        self.flag = flag