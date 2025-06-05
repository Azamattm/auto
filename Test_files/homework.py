from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_fn = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    input_fn.click()
    input_fn.send_keys("Jhon")

    input_ln = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    input_ln.click()
    input_ln.send_keys("Snow")


    input_email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    input_email.click()
    input_email.send_keys("jimbo123@gmail.com")

    input_phone = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone:']")
    input_phone.click()
    input_phone.send_keys("89993456712")   

    input_adress = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address:']")
    input_adress.click()
    input_adress.send_keys("Lenin Str, 34")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

