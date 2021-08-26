from entity.class_ticket import Ticket
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
@app.route('/confirm_reservation', methods=['POST'])
def show_confirm_reservation_page():

    kind = request.form.get('kind') # 座席の種類
    num = request.form.get('num') # 人数
    print(kind, num)
    # TODO: チケット購入者の処理

    return render_template('confirm_reservation.html')

# マイページ : プロフィール
@app.route('/mypage/profile')
def show_profile_page():
    return render_template('profile.html')

# マイページ : 申し込み一覧
@app.route('/mypage/reserve')
def show_reserve_page():
    return render_template('reserve.html')

# マイページ : お知らせ
@app.route('/mypage/news')
def show_news_page():
    return render_template('news.html')


if __name__ == "__main__":
    app.run(debug=True)