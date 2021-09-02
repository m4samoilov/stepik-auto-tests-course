from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver 
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять price в течение 12 секунд, когда price станет $100 - переход дальше
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )

    # находим кнопку на странице и кликаем (когда условие выполнилось)
    browser.find_element(By.ID, "book").click()

    # находим значение для х и расчитываем его
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # находим инпут и вводим в него получившееся значение у
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # находим кнопку на странице и делаем отскролл вниз (так чтобы была видна кнопка)
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


# 123
