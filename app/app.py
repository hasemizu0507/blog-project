"""
初期化処理
"""
from flask import Flask

# Flaskのインスタンスを生成
app = Flask(__name__)

"""
トップページのルーティング
"""
from flask import render_template

@app.route("/")
def index():
    # index.htmlをレンダリングして返す
    return render_template('index.html')