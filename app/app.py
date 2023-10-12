"""
初期化処理
"""
from flask import Flask

# Flaskのインスタンスを生成
app = Flask(__name__)

# 設定ファイルを読み込む
app.config.from_pyfile('settings.py')

# SQLAlchemyのインスタンスを生成
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# SQLAlchemyオブジェクトにFlaskオブジェクトを登録する
db.init_app(app)

# Migrateオブジェクトを生成して
# FlaskオブジェクトとSQLAlchemyオブジェクトを登録する
from flask_migrate import Migrate
Migrate(app, db)

"""
トップページのルーティング
"""
from flask import render_template
import MySQLdb

@app.route("/")
def index():
    # DBに接続しカーソルを取得する
    connect = MySQLdb.connect(host='db', port=3306, user='user', passwd='password' , db='database', charset='utf8')
    cursor = connect.cursor()

    #レコードの挿入
    sql = "select * from posts"
    cursor.execute(sql) # 1つ目のレコードを挿入
    
    id, name = cursor.fetchone()
    cursor.close()
    connect.close()     # データベースオジェクトを閉じる



    # index.htmlをレンダリングして返す
    return render_template('index.html', id=id, name=name)

"""
ブループリントの登録
"""
# crudアプリのモジュールviews.pyからBlueprint「crud」をインポート
from app.crud.views import crud

# FlaskオブジェクトにBlueprint「crud」を登録
app.register_blueprint(crud)