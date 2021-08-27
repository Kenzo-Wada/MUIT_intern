import random

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

def get_ticket_by_ticketId(ticketId, tickets):
    for ticket in tickets:
        if ticket.ticketId == ticketId:
            return ticket
    else:
        return False # 存在しない

def get_tickets_by_flag(flag, tickets):
    flag_tickets = []
    for ticket in tickets:
        if ticket.flag == flag:
            flag_tickets.append(ticket)
    return flag_tickets

def get_tickets_by_valid(valid, tickets):
    valid_tickets = []
    for ticket in tickets:
        if ticket.valid == valid:
            valid_tickets.append(ticket)
    return valid_tickets

def get_tickets_by_userId(userId, tickets):
    user_tickets = []
    for ticket in tickets:
        if ticket.userId == userId:
            user_tickets.append(ticket)
    return user_tickets

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
    for ticket in live_tickets:
        if ticket.flag == 0:
            ticket.set_userId(user_r)
            ticket.flag = 1
            break
    else:
        return False

    return True

# 購入する
def buy_ticket(ticketId, userId, tickets):
    """チケットを購入する
    本来であれば限定ライブに限った話ではないが、今回買えるのは限定ライブのみとする
    """
    
    selected_ticket = get_ticket_by_ticketId(ticketId, tickets)
    
    # TODO: このチケットのライブが、限定ライブであるかどうかの判定
    if selected_ticket.flag == 0: # まだ所有者がいない
        selected_ticket.flag = 1
        selected_ticket.userId = userId
        selected_ticket.valid = 3 # 購入済み
        return True
    else:
        return False


#抽選をする
def lottery_tickets(tickets):
    waiting_tickets = get_tickets_by_valid(2, tickets)
    for ticket in waiting_tickets:
        if ticket.flag == 1: # チケット状態が未定　かつ　所有者がいる
            if random.random() < 0.7: # 高い確率で外れる
                result = 0
            else:
                result = 1
            ticket.valid = result

# 抽選結果（ポイント）を計算する
def calc_point(tickets):
    """

    Args:
        tickets (List<Ticket>): 計算したいチケットのリスト
    Example:
        user_tickets = get_tickets_by_userId(0, tickets)
        point = calc_point(user_tickets)
    """
    point = 0
    for ticket in tickets:
        if ticket.valid == 0: # 落選していれば、加算
            # TODO: 落選は全て1ポイントの加算
            point += 1
    return point
