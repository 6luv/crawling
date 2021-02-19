# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from urllib.parse import parse_qs, parse_qsl
import urllib.request
import time
import csv
import pandas as pd

driver = webdriver.Chrome("C:/Users/201820969/Desktop/selenium/selenium")
driver.get('https://smartstore.naver.com/yelloweggmart/category/87db5aa627874111b9ac8060905a2d54?cp=1')

address = driver.find_elements_by_css_selector(".-qHwcFXhj0")
images = []
names = []
count = 1
number = 3
j = 3
while True:
    try:
        if (number != 41):
            product = driver.find_element_by_xpath("//*[@id='CategoryProducts']/ul/li["+str(number)+"]/a")
            product.click()
            time.sleep(2)
            name = driver.find_element_by_css_selector("._3oDjSvLwq9._copyable").text
            image = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/div[5]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div/div/a/img").get_attribute("data-src")
            #urllib.request.urlretrieve(image, str(count) + ".jpg")
            imgurl = urllib.parse.urlparse(image)
            

            # path = imgurl[2]
            # #print(path)
            # path = urllib.parse.quote(path)
            # imgurl[2].update(path)
            print(imgurl)
            
            

            # print(urllib.parse.urlencode(path, doseq=False, safe=' ', encoding="UTF-8", errors=None))
        
            names.append(name)
            #print(image)
            images.append(image)
            
            driver.back()
            time.sleep(1)
            number = number + 1
            count += 1
            #print(images)
        else:
            next = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[3]/a["+str(j)+"]")
            next.click()
            time.sleep(3)
            j = j + 1
            number = 1
            # break
    except:
        pass


# for i in range(len(images)):
    
    

# names = pd.DataFrame(names)
# names.columns=['name']
# names.head()


# names.to_csv('C:/Users/장영아/Desktop/aaa/list.csv', index=False, header=True, encoding='utf-8-sig')
# with open('list.csv', 'w', index=False, encoding='utf-8', newline='') as f:
#     wirter = csv.writer(f)                      #csv파일로 저장
#     wirter.writerows(names) 

        

