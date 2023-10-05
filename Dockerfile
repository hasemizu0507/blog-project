# FROM｜ベースイメージを指定
# pythonのバージョンは任意
FROM python:3.10.11

# WORKDIR｜作業ディレクトリ指定
WORKDIR /usr/src/app
# ENV｜環境変数設定
ENV FLASK_APP=app

# COPY｜File/Directoryコピー
COPY /app/requirements.txt ./

# RUN｜コマンド実行
RUN pip install --upgrade pip
RUN pip install --upgrade werkzeug
RUN pip install --no-cache-dir -r requirements.txt