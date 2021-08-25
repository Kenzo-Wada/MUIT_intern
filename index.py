from flask import Flask

app = Flask(__name__)

#menu画面
@app.route('/')
def menu():
    return 'menu'

#live情報の一覧
@app.route('/live')
def live():
    return 'live'

#mypageでの閲覧
@app.route('/mypage')
def mypage():
    return 'mypage'\



if __name__ == "__main__":
    app.run(debug=True)