import json
import pandas as pd
from ytlv import *

def json_to_dict_board(result):
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

    for row in result:
        live = lv.ytid(row['channel_id'])
        live = live[0]
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
    return json.loads(pd_json)