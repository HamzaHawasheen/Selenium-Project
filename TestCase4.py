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
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'المكتبة')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(3
search_field.click()
time.sleep(3)
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'التخرج')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(3)
search_field.click()
time.sleep(3)
search_field = driver.find_element(By.ID, 'rBooksForm:searchTxt')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(3)
search_field.send_keys('هندسة أنظمة حاسوب')
search_field.submit()
time.sleep(3)
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'مشروع')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(3)
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'division')
search_field.click()
time.sleep(3)
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'إغلاق')
search_field.click()
time.sleep(6)
driver.close()