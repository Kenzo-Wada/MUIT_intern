from service.live_service import get_live_by_liveId
from service.ticket_service import get_tickets_by_liveId, get_tickets_by_flag

def get_user_by_userId(userId, users):
    for user in users:
        if user.id == userId:
            return user

# userの持っているチケット一覧を表示
def get_tickets_by_userId(userId, tickets):
    user_tickets = []
    for ticket in tickets:
        if ticket.userId == userId:
            user_tickets.append(ticket)
    return user_tickets

# ユーザがそのチケットを買うことができるか
def can_buy_ticket(userId, liveId, users, lives, tickets):
    buyer = get_user_by_userId(userId, users)
    live = get_live_by_liveId(liveId, lives)
    live_tickets = get_tickets_by_liveId(liveId, tickets) # 求めているライブのチケット
    print("ライブのチケット数", len(live_tickets))
    valid_live_tickets = get_tickets_by_flag(0, live_tickets) # そのうち空きのあるもの
    print("残りチケット数", len(valid_live_tickets))
    print("ポイント", buyer.point)
    print("コスト", live.charge)
    if len(valid_live_tickets) == 0:
        return False
    else:
        if buyer.point >= live.charge:
            return True
        else:
            return False