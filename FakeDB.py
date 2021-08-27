from entity.class_user import User
from entity.class_live import Live
from entity.class_ticket import Ticket
import random

class DB():
    user_db = []
    live_db = []
    ticket_db = []

    artist_candidate = ["Bunp of Chicken", "RATWINPS", "ONE OK LOCK", "King Muu"]
    charge_candidate = [5000, 7000, 8000, 8500, 10000]
    point_candidate = [2, 3, 4]
    place_candidate = ["横浜アリーナ(神奈川)", "さいたまスーパーアリーナ(埼玉)", "東京ドーム(東京)"]
    time_candidate = [("13:00", "15:00", "11:30"), ("17:00", "20:00", "15:30"), ("13:00", "16:00", "12:00")]
    date_candidate = ["2021/9/18 (土)", "2021/9/19 (日)", "2021/9/20 (月)", "2021/9/26 (日)"]

    def __init__(self):
        user = User(0, "和田賢造", 0, [])
        self.user_db.append(user)

    def create_random_db(self, num):
        self.create_random_live_db(num)
        self.create_random_ticket_db(3)

    def create_random_live_db(self, num):
        for idx in range(num):
            artist = random.choice(self.artist_candidate)
            place = random.choice(self.place_candidate)
            time = random.choice(self.time_candidate)
            date = random.choice(self.date_candidate)
            detail = ""
            if random.random() < 0.3:  # 限定ライブである確率
                premium = 1
                plice = random.choice(self.point_candidate)
            else:
                premium = 0
                plice = random.choice(self.charge_candidate)

            live = Live(idx+1, artist, plice, place, *time, date, detail, premium)
            self.live_db.append(live)
    
    def create_random_ticket_db(self, num):
        """[summary]

        Args:
            num ([int]): 一つのライブに最大何枚のチケットを用意するか
        """
        ticket_id = 1
        for live in self.live_db:
            max_n_ticket = random.randint(1, num)
            for idx in range(max_n_ticket):
                ticket = Ticket(ticket_id, None, live.id, 2, 0)
                self.ticket_db.append(ticket)
                ticket_id += 1

    
if __name__ == "__main__":
    db = DB()
    db.create_random_db(10)
    print(db.user_db)
    for live in db.live_db:
        print(live)
    for ticket in db.ticket_db:
        print(ticket)