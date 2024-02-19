# import requests
# import re
# from bs4 import BeautifulSoup as bs
# #for start need source of digikala
# for i in range (1,99):
#     url='https://www.digikala.com/product/dkp-%s'%i
#     respons=requests.get(url)#u can use every category an dirctory for scrap
#     print(respons)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# # options = webdriver.EdgeOptions()
# # options.add_experimental_option("detach", True)


# # chrome_driver_path = "D:\msedgedriver.exe"

# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# time.sleep(10)



# driver.get('https://www.digikala.com/search/category-mobile-phone/product-list')
# time.sleep(10)

# items=driver.find_elements(By.CLASS_NAME,"block cursor-pointer relative bg-neutral-000 overflow-hidden grow py-3 px-4 lg:px-2 h-full styles_VerticalProductCard--hover__ud7aD")
# time.sleep(10)

# product_img_path='//*[@id="ProductListPagesWrapper"]/section[1]/div[2]/div[10]/a/div/article/div[2]/div[1]/div/div/div[1]/div/picture/img'
# title_name_path='.//*[@id="ProductListPagesWrapper"]/section/div[3]/div[2]/a/div/article/div[2]/div[2]/div[2]/h3'
# price_path='.//*[@id="ProductListPagesWrapper"]/section/div[3]/div[2]/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span'


# for product in items:
#     time.sleep(10)

#     product_img=driver.find_element(By.XPATH,product_img_path).text
#     #title_name=items.find_element(by=By.XPATH,value=title_name_path)
#     #price=items.find_element(by=By.XPATH,value=price_path)
#     print(product_img)#title_name,price)
#***************************************************************************
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# website='https://www.digikala.com/search/category-mobile-phone/product-list'
# path=r"/chromedriver-win64/chromedriver.exe"


# driver=webdriver.Chrome()
# driver.get(website)
# assert "No results found." not in driver.page_source
# image=driver.find_elements(By.CLASS_NAME,'w-full rounded-medium inline-block')
# wait = WebDriverWait(driver, 30)

# print(image)
# driver.quit()
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
         

print('finish')

