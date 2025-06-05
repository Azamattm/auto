import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://ru.wikipedia.org/')

# url = driver.current_url
# print(f'URL страницы: {url}')
# assert url == "https://ru.wikipedia.org/", "Ошибка в url, открыта не та страница"

# current_title = driver.title
# print(f'Title страницы: {current_title}')
# assert current_title == 'Википедия', 'Некорректный заголовок страницы'

print(driver.page_source)

time.sleep(3)