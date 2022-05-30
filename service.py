import json
import pandas as pd
from ytlv import *
from concurrent.futures import ThreadPoolExecutor
from operator import itemgetter
import datetime

def json_to_dict_board(result):
    global lv, channel_num, channel_name, channel_url, channel_id, published_at, birthday, inactive, debut, embed_url, state
    lv = islive()
    channel_num = []
    channel_name = []
    channel_url = []
    channel_id = []
    published_at = []
    birthday = []
    inactive = []
    debut = []
    embed_url = []
    state = []
    with ThreadPoolExecutor(max_workers=30) as pool:
        for page in pool.map(fetch, result):
            page
    pd_data = {
        "channel_num": channel_num,
        "channel_name": channel_name,
        "channel_url": channel_url,
        "channel_id" : channel_id,
        "published_at": published_at,
        "birthday": birthday,
        "inactive": inactive,
        "debut": debut,
        "embed_url": embed_url,
        "state": state
    }
    pd_json = pd.DataFrame(pd_data).to_json(orient="records")
    pd_json = json.loads(pd_json)
    # result = sorted(pd_json, key=lambda pd_json: (pd_json['channel_num']))
    result = sorted(pd_json, key=itemgetter('channel_num'))
    return result

def fetch(row):
    live = lv.ytid(row['channel_id'])
    live = live[0]
    if not live['timestamp'] == 'NONE':
        dt = datetime.datetime.fromtimestamp(int(live['timestamp']))
        live['timestamp'] = dt.strftime("%Y-%m-%d %H:%M:%S")
    # 나중에 현재 시간 기준으로 1주일 이내 방송만 표시 되게 끔 수정할 예정임
    channel_num.append(row['channel_num'])
    channel_name.append(row['channel_name'])
    channel_url.append(row['channel_url'])
    channel_id.append(row['channel_id'])
    published_at.append(row['published_at'])
    birthday.append(row['birthday'])
    inactive.append(False) if row['inactive'] == 0 else inactive.append(True)
    debut.append(row['debut'])
    embed_url.append("https://www.youtube.com/embed/live_stream?channel=" + row['channel_id'])
    state.append(live)