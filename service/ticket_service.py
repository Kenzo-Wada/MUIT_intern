
def get_tickets_by_liveId(liveId, tickets):
    """ライブIDが合致するチケットを取得する
    その際、チケットの所有者がいるかどうかは関係ない

    Args:
        liveId ([type]): [description]
        tickets ([type]): [description]
    """
    live_tickets = []
    for ticket in tickets:
        if ticket.liveId == liveId:
            live_tickets.append(ticket)
    return live_tickets

# 予約する
def reserve_ticket(live_r, user_r, tickets):
    """チケットを予約する
    liveIdが合致しているチケットのうち、所有者がいないものを予約ずみにする

    Args:
        live_r ([int]): [ライブのID]
        user_r ([int]): [ユーザのID]
        tickets ([list <Ticket>]): データベース内のすべてのチケット
    """
    
    live_tickets = get_tickets_by_liveId(live_r, tickets)
    print(live_tickets)
    for ticket in live_tickets:
        if ticket.flag == 0:
            ticket.set_userId(user_r)
            ticket.set_flag(1)
            ticket.flag = True
            break
    else:
        return False

    return True