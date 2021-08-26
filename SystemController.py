from os import truncate
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

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
    return render_template('main.html')

# ライブ詳細ページ
@app.route('/detail')
def show_detail_page():
    return render_template('detail.html')

# 予約完了ページ
@app.route('/confirm_reservation', methods=['POST'])
def show_confirm_reservation_page():

    kind = request.form.get('kind') # 座席の種類
    num = request.form.get('num') # 人数
    print(kind, num)
    # TODO: チケット購入者の処理

    return render_template('confirm_reservation.html')

# マイページ
# 予約完了ページ
@app.route('/mypage')
def show_mypage():
    return render_template('mypage.html')

if __name__ == "__main__":
    app.run(debug=True)