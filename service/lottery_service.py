import random
from service.user_service import get_tickets_by_userId

def get_tickets_by_flag(tickets):
    """所有者がいるチケットを取得する

    Args:
        tickets ([type]): [description]
    """
    owned_tickets = []
    for ticket in tickets:
        if ticket.flag == 1:
            owned_tickets.append()
    return owned_tickets

#抽選をする
def lottery_ticket(tickets):
    owned_tickets = get_tickets_by_flag(tickets)
    for ticket in owned_tickets:
        result = random.randint(0,1)
        ticket.set_valid(result)

#抽選結果を表示する
def view_lottery(user, tickets):
    tickets = get_tickets_by_userId(user, tickets)
    for ticket in tickets:
        if ticket.valid == 0:
            return ticket.id, False
        if ticket.valid == 1:
            return ticket.id, True


