from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import chromedriver_binary
import time


driver = webdriver.Chrome() 
driver.get('https://members.classmethod.net/#!/login')

try:
  id = WebDriverWait(driver, 15).until(
    expected_conditions.presence_of_element_located((By.ID, "loginID"))
  )
  print(id)
  print(driver.title)
except TimeoutError:
  print("Timeout")

wrapper = driver.find_element_by_id("wrapper")
id = driver.find_element_by_id("loginID")
print(id)
# password = driver.find_element_by_id("loginPW")
time.sleep(5)
driver.quit()
