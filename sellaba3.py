from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time


AnyWords = 'anywords.txt'

data = []

# with open('anywords.txt', encoding='utf-8') as file:
#     for line in file:
#         data.append(line)
        


driver = webdriver.Chrome()
url = 'https://www.bukvarix.com'

driver.get(url)

def find_keyword(keyword: str):
    print(f'{keyword:.^30}')
    if 'keywords' in driver.current_url:
        search_input = driver.find_element(By.ID, 'search_form_q')
        search_button = driver.find_element(By.CSS_SELECTOR, '.search-form-submit-f > input:nth-child(1)')
        search_input.send_keys(Keys.CONTROL + 'A')
        time.sleep(2)
        search_input.send_keys(Keys.DELETE)
        time.sleep(2)
    else:
        search_input = driver.find_element(By.ID, 'SearchFormIndexQ')
        search_button = driver.find_element(By.CSS_SELECTOR, '.search-form-submit-index > input:nth-child(1)')
    search_input.send_keys(keyword)
    time.sleep(2)
    search_button.click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'report-download-button').click()
    print(f'сохранён файл {keyword}.csv')


time.sleep(2)
with open(AnyWords, encoding='UTF-8') as f:
    for line in f:
        find_keyword(line.rstrip('\n'))
        time.sleep(2)
    driver.close()
    driver.quit()


# try:
#     for i in range(len(data)):
#         driver.get(url)
#         time.sleep(2)

#         sc_button = driver.find_element(By.CSS_SELECTOR, '#SearchFormIndexQ')
#         sc_button.click()

#         Words = driver.find_element(By.ID, 'SearchFormIndexQ')
#         Words.send_keys(data[i])

#         time.sleep(2)

#         sc_button = driver.find_element(By.CSS_SELECTOR,'#search_form_index > div.search-form-submit-index > input[type=submit]')
#         sc_button.click()

#         time.sleep(2)
        
#         # sc_button = driver.find_element(By.CSS_SELECTOR, '##search_form_q')
#         # sc_button.double_click()
    
#         time.sleep(2)


# except Exception as e:
#     print(e)
# finally:
#     driver.close()
#     driver.quit()