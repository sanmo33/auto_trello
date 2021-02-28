# auto_trello

毎日やること・曜日ごとにやることを自動でtrelloに入力してくれるプログラムです。

pip install py-trello

pythonで扱うのでpy-trelloをインストールします。

config.iniというファイルを同ディレクトリにいれて下記のように設定してください。
```
[login]
api_key = your api_key
trello_secret = your secret_key
bd_id  = your board_id
```
