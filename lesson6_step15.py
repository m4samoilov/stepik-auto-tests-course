from selenium import webdriver 
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button").click()

    # объявляем переменную для новой вкладки
    new_window = browser.window_handles[1]
    # переключаемся на новую вкладку
    browser.switch_to.window(new_window)

    # находим значение для х и расчитываем его
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # находим инпут и вводим в него получившееся значение у
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

