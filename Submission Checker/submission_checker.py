from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import pandas as pd

homeworks = ['Say "Hello, World!" With Python', 'Python If-Else', 'Python: Division','Loops', 
             'Write a function', 'Print Function', 'List Comprehensions', 'Find the Runner-Up Score!',
             'Nested Lists', 'Finding the percentage', 'Introduction to Sets', 'Lists']

result = {}
result.setdefault("names", [])
result.setdefault("total", [])

PATH = "C:\Program Files\chromedriver.exe" #write your own path!!

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
#chrome_options.headless = True

driver = webdriver.Chrome(PATH, options = chrome_options)

link = "https://www.hackerrank.com/"

df = pd.read_csv("names.csv")

for i in df.user_name:
    
    data = []
    
    new_link = link + i
    
    driver.get(new_link)
    
    time.sleep(2)
    
    load_button = driver.find_elements_by_xpath("//button[@class='ui-btn ui-btn-normal ui-btn-line-primary history-load-more ui-btn-styled']")
    len_button = len(load_button)
    
    while(len_button > 0):
        
        driver.find_element_by_xpath("//button[@class='ui-btn ui-btn-normal ui-btn-line-primary history-load-more ui-btn-styled']").click()
        time.sleep(1)
        len_button = len(driver.find_elements_by_xpath("//button[@class='ui-btn ui-btn-normal ui-btn-line-primary history-load-more ui-btn-styled']"))
        
    
    history = driver.find_elements_by_xpath("//a[@class='history-list-item-link']")
    
    for k in history:
        data.append(k.text)
    
    count = 0
    
    for homework in homeworks:
        for z in data:
            if homework == z:
                count = count + 1
                break
    
    print("{0}: {1}/12" .format(i, count))
    
    result["names"].append(i)
    result["total"].append(count)
    
df = pd.DataFrame(data=result)
df.to_csv('result.csv', index=False)

            
    