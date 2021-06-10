import requests

receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
with open(r'C:\Users\Soccerboy_Krish\src\trello\db','wb') as f:
    f.write(receive.content)

