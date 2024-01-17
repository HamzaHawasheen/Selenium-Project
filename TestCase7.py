import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
time.sleep(3)
driver.maximize_window()
search_field = driver.find_element(By.ID, 'APjFqb')
search_field.send_keys('AAUP')
search_field.submit()
time.sleep(3)
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'جامعة')
search_field.click()
time.sleep(3)
search_field = driver.find_element(By.ID, 'menu-10359-2')
search_field.click()
time.sleep(3)
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'البوابة')
search_field.click()
time.sleep(3)
handles = driver.window_handles
driver.switch_to.window(handles[1])
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'Login')
search_field.click()
time.sleep(3)
search_field = driver.find_element(By.NAME, 'lognForm:j_idt17')
search_field.send_keys('hamza')
time.sleep(3)
search_field = driver.find_element(By.NAME, 'lognForm:j_idt21')
search_field.send_keys('12345')
time.sleep(3)
search_field = driver.find_element(By.NAME, 'lognForm:j_idt27')
search_field.click()
time.sleep(6)
driver.close()