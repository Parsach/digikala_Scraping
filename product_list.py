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
#driver.maximize_window()

product_url=open('ptoduct_url.text','w')

driver.get('https://www.digikala.com/search/category-mobile-phone/product-list/')
time.sleep(3)
driver.implicitly_wait(15)

# for i in range(1,15):
        
#         time.sleep(2)
#         scroll+=1100
#         driver.execute_script("window.scrollTo(0,%i)"%scroll)



image=driver.find_element(By.XPATH,"//div[@class['product-list_ProductList__pagesContainer__zAhrX product-list_ProductList__pagesContainer--withSidebar__17nz1 product-list_ProductList__pagesContainer--withoutSidebar__aty9j']]")
image_22=image.find_elements(By.XPATH,"//a[@class['block cursor-pointer relative bg-neutral-000 overflow-hidden grow py-3 px-4 lg:px-2 h-full styles_VerticalProductCard--hover__ud7aD']]")

 
for images_88 in image_22 :
     all_url=images_88.get_attribute('href')
     image_url=re.search(r'(/product/.*?/)',str(all_url))
     if image_url != None :
          print(image_url.group(1))
          x='https://www.digikala.com%s#gallery\n'%image_url.group(1)
          product_url.writelines(x)


driver.close()
product_url.close()
print('finish')

