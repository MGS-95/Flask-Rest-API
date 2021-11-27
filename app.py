from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine, text, MetaData, Table
import logging
import os
from dotenv import load_dotenv
import service

load_dotenv(verbose=True)

app = Flask(__name__)   # Flask 앱 생성 (__name__ 값에 app 이름을 지정. 기본값은 app)
api = Api(app)          # API 서버로 사용할 수 있게 해줌.

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
                return service.json_to_dict_board(result)
            result = connection.execute(text(f"{os.getenv('SELECT_NUM')}{channel_num}"))
            print(f"[{ip}] ユーザーが一つ情報をリクエストしました。")
            return service.json_to_dict_board(result)

api.add_resource(BoardController, '/list/<channel_num>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
