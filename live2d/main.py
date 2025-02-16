# 使用 Flask 框架
from flask import render_template, request, Flask

from utils.get_txt import chat

app = Flask(__name__)


@app.route('/main')
def home():
    return render_template('index.html')


@app.route('/login')
def home2():
    return render_template('login.html')


@app.route("/api/chat", methods=["POST"])
def chat_get():
    return chat(request)


if __name__ == '__main__':
    app.run(debug=True)
