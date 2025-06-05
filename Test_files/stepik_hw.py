import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, "[id='book']")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[id='price']"), "$100"))
button.click()

x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = int(x_element.text)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

result = browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys(calc(x))

# name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']").send_keys('Jason')
# last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']").send_keys('Stathom')
# email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']").send_keys('jason_one@gmail.com')

# button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
# button.send_keys(f"{os.getcwd()}\\lessons\\download\\test.txt")

Button = browser.find_element(By.CSS_SELECTOR, "[id='solve']")
browser.execute_script("return arguments[0].scrollIntoView(true);", Button)
Button.click()
time.sleep(4)