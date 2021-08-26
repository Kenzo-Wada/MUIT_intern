
# userの持っているチケット一覧を表示
def get_tickets_by_userId(userId, tickets):
    query_userId = input("検索するuserIdを⼊⼒して下さい: ") # とりあえず標準入力で受け取る
    query_userId_split = query_userId.split()
    user_tickets = []
    for ticket in tickets:
        if ticket.userId == userId:
            user_tickets.append(ticket)
    return user_tickets