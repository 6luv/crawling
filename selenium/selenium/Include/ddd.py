# 노른자마트 크롤링

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from urllib.parse import parse_qs, parse_qsl
import urllib.parse
import urllib.request
import time
import csv
import pandas as pd

def isCondition( number, j):
   if ( number == 5 and j == 2 or number == 7 and j == 2 or number == 18 and j == 2 or number == 20 and j == 2 or number == 21 and j == 2 or number == 22 and j == 2 or number == 30 and j == 3 or number == 20 and j == 4 or number == 13 and j == 6 or number == 14 and j == 6 or number == 15 and j == 6 or number == 16 and j == 6 or number == 21 and j == 6 or number == 22 and j == 6 or number == 23 and j == 6 or number == 25 and j == 6 or number == 27 and j == 6 or number == 28 and j == 6 or number == 29 and j == 6 or number == 30 and j == 6 or number == 31 and j == 6 or number == 3 and j == 7 or number == 6 and j == 7 or number == 7 and j == 7 or number == 8 and j == 7 or number == 9 and j == 7 or number == 10 and j == 7 or number == 11 and j == 7 or number == 12 and j == 7 or number == 13 and j == 7 or number == 14 and j == 7 or number == 16 and j == 7 or number == 17 and j == 7 or number == 18 and j == 7 or number == 19 and j == 7 or number == 20 and j == 7 or number == 22 and j == 7 or number == 25 and j == 7 or number == 26 and j == 7 or number == 27 and j == 7 or number == 28 and j == 7 or number == 29 and j == 7 or number == 30 and j == 7 or number == 31 and j == 7 or number == 32 and j == 7):
      return True
   else:
      return False

driver = webdriver.Chrome("C:/Users/201820969/Desktop/coding/Crawling/selenium/selenium/chromedriver.exe")
driver.get('https://smartstore.naver.com/yelloweggmart/category/f5488b8f2b5b4132add19275a3723ea0?st=POPULAR&free=false&dt=IMAGE&page=3&size=40')

address = driver.find_elements_by_css_selector(".-qHwcFXhj0")

arCol = []      #전역변수

images = []     #이미지
names = []      #과자 이름
data = []       #과자, 이미지 데이터
count = 1       #사진 저장할 때 이름 (1씩 증가)
urlList = []
number = 3      #세번째 이미지부터 시작
j = 2       #페이지 버튼 (1페이지가 j=2)

while True:
    try:
        if (number != 41):
            product = driver.find_element_by_xpath("//*[@id='CategoryProducts']/ul/li[" + str(number) + "]/a")
            product.click()     #제품 클릭
            time.sleep(1)

            name = driver.find_element_by_css_selector("._3oDjSvLwq9._copyable").text       #과자 이름 text로 받아오기

            if isCondition( number, j) :
                image = driver.find_element_by_xpath(
                    "/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[5]/div/div[5]/div[2]/div/div/div/div/div[2]/div/div/div/a/img").get_attribute(
                    "data-src")     #data-src형태로 가지고 오겠다
            else:
                image = driver.find_element_by_xpath(
                    "/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[5]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div/div/a/img").get_attribute(
                    "data-src")

            imgurl = urllib.parse.urlparse(image)       #주소를 분석하기
            path = imgurl[2]        #2가 path다.
            replaced = imgurl._replace(path=urllib.parse.quote(path))       #컴퓨터가 읽을 수 있게 바꿔주기(한글을), quote는 (한글을 utf-8로 인코딩)
            replaced = urllib.parse.urlunparse(replaced)        #분석한 거를 원래 주소로 합쳐준다? 주소를 나눈 거 다시 붙여주기

            temp = []       # 빈 리스트

            arURL = driver.current_url.split("/")
            urlList.append( arURL[5] )

            temp.append(arURL[5])
            temp.append(name)       #과자 이름 추가
            temp.append(replaced)

            urllib.request.urlretrieve(replaced, arURL[5] + ".jpg")       #이미지 저장

            data.append(temp)
            driver.back()
            time.sleep(0.5)
            number = number + 1     #이미지 하나씩 늘리기
            count += 1      #사진 저장할 때 이름 하나씩 늘리기

        else:
            j = j + 1       #다음 페이지 넘어가기
            next = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/a["+str(j)+"]")
            next.click()
            time.sleep(3)
            number = 1
            # break
    except:
        break

data = pd.DataFrame(data)
data.columns = ['상품코드', '상품명', '영양정보']
data.head()

data.to_csv('C:/Users/201820969/Desktop/coding/Crawling/selenium/data.csv', index=False, header=True,
            encoding='utf-8-sig')
with open('data.csv', 'w', index=False, encoding='utf-8', newline='') as f:
    writer = csv.writer(f)  # csv파일로 저장
    writer.writerows(data)