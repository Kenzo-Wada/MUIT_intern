import class_liveList
import class_live

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/main")
def main():
    liveList = class_liveList.LiveList()
    return render_template("mainpage.html",liveList_value = liveList)

if __name__ == "__main__":
    app.run(debug=True)

