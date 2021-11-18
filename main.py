from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from sqlalchemy import create_engine, text, MetaData, Table
import logging
import pandas as pd
import json
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

app = Flask(__name__)  # Flask 앱 생성
api = Api(app)  # API 서버로 사용할 수 있게 해줌.

app.config.from_pyfile('config.py')

engine = create_engine(app.config['DB_URL'], encoding="utf-8")
metadata = MetaData(bind=engine)

board = Table('channel', metadata, autoload=True)

logging.basicConfig(filename='test.log', level=logging.INFO, encoding='UTF-8')

class BoardController(Resource):

    def get(self, channel_num):
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        with engine.connect() as connection:
            if channel_num == "all":
                print(f"[{ip}] ユーザーが全体情報をリクエストしました。")
                result = connection.execute(text(os.getenv('SELECT_ALL')))
                return json_to_dict_board(result)
            result = connection.execute(text(os.getenv('SELECT_NUM')))
            print(f"[{ip}] ユーザーが一つ情報をリクエストしました。")
            return json_to_dict_board(result)

api.add_resource(BoardController, '/list/<channel_num>')


def json_to_dict_board(result):
    channel_num = []
    channel_name = []
    channel_url = []
    channel_id = []
    published_at = []
    birthday = []
    inactive = []
    debut = []
    for row in result:
        channel_num.append(row['channel_num'])
        channel_name.append(row['channel_name'])
        channel_url.append(row['channel_url'])
        channel_id.append(row['channel_id'])
        published_at.append(row['published_at'])
        birthday.append(row['birthday'])
        inactive.append(row['inactive'])
        debut.append(row['debut'])
    pd_data = {
        "channel_num": channel_num,
        "channel_name": channel_name,
        "channel_url": channel_url,
        "channel_id" : channel_id,
        "published_at": published_at,
        "birthday": birthday,
        "inactive": inactive,
        "debut": debut
    }
    pd_json = pd.DataFrame(pd_data).to_json(orient="records")
    return json.loads(pd_json)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
