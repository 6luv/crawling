import urllib.request
from bs4 import BeautifulSoup
import csv


hdr = {'User-Agent' : 'Mozilla/5.0'}
url1 = 'https://www.melon.com/chart/index.htm'

req = urllib.request.Request(url1, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

song_list = soup.select('tbody > tr')

melonlist = []
for song in song_list:
    temp = []
    temp.append(song.select('div.ellipsis.rank01 > span > a')[0].text)
    melonlist.append(temp)

with open('melon100.csv', 'w', encoding='utf-8', newline='') as f:
    wirter = csv.writer(f)
    wirter.writerow(['곡명'])
    wirter.writerows(melonlist)