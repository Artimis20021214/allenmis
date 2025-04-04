from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
    now = datetime.now()
    return render_template("about.html", datetime = str(now))
@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)


if __name__ == "__main__":
 app.run()
