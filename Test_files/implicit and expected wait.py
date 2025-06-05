import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# implicit wait
# driver.implicitly_wait(10)
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
# driver.find_element(*VISIBLE_AFTER_BUTTON).click()

#Explicit wait
wait = WebDriverWait(driver, 15)
"""ожидать пока, в скобках бибилотека управления условием, функция распоковывает кортеж сама, также результатом работы данной функции ниже будет элемент
поэтому на него можно сразу кликнуть"""
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)).click()

# клик по появляющемуся элементу
ENABLE_IN_SECOND = ("xpath", "//button[@id=''enableAfter]")
wait.until(EC.element_to_be_clickable(EncodingWarning)).click()

# Клик по исчезающей кнопке
REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
driver.find_element(*REMOVE_BUTTON).click()
wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON)).click()

# Дожидаемся кликабельности
ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
TEXT_FIELD = ("xpath", "//input[@type='text']")
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
# Ожидаем доступности ввода поля input
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys('Hello')

# Текст в элементе появляется в атрибуте, в поле
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, 'Hello'))


driver.get('https://demoqa.com/dynamic-properties')

