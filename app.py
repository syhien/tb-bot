from flask import Flask, render_template, request
from taobao_util import taobao

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        result, link = taobao(keyword)
        return render_template("result.html", result=result, link=link)
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    keyword = request.form.get("keyword")
    result, link = taobao(keyword)
    return render_template("result.html", result=result, link=link)


if __name__ == "__main__":
    app.run(debug=True, host="::", port=80)
