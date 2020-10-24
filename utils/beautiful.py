import requests
from bs4 import BeautifulSoup


target_url = "https://apex.tracker.gg/apex/leaderboards/pc/RankScore"
r = requests.get(target_url)

soup = BeautifulSoup(r.text, 'lxml')

a_items = soup.find_all("a", attrs={"class": "trn-lb-entry__name"})
for item in a_items:
    print(item.string)
print(soup.find("a", attrs={"class": "trn-lb-entry__name"}).string)

