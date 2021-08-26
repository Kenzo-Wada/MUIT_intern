import class_ticket

# チケットを管理するリスト
tickets = []
# チケット数
n_tickets = 100

for i in range(n_tickets):
    # 仮のオブジェクトを⽣成し，リストに追加
    # (ticketId, userId, liveId, 抽選結果, flag)
    # 抽選結果, 0:落選, 1:当選, 2:未定
    tickets.append(class_ticket.Ticket(i, 0, 0, 2, 0))


# 内部で手動登録

tickets[0].set_liveId(1)
tickets[0].set_userId(1)
tickets[0].set_flag(1)

tickets[1].set_liveId(2)
tickets[1].set_userId(1)
tickets[1].set_flag(1)

tickets[2].set_liveId(2)
tickets[2].set_userId(3)
tickets[2].set_flag(1)


# 予約する
query_reserve = input("liveIdとuserIdを空白区切りで⼊⼒して下さい: ") # とりあえず標準入力で受け取る
query_reserve_split = query_reserve.split()
live_r = int(query_reserve_split[0])
user_r = int(query_reserve_split[1])
for i in range (n_tickets):
    if tickets[i].flag == 0:
        tickets[i].set_liveId(live_r)
        tickets[i].set_userId(user_r)
        tickets[i].set_flag(1)
        break

# userの持っているチケット一覧を表示
query_userId = input("検索するuserIdを⼊⼒して下さい: ") # とりあえず標準入力で受け取る
query_userId_split = query_userId.split()
for query in query_userId_split:
    for i in range (n_tickets):
        if tickets[i].userId == int(query):
            userId = tickets[i].userId
            ticketId = tickets[i].ticketId
            liveId = tickets[i].liveId
            print('user id: ' + str(userId) + ', ticket id: ' + str(ticketId) + ', live id: ' + str(liveId))
            continue
        