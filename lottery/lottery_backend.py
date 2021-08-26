import class_ticket
import random

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
tickets[2].set_userId(1)
tickets[2].set_flag(1)

#抽選をする
for i in range(n_tickets):
    if tickets[i].flag == 1 :
        result = random.randint(0,1)
        tickets[i].set_valid(result)

#抽選結果（ポイント）を計算する
user_point = {} # keyをuserId,valueをポイントに設定
lottery_result = input("抽選結果（ポイント）を表示する場合はyを入力: ") # とりあえず標準入力で受け取る
if lottery_result == 'y':
    userId = input("検索するuserIdを⼊⼒して下さい: ")
    # 辞書に新規登録
    user_point[int(userId)] = 0
    for i in range (n_tickets):
        # チケットにユーザが紐づけられている場合
        if int(userId) == tickets[i].userId :
            # ポイントを加算
            if int(tickets[i].valid) == 0:
                user_point[int(userId)] += 1

    for key,val in user_point.items():
        print("user:"+ str(key) + ",point:" + str(val))
