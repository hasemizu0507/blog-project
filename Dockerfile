# FROM｜ベースイメージを指定
# pythonのバージョンは任意
# FROM python:3.10.11
FROM ubuntu:22.04

RUN apt update
RUN apt install -y python3.10
RUN apt install -y python3-pip

# WORKDIR｜作業ディレクトリ指定
WORKDIR /usr/src/app
# ENV｜環境変数設定
ENV FLASK_APP=app

# COPY｜File/Directoryコピー
COPY /app/requirements.txt ./

# RUN｜コマンド実行
RUN pip install --upgrade pip
RUN pip install --upgrade werkzeug
# RUN pip install six
RUN apt install -y pkg-config
RUN apt-get -y install gcc libmariadb-dev
# RUN apt-get -y install default-libmysqlclient-dev
RUN apt-get -y install libmysqlclient-dev
# RUN apt-get -y install python3-dev
RUN pip install --no-cache-dir -r requirements.txt