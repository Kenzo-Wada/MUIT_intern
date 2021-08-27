from service.live_service import get_live_by_liveId
from service.ticket_service import calc_point

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
def can_buy_ticket(userId, liveId, users, lives):
    buyer = get_user_by_userId(userId, users)
    item = get_live_by_liveId(liveId, lives)
    print(buyer.point, item.charge)
    if buyer.point >= item.charge:
        return True
    else:
        return False