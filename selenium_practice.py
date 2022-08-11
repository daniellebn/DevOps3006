"""from selenium import webdriver
from selenium.webdriver.common.by import By

import time

path = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://clalit.co.il/he/Pages/default.aspx")
print(driver.title)
search = driver.find_element(By.ID, 'tbUserId')
search.send_keys("203826656")"""

import requests
"""payload = {'key1': 'value1'}
# GET request
r_get = requests.get('https://httpbin.org/get', params=payload)
print(r_get.url)

# POST request
r_post = requests.post('https://httpbin.org/post', data=payload)
print(r_post.text)"""

res = requests.get('https://httpbin.org/get')
print(res.status_code)

print(res.json())