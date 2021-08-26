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
    print(request.form)

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
    print(live_db)
    return render_template('main.html',list_value = live_db)

# ライブ詳細ページ
@app.route('/detail/<int:id>')
def show_detail_page(id):
    print(id)
    return render_template('detail.html',live_id = id-1, list_value = live_db)

# 予約完了ページ
@app.route('/confirm_reservation/<int:liveId>', methods=['POST'])
def show_confirm_reservation_page(liveId):

    kind = request.form.get('kind') # 座席の種類
    num = request.form.get('num') # 人数
    print(kind, num)
    # TODO: チケット予約者の処理
    is_reserve = ticket_service.reserve_ticket(liveId, 0, ticket_db)  # 最初の人のみが取引する
    if is_reserve: # チケット予約できたとき
        return render_template('confirm_reservation.html')
    else: # 予約できなかったとき
        # TODO
        pass

# マイページ : プロフィール
@app.route('/mypage/profile')
def show_profile_page():
    return render_template('profile.html')

# マイページ : 申し込み一覧
@app.route('/mypage/reserve')
def show_reserve_page():
    user_tickets = user_service.get_tickets_by_userId(0, ticket_db)  # とりあえず最初の人の情報を扱う
    if len(user_tickets) == 0:
        is_zero = True
    else:
        is_zero = False
    user_lives = []
    for ticket in user_tickets:
        live = live_service.get_live_by_liveId(ticket.liveId, live_db)
        user_lives.append(live)
    return render_template('reserve.html', lives = user_lives, is_zero = is_zero)

# マイページ : お知らせ
@app.route('/mypage/news')
def show_news_page():
    return render_template('news.html')


if __name__ == "__main__":
    app.run(debug=True)