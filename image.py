from selenium import webdriver
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
time.sleep(5)
driver.execute_script("window.scrollTo(0,15)")
driver.implicitly_wait(15)
image=driver.find_elements(By.XPATH,"//img[@class['w-full rounded-medium inline-block']]")

for images in image :
            
     print (images.get_attribute('src'))
# for i in range(1,7):
        
#         time.sleep(5)
#         scroll+=1000
#         driver.execute_script("window.scrollTo(0,%i)"%scroll)
         
driver.close()
print('finish')

