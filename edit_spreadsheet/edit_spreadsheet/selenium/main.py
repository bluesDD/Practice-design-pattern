from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import chromedriver_binary
import time
import sys
import os

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/test.png")
target_url = "https://members.classmethod.net/#!/login"
user_id = "test"
user_password = "test"
element_id_user_id = "loginID"
element_id_user_password = "loginPW"
element_class_login_button = "btn"
options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options) 
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
  sys.exit("Timeout, check if the url is correct")

driver.save_screenshot(file_name)
time.sleep(5)
driver.quit()
