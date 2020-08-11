from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import chromedriver_binary
import time
import sys

target_url = "https://members.classmethod.net/#!/login"
user_id = "test"
user_password = "test"
element_id_user_id = "loginID"
element_id_user_password = "loginPW"
element_class_login_button = "btn"
driver = webdriver.Chrome() 
driver.get(target_url)

try:
  id = WebDriverWait(driver, 15).until(
    expected_conditions.presence_of_element_located((By.ID, element_id_user_id))
  )
  id.send_keys(user_id)
  password = WebDriverWait(driver, 15).until(
    expected_conditions.presence_of_element_located((By.ID, element_id_user_password))
  )
  password.send_keys(user_password)
  driver.find_element_by_class_name(element_class_login_button).click()

except TimeoutError:
  sys.exit("Timeout")

time.sleep(5)
driver.quit()
