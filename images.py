from selenium import webdriver
import re
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import product_list
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service('./chromedriver-win64/chromedriver.exe'))

driver.maximize_window()
for images in image:
        driver.get('https://www.digikala.com/search/category-mobile-phone/product-list/')
        time.sleep(3)
        parentWindow= driver.window_handles
        print(images.get_attribute('href'))
        all_url=re.search(r'(/product/.*?/)',str(images.get_attribute('href')))
        # all_url=re.search(r'.*product/dkp(.+?)\/',str(images.get_attribute('href')))
          




         
driver.close()
print('finish')

