import requests
from bs4 import BeautifulSoup


target_url = "https://apex.tracker.gg/apex/leaderboards/pc/RankScore"
r = requests.get(target_url)

soup = BeautifulSoup(r.text, 'lxml')

print(soup.find_all("a", attrs={"class": "trn-lb-entry__name"}))

