from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome()
my_driver.get("C:/Users/Danielle/Desktop/tip_calc/index.html")
my_driver.find_element(by="id", value="billamt").send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element(by="id", value="peopleamt").send_keys("5")
my_driver.find_element(by="id", value="music2").click()
expected = "8.00"
actual = my_driver.find_element(by="id", value="tip").text
assert expected == actual
