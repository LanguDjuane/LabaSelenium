from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Открываем браузер
browser = webdriver.Chrome()

# Открываем сайт
browser.get('https://www.bukvarix.com')

# Читаем строки из файла
with open('file.txt', 'r') as f:
    lines = f.readlines()

# Вводим строки в строку поиска на сайте
for line in lines:
    search_box = browser.find_element(By.ID, 'SearchFormIndexQ')
    search_box.send_keys(line)
    search_box.submit()
    time.sleep(5)

# Закрываем браузер
browser.quit()