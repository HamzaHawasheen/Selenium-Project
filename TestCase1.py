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
search_field = driver.find_element(By.NAME, 'search_block_form')
search_field.send_keys('هندسة')
search_field.submit()
time.sleep(3)
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'الجودة الأكاديمية')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(3)
search_field.click()
time.sleep(3)
search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'اعتماد ABET لبرنامج هندسة أنظمة الحاسوب')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(3)
search_field.click()
time.sleep(3)
search_field = driver.find_element(By.XPATH, '//*[@id="node-19256"]/div/div/div[5]/div/div[1]/img')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(3)
search_field = driver.find_element(By.XPATH, '//*[@id="node-19256"]/div/div/div[5]/div/div[2]/img')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(3)
search_field = driver.find_element(By.XPATH, '//*[@id="node-19256"]/div/div/div[5]/div/div[3]/img')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(3)
search_field = driver.find_element(By.XPATH, '//*[@id="node-19256"]/div/div/div[5]/div/div[4]/img')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });", search_field)
time.sleep(6)
driver.close()