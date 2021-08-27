from entity.class_ticket import Ticket
from service import user_service, live_service, ticket_service
from os import truncate
from flask import Flask, render_template, redirect, request
from FakeDB import DB

app = Flask(__name__)

db = DB()
db.create_random_db(9)
user_db = db.user_db
live_db = db.live_db
ticket_db = db.ticket_db

# ログインページ
@app.route('/login')
def show_login_page():
    return render_template('login.html')

# ログイン情報チェック
@app.route('/check_login', methods=['POST'])
def check_login():

    email = request.form.get('email')
    passward = request.form.get('passward')

    if True:
        # TODO: とりあえず、みんなログインできる
        return redirect('/main')
    else:
        return redirect('/login')

# ライブ一覧ページ
@app.route('/main')
def show_main_page():
    #livelist = LiveList()
    #list = livelist.live_list

    return render_template('main.html',list_value = live_db)

# ライブ詳細ページ
@app.route('/detail/<int:id>')
def show_detail_page(id):

    return render_template('detail.html',live_id = id-1, list_value = live_db)

# 限定ライブ詳細ページ
@app.route('/detail/limit/<int:id>')
def show_detail_limit_page(id):
    print("liveId:", id)
    can_buy = user_service.can_buy_ticket(0, id, user_db, live_db, ticket_db)
    print(can_buy)
    return render_template('lim_detail.html',live_id = id-1, list_value = live_db, can_buy = can_buy)


# 予約完了ページ
@app.route('/confirm_reservation/<int:liveId>', methods=['POST'])
def show_confirm_reservation_page(liveId):

    kind = request.form.get('kind') # 座席の種類
    num = request.form.get('num') # 人数
    print(kind, num)
    # TODO: チケット予約者の処理
    is_reserve = ticket_service.reserve_ticket(liveId, 0, ticket_db)  # 最初の人のみが取引する
    if is_reserve: # チケット予約できたとき
        return render_template('confirm_reservation.html',live_id = liveId-1, list_value = live_db)
    else: # 予約できなかったとき
        # TODO
        pass

# 購入完了ページ
@app.route('/confirm_buy/<int:liveId>', methods=['POST'])
def show_confirm_buyt_page(liveId):

    is_buy = ticket_service.buy_ticket(0, liveId, live_db, ticket_db)
    if is_buy: # チケット予約できたとき
        # TODO: 時間がないので応急処置 このままだと、ユーザ全員が同じポイント数
        user_db[0].point = ticket_service.calc_point(ticket_db, live_db)
        return render_template('lim_conf.html',live_id = liveId-1, list_value = live_db)
    else: # 予約できなかったとき
        # TODO
        pass

# マイページ : プロフィール
@app.route('/mypage/profile')
def show_profile_page():
    user_tickets = ticket_service.get_tickets_by_userId(0, ticket_db)
    point = ticket_service.calc_point(user_tickets, live_db)
    return render_template('profile.html', point=point)

# マイページ : 申し込み一覧
@app.route('/mypage/reserve')
def show_reserve_page():
    user_tickets = user_service.get_tickets_by_userId(0, ticket_db)  # TODO: とりあえず最初の人の情報を扱う
    if len(user_tickets) == 0:
        is_zero = True
    else:
        is_zero = False
    user_lives = []
    for ticket in user_tickets:
        live = live_service.get_live_by_liveId(ticket.liveId, live_db)
        user_lives.append(live)
    ticket_live_set = []
    for idx, ticket in enumerate(user_tickets):
        ticket_live_set.append((ticket, user_lives[idx]))
    print(*ticket_live_set)
    return render_template('reserve.html', tickets_lives = ticket_live_set, is_zero = is_zero)

# マイページ : お知らせ
@app.route('/mypage/news')
def show_news_page():
    return render_template('news.html')

# 管理者画面
@app.route('/admin')
def show_admin_page():
    return render_template('admin.html', users=user_db, lives=live_db, tickets=ticket_db)

# 抽選
@app.route('/admin/lottery')
def lottery():
    ticket_service.lottery_tickets(ticket_db)
    # TODO: 時間がないので応急処置 このままだと、ユーザ全員が同じポイント数
    user_db[0].point = ticket_service.calc_point(ticket_db, live_db)
    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)