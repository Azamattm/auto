import time
import os

import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")
# driver.get_cookie("country_code")
driver.get_cookies()
driver.add_cookie({
    "name": "Example",
    "value": "Kukushka"
})

before = driver.get_cookie("split")
# driver.delete_cookie("split")
driver.get_cookies()
driver.delete_all_cookies()

pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookie.pkl", "wb"))
cookies = pickle.load(open(os.getcwd() + "/cookies/cookie.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()