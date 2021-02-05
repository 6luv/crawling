import urllib.request                           #URL 요청을 위한 클래스, 함수 정의
from bs4 import BeautifulSoup                   #BeautifulSoup을 사용하기 위해 정의
import csv                                      #csv를 테이블로 가져옴

hdr = {'User-Agent' : 'Mozilla/5.0'}            #크롤링시 봇이 아님을 증명
url1 = 'https://www.melon.com/chart/index.htm'  #크롤링 할 URL

req = urllib.request.Request(url1, headers=hdr) #URL 요청을 추상화하기 위한 클래스
html = urllib.request.urlopen(req).read()       #URL을 열기위한 함수, read()는 데이터를 바이트형으로 받음
soup = BeautifulSoup(html, 'html.parser')       #HTML 데이터를 BeautifulSoup 읽기

song_list = soup.select('tbody > tr')           #.select를 사용하여 tbody 태그 바로 아래 tr 태그 정보를 song_list에 저장

melonlist = []                                  #빈 리스트 정의
for song in song_list:                          #노래 리스트 만큼 반복
    temp = []                                   #빈 리스트 정의

             #div.ellipsis.rank01 > span > a의 정보 가져옴, [0]은 리스트 형식 없애줌, .text는 텍스트 형식으로 temp에 저장
    temp.append(song.select('div.ellipsis.rank01 > span > a')[0].text) 
    temp.append(song.select('div.ellipsis.rank02 > span > a')[0].text)
    temp.append(song.select('div.ellipsis.rank03 > a')[0].text)
    melonlist.append(temp)                      #temp를 melonlist에 저장

                                                    #with open(파일의 경로, 모드, 인코딩, 자동 개행 방지) as 파일의 객체
with open('melon100.csv', 'w', encoding='utf-8', newline='') as f: 
    wirter = csv.writer(f)                      #csv파일로 저장
    wirter.writerow(['곡명', '가수명', '앨범명'])  #csv파일 가장 위에 표시
    wirter.writerows(melonlist)                 #쓰기 모드로 melonlist에 있는 내용 저장