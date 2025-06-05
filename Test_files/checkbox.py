from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://the-internet.herokuapp.com/checkboxes')
select = select()

CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")
print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
driver.find_element(*CHECKBOX_1).click()
print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))