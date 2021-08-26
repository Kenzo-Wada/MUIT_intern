# liveを表すのクラス
class Live():
    def __init__(self, id, name, charge, place, startTime, endTime, open, date, detail, premium):
        self.id = id # ライブID
        self.name = name # 名前
        self.charge = charge # 料金
        self.place = place # 場所
        self.startTime = startTime # 開演時間
        self.endTime = endTime # 終了時間
        self.open = open # 開場時間
        self.date = date # 日付
        self.detail = detail # 説明文
        self.premium = premium # 限定ライブかどうか

    # ライブID（識別番号）を返すメソッド
    def get_id(self):
        return self.id

    # 名前を返すメソッド
    def get_name(self):
        return self.name

    # 料金を返すメソッド
    def get_charge(self):
        return self.charge
        
    # 場所を返すメソッド
    def get_place(self):
        return self.place

    # 開演時間を返すメソッド
    def get_startTime(self):
        return self.startTime
    
    # 終了時間を返すメソッド
    def get_endTime(self):
        return self.endTime
    
    # 開場時間を返すメソッド
    def get_open(self):
        return self.open
    
    # 日付を返すメソッド
    def get_date(self):
        return self.date

    # 説明文を返すメソッド
    def get_detail(self):
        return self.detail
    
    def get_premium(self):
        return self.Premium
    
    def __str__(self):
        return "<Live>"+"id:"+str(self.id)