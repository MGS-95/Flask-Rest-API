import os
from dotenv import load_dotenv
load_dotenv(verbose=True)           # .env 파일 불러옴
user = os.getenv('MYSQL_USER')
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv('MYSQL_HOST')
port = os.getenv("MYSQL_PORT")
database = os.getenv("MYSQL_DB")

DB_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}?charset=utf8"