from trello import TrelloClient


import os
import configparser
import datetime


def class_insert(yobi):
    classes_list = classes[yobi]
    for card in classes_list:
        todo_list.add_card(card)

#config.iniからapi_key,secret_key,board_idを読み込む
config_ini  = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

os.environ["trello_key"] = config_ini['login']['api_key']
os.environ["trello_secret"] = config_ini['login']['trello_secret']
os.environ["id_board"] = config_ini['login']['bd_id']


client = TrelloClient(
    api_key = os.environ["trello_key"],
    api_secret = os.environ["trello_secret"],
)

#毎日行うtodoはここへ
everyday_todo = ['読書', 'Atcoder', '就活に時間を当てよう', 'pythonの勉強']

#授業はここへ/または曜日事のtodoはここへ
classes = {
    "Mon":['Risk Management', 'Data Science Concept'],
    "Tue":['Discrete Mathmatics'],
    "Wed":['Risk Management'],
    "Thu":['Computer Language'],
    "Fri":['Risk Management', 'Network Security'],
    "Sat":[],
    "Sun":[],
}

#board_idはhttps://trello.com/b/○○ の〇〇の部分を入れる。
board_id = os.environ["id_board"]

#0番目にtodoリストがあるのでboard.list_lists()[0]をtodo_listに入れる。
board = client.get_board(board_id)
todo_list = board.list_lists()[0]

#前日までのtodoをアーカイブする
todo_list.archive_all_cards()

#変数"yobi"に今日が何曜日かを入れる。
dt_now = datetime.datetime.now()
yobi = dt_now.strftime('%a')

#毎日のtodoをtodoリストに入れる。
for card in everyday_todo:
    todo_list.add_card(card)

#曜日ごとの授業をtodoに入れる。
class_insert(yobi)