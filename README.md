# Flask-Rest-API
<hr>
Title: Flask-Rest-API

<br><br>

### Environment

<hr>

```
OS : GCP Ubuntu
DB : AWS RDS (MySQL 8.x)
Deployment : Docker
Language : Python3.9.6
Framework : Flask
```

### Requirement

<hr>

```
# File
test.log : 記録を残すため。ロギングレベルは「INFO」。ルートパッケージに生成。
.env : 様々な環境変数（主にデータベースの情報）やSQLコマンドを作成し、生成
```

<br>

### Docker command

<hr>

```
# Build (Create Docker Image)
sudo docker build -t demo-flask:latest .

# -t (or --tag) : イメージやタグの名前を設定します。

# Run Image
sudo docker run --name demo-flask -d -p 80:80 demo-flask

# -d : コンテナーをバックグラウンドで実行します。
# -p 80:80 : このオプションでホストの80ポートとコンテナーの80ポートをコネクトし、外部と連結します。

```

### Setup for Development (Not using docker)

<hr>

```
0. Create .env and test.log files
1. Set the .env file

ex) .env
    # MySQL Connect
    MYSQL_USER = <user>
    MYSQL_PASSWORD = <password>
    MYSQL_HOST = <url>
    MYSQL_PORT = <port>
    MYSQL_DB = <db>

    # SQL
    SELECT_ALL = SELECT * FROM <Table>
    SELECT_NUM = SELECT * FROM <Table> WHERE <num> = <num>

2. Connect http://localhost/list/all or http://<your-ip>/list/all
```
