# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse 
from urllib.parse import quote
from urllib.parse import parse_qs, parse_qsl
import urllib.request
import time
import csv
import pandas as pd

driver = webdriver.Chrome("C:/Users/장영아/Desktop/aaa/selenium/chromedriver")
driver.get('https://smartstore.naver.com/yelloweggmart/category/87db5aa627874111b9ac8060905a2d54?st=POPULAR&free=false&dt=IMAGE&page=1&size=40')

address = driver.find_elements_by_css_selector(".-qHwcFXhj0")
images = []
names = []
data = []
count = 1
number = 3
j = 3
while True:
    try:
        if (number != 41):
            product = driver.find_element_by_xpath("//*[@id='CategoryProducts']/ul/li["+str(number)+"]/a")
            product.click()
            time.sleep(1)
            name = driver.find_element_by_css_selector("._3oDjSvLwq9._copyable").text
            if(number == 40 and j == 3):
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
            time.sleep(1)
            number = number + 1
            count += 1
            print(data)
        else:
            next = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/a["+str(j)+"]")
            next.click()
            time.sleep(3)
            j = j + 1
            number = 1
            # break
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


data.to_csv('C:/Users/장영아/Desktop/aaa/data.csv', index=False, header=True, encoding='utf-8-sig')
with open('data.csv', 'w', index=False, encoding='utf-8', newline='') as f:
    writer = csv.writer(f)                      #csv파일로 저장
    # writer.writerow(['상품명', '영양정보'])
    writer.writerows(data) 

        

