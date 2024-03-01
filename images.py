from selenium import webdriver
import re
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service('./chromedriver-win64/chromedriver.exe'))
product_url=open('ptoduct_url.text','r')
count=0
img_counter=0
lines=product_url.readlines()
img_url=open('img_url.text','w')

for i in lines:
    print(i)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    count+=1
    driver.get('%s'%i)
    time.sleep(3)
    swap_page=driver.find_element(By.XPATH,"//div[@class['ReactModal__Content ReactModal__Content--after-open bg-neutral-000 absolute overflow-y-hidden rounded-medium styles_Modal__TsaRp']]")
    img_gallery=swap_page.find_element(By.XPATH,"//div[@class['flex flex-wrap']]")
    img_src=img_gallery.find_elements(By.XPATH,"//img[@class['w-full bg-neutral-000 inline-block']]")

    for link in img_src:
        src_link=link.get_attribute('src')
        verifie_img=re.search(r'(\/\/dkstatics)',str(src_link))
        if verifie_img != None:
            print(src_link)
            img_counter+=1
            print(img_counter)
            img_url.writelines('%s\n'%src_link)


    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    if count == 2:
        break
driver.quit()
img_url.close()




# driver.maximize_window()
# for images in image:
#         driver.get('https://www.digikala.com/search/category-mobile-phone/product-list/')
#         time.sleep(3)
#         parentWindow= driver.window_handles
#         print(images.get_attribute('href'))
#         all_url=re.search(r'(/product/.*?/)',str(images.get_attribute('href')))
#         # all_url=re.search(r'.*product/dkp(.+?)\/',str(images.get_attribute('href')))
          




         
# driver.close()
print('finish')

