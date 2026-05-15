import json

from flask import Flask, Response, render_template, request
from taobao_util import taobao, taobao_stream

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return search()
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    keyword = request.form.get("keyword")
    results, result, links = taobao(keyword)
    return render_template("result.html", results=results, result=result, link=links[0] if links else None, links=links)


@app.route("/search/stream", methods=["POST"])
def search_stream():
    keyword = request.form.get("keyword")

    def generate():
        for event in taobao_stream(keyword):
            event_type = event.get("type", "message")
            yield f"event: {event_type}\ndata: {json.dumps(event, ensure_ascii=False)}\n\n"

    return Response(generate(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True, host="::", port=80)
