from service.user_service import get_tickets_by_userId

#抽選結果（ポイント）を計算する
def calculate_point(user_r, tickets):
    user_tickets = get_tickets_by_userId(user_r, tickets)
    # keyをuserId,valueをポイントに設定
    user_point = {} 
    # 辞書に新規登録
    user_point[user_r] = 0
    for ticket in user_tickets:
        # ポイントを加算
        if ticket.valid == 0:
            user_point[user_r] += 1
    # pointの合計をreturn
    return user_point[user_r]
