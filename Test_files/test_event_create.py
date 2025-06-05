import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.page_load_strategy = "normal"
# options.add_argument("--window-size=1920, 1080")
options.add_argument("--start-fullscreen")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://eoffice6-pre.mos.ru/arm/login?from=calendar')

time.sleep(3)

login = driver.find_element("id", ":r0:")
login.click()
login.send_keys(os.environ['LOGIN'])
password_input = driver.find_element("xpath", "(//input)[2]")
password_input.click()
password_input.send_keys(os.environ["PASSWORD"])
button_auth = driver.find_element('xpath', '(//button)[2]')
button_auth.click()
print(password_input.get_attribute("value"))
time.sleep(4)
# sell_calendar = driver.find_element("xpath", "//button[text()='Создать событие']").click()
# print(sell_calendar)

name = 'СНА Ликс'
time_value = '14:00:00'
slot = driver.find_element("xpath", f"(//td[@data-time='{time_value}'])[2]")
slot.click()
slot_active = driver.find_element("xpath", "//div[@class='ql-editor ql-blank']")
slot_active.send_keys(f"{name}")
empty_slot = driver.find_element("xpath", "(//td[@data-time='13:30:00'])[2]")
empty_slot.click()
time.sleep(8)
