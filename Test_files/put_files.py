import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://the-internet.herokuapp.com/upload')
driver.find_element("xpath", "//input[@type='file']").send_keys(f"{os.getcwd()}\\download\\random_data.txt")
time.sleep(4)