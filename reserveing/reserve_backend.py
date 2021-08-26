import class_ticket

# チケットを管理するリスト
tikets = []
# チケット数
n_tikets = 100

'''
# チケット情報の読み込み（本来ならDBから貰ってくる）
tiket1 = class_ticket.Ticket(1, 1, 1, 1, 1)
tiket2 = class_ticket.Ticket(2, 5, 1, 0, 1)
tiket3 = class_ticket.Ticket(3, 8, 1, 3, 1)
tiket4 = class_ticket.Ticket(4, 1, 2, 0, 1)


# チケットをリスト化
tikets.append(tiket1)
tikets.append(tiket2)
tikets.append(tiket3)
tikets.append(tiket4)


# userの持っているチケット一覧を表示
query_userId = input("userIdを⼊⼒して下さい: ") # とりあえず標準入力で受け取る
query_userId_split = query_userId.split()
for query in query_userId_split:
    for i in range (n_tikets):
        if tikets[i].userId == int(query):
            userId = tikets[i].userId
            ticketId = tikets[i].ticketId
            liveId = tikets[i].liveId
            print('user id: ' + str(userId) + ',ticket id: ' + str(ticketId) + ',live id: ' + str(liveId))
'''

for i in range(n_tikets):
    # 仮のオブジェクトを⽣成し，リストに追加
    tikets.append(class_ticket.Ticket(i, 0, 0, 3, 0))

query_reserve = input("liveIdとuserId⼊⼒して下さい: ") # とりあえず標準入力で受け取る
query_reserve_split = query_reserve.split()
live_r = int(query_reserve_split[0])
user_r = int(query_reserve_split[1])
for i in range (n_tikets):
    if tikets[i].flag == 0:
        tikets[i].set_liveId(live_r)
        tikets[i].set_userId(user_r)
        break



