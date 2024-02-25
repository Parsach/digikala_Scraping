from selenium import webdriver
import re
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service('./chromedriver-win64/chromedriver.exe'))
scroll=0
driver.maximize_window()

driver.get('https://www.digikala.com/search/category-mobile-phone/product-list/')
#driver.get('https://www.digikala.com/search/category-mobile-phone/product-list/')
time.sleep(10)
driver.execute_script("window.scrollTo(0,15)")
driver.implicitly_wait(15)
element=driver.find_element(By.CLASS_NAME,'flex items-center mt-5 mb-3')
image=element.find_elements(By.XPATH,"")
#image=driver.find_elements(By.XPATH,"//a[@class['block cursor-pointer relative bg-neutral-000 overflow-hidden grow py-3 px-4 lg:px-2 h-full styles_VerticalProductCard--hover__ud7aD']]")
#div[@class'flex items-center mt-5 mb-3'] w-full inline-block

for images in image :
     all_url=re.search(r'.*product/dkp(.+?)\/',str(images.get_attribute('href')))      
     print(all_url)

# for i in range(1,7):
        
#         time.sleep(5)
#         scroll+=1000
#         driver.execute_script("window.scrollTo(0,%i)"%scroll)
         
driver.close()
print('finish')

