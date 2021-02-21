# 노른자마트 크롤링
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from urllib.parse import parse_qs, parse_qsl
import urllib.parse 
import urllib.request
import time
import csv
import pandas as pd

driver = webdriver.Chrome("C:/Users/201820969/Desktop/coding/Crawling/selenium/selenium/chromedriver.exe")
driver.get('https://smartstore.naver.com/yelloweggmart/category/f5488b8f2b5b4132add19275a3723ea0?cp=1')

address = driver.find_elements_by_css_selector(".-qHwcFXhj0")

images = []
names = []
data = []
count = 1
number = 3
j = 2
while True:
    try:
        if (number != 10):                  
            product = driver.find_element_by_xpath("//*[@id='CategoryProducts']/ul/li["+str(number)+"]/a")
            product.click()
            time.sleep(1)

            name = driver.find_element_by_css_selector("._3oDjSvLwq9._copyable").text
            if(number == 5 and j == 2 or number == 7 and j == 2 or number == 18 and j == 2 or number == 20 and j == 2 or number == 21 and j == 2 or number == 22 and j == 2 or number == 30 and j == 3 or number == 20 and j == 4 or number == 13 and j == 6 or number == 14 and j == 6 or number == 15 and j == 6 or number == 16 and j == 6 or number == 21 and j == 6 or number == 22 and j == 6 or number == 23 and j == 6 or number == 25 and j == 6 or number == 27 and j == 6 or number == 28 and j == 6 or number == 29 and j == 6 or number == 30 and j == 6 or number == 31 and j == 6 or number == 3 and j == 7 or number == 6 and j == 7 or number == 7 and j == 7 or number == 8 and j == 7 or number == 9 and j == 7 or number == 10 and j == 7 or number == 11 and j == 7 or number == 12 and j == 7 or number == 13 and j == 7 or number == 14 and j == 7 or number == 16 and j == 7 or number == 17 and j == 7 or number == 18 and j == 7 or number == 19 and j == 7 or number == 20 and j == 7 or number == 22 and j == 7 or number == 25 and j == 7 or number == 26 and j == 7 or number == 27 and j == 7 or number == 28 and j == 7 or number == 29 and j == 7 or number == 30 and j == 7 or number == 31 and j == 7 or number == 32 and j == 7):
                image = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[5]/div/div[5]/div[2]/div/div/div/div/div[2]/div/div/div/a/img").get_attribute("data-src")
            else:                                 
                image = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[5]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div/div/a/img").get_attribute("data-src")
            imgurl = urllib.parse.urlparse(image)
            path = imgurl[2]
            replaced = imgurl._replace(path = urllib.parse.quote(path))
            replaced = urllib.parse.urlunparse(replaced)
            urllib.request.urlretrieve(replaced, str(count) + ".jpg")
            
            temp = []
            temp.append(name)
            temp.append(replaced)

            data.append(temp)
            driver.back()
            time.sleep(0.5)
            number = number + 1
            count += 1
            print(data)
        else:
            # j = j + 1
            # next = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/a["+str(j)+"]")
            # next.click()
            # time.sleep(3)
            # number = 1
            break
    except:
        break

# data.to_csv('C:/Users/장영아/Desktop/aaa/data.csv', index=False, header=True, encoding='utf-8-sig')
# with open('data.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['상품명', '영양정보'])
#     writer.writerows(data)

data = pd.DataFrame(data)
data.columns=['상품명', '영양정보']
data.head()


data.to_csv('C:/Users/201820969/Desktop/coding/Crawling/selenium/data.csv', index=False, header=True, encoding='utf-8-sig')
with open('data.csv', 'w', index=False, encoding='utf-8', newline='') as f:
    writer = csv.writer(f)                      #csv파일로 저장
    writer.writerows(data) 

        


