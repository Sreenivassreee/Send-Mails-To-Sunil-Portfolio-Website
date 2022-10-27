from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
f = open('q.json')
data = json.load(f)

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get('https://sunilreddy-chinthaparthi.github.io/Personal_Website/')
wait = WebDriverWait(driver, 10)
def clear():
    driver.find_element(By.XPATH, '//*[@id="contact"]/div/form/input[1]').clear()
    driver.find_element(By.XPATH, '//*[@id="contact"]/div/form/input[2]').clear()
    driver.find_element(By.XPATH, '//*[@id="contact"]/div/form/textarea').clear()
for i in data['quotes']:
    quote=i['quote']
    author=i['author']
    driver.find_element(By.XPATH, '//*[@id="contact"]/div/form/input[1]').send_keys(author)
    driver.find_element(By.XPATH, '//*[@id="contact"]/div/form/input[2]').send_keys(author+'@Gmail.com')
    driver.find_element(By.XPATH, '//*[@id="contact"]/div/form/textarea').send_keys(quote)
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//*[@id="contact"]/div/form/button')
    driver.execute_script("arguments[0].click();", element)
    print("Send -"+str(i))
    time.sleep(1)
    clear()
driver.close()




