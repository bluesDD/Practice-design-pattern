from selenium import webdriver
import chromedriver_binary
import time


driver = webdriver.Chrome() 
driver.get('https://members.classmethod.net/#!/login')
id = driver.find_element_by_id("loginID")

time.sleep(5)
driver.quit()
