from flask import Flask, render_template, redirect

app = Flask(__name__)

# ログインページ
@app.route('/login')
def show_login_page():
    return render_template('login.html')

# ログイン情報チェック
@app.route('/check_login')
def check_login():
    # TODO: とりあえず、みんなログインできる
    return redirect('/main')

# ライブ一覧ページ
@app.route('/main')
def show_main_page():
    return render_template('main.html')

# ライブ詳細ページ
@app.route('/detail')
def show_detail_page():
    return render_template('detail.html')

# 予約完了ページ
@app.route('/confirm_reservation')
def show_confirm_reservation_page():
    return render_template('confirm_reservation.html')

# マイページ
# 予約完了ページ
@app.route('/mypage')
def show_mypage():
    return render_template('mypage.html')

if __name__ == "__main__":
    app.run(debug=True)