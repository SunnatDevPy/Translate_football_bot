import requests
import http.client
from datetime import datetime, timedelta
import pytz
from aiogram.utils.text_decorations import html_decoration


def change_timezone(iso_date_str):
    dt_utc = datetime.fromisoformat(iso_date_str)

    local_tz = pytz.timezone('Asia/Tashkent')
    dt_local = dt_utc.astimezone(local_tz)

    formatted_date_str = dt_local.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date_str


def get_data():
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "666fb3a3f0mshd6f49ac99388165p10de96jsn4e667b43a669",
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }
    # url = "https://api-football-v1.p.rapidapi.com/v3/predictions"

    # url = "https://api-football-v1.p.rapidapi.com/v2/timezone"
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    # url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    # url = "https://api-football-v1.p.rapidapi.com/v3/countries"
    # url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

    # querystring = {"last": "50"}
    # querystring = {"type":"cup"}  # keyingi o'yinlar ro'yxati
    # querystring = {"league": "78", "season": "2024"}  # liga bo'yicha o'yinlar
    querystring = {"live":"all"}  # liga bo'yicha o'yinlar
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()



# print(datetime.today().date() - timedelta(days=1))

print(get_data())


# def live_game(res, id):
#     list_ = []
#     data = res['response']
#     print(data)
#     for i in data:
#         league = i.get('league')
#         if league['id'] == id:
#             status = ''
#             if i['status']['long'] == 'Halftime':
#                 status = "Tanafus"
#
#             short = "1 time" if i['status']['short'] == '1H' else '2 time'
#             result = team_goal(i['events'], i['teams'])
#             text = html_decoration.bold(f'''
# 🏟Stadion: {i['fixture']['venue']['name']}
# 🌇Shaxar: {i['fixture']['venue']['city']}
# ⌛Boshlangan vaqti (Toshkent): {change_timezone(i['fixture']['date'])}
# Bosqich: {short} {status}
# Hozirgi daqiqa: {i['status']['elapsed']}
#
# 🏠Uyda: {i['teams']['home']['name']}
#
# Statistika
# Goal: {html_decoration.code(i['goals']['home'] if i['goals']['home'] else 0)}
# Penalty: {i['score']['penalty']['home'] if i['score']['penalty']['home'] else 0}
# Extra time: {i['score']['extratime']['home'] if i['score']['extratime']['home'] else 0}
# {result[0]}
#
# 🤼Mehmonda: {i['teams']['away']['name']}
#
# Statistika
# Goal: {html_decoration.code(i['goals']['away'] if i['goals']['away'] else 0)}
# Penalty: {i['score']['penalty']['away'] if i['score']['penalty']['away'] else 0}
# Extra time: {i['score']['extratime']['away'] if i['score']['extratime']['away'] else 0}
# {result[1]}
# ''')
#             list_.append(text)
#     return list_
#
#
# def team_goal(events, teams):
#     home = ""
#     away = ""
#     for i in events:
#         type = "urdi" if i['type'] == "Goal" else "oldi"
#         assist = f"Assist: {i['assist']['name']} \n\n" if i['assist']['name'] else " "
#         extra = f"Extra Time: " if i['time']['extra'] else "Time: "
#         if i['team']["id"] == teams['home']["id"]:
#             home += '=========================================\n'
#             home += f'{extra}{i["time"]["elapsed"]} \n'
#             home += f"Player: {i['player']['name']} {type}\n"
#             home += assist
#         else:
#             away += '=========================================\n'
#             away += f'{extra}{i["time"]["elapsed"]} \n'
#             away += f"Player: {i['player']['name']} {type}\n"
#             away += assist
#     return home, away


# print(live_game(get_data(),78))
