from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # By クラスをインポート
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://www.google.com')
driver.implicitly_wait(10)

# 検索ボックスを By.NAME を使って見つけます
search_box = driver.find_element(By.NAME, 'q')

search_box.send_keys('Python')
search_box.send_keys(Keys.RETURN)
driver.implicitly_wait(10)

driver.quit()
