from logging import exception
from socket import timeout
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# u need all of these packages
# and also a executable for selenium
# https://chromedriver.chromium.org/downloads

import time
import pyautogui

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

# put path of executable
driver = webdriver.Chrome(options=options,executable_path='/Users/msommerfeld/Desktop/chromedriver')


driver.maximize_window()

#driver = webdriver.Safari()
for time in ['33', '34']:
    while True:
        try:
            driver.get('https://login.maastrichtuniversity.nl'
                       '/adfs/ls/?  SAMLRequest=nZLNbtswEITvBfoOAu8SKcU%2FKmE5cGMENZC2Rqz00EtBS2ubALVUuZRTv31oqUb   Tg4OivJGcJb%2BZ3dntr8ZER3CkLRYsTQSLACtba9wX7Km8j3N2O5%2BRakwrF50%2F4CP87IB8FO   qQZH9RsM6htIo0SVQNkPSV3Cw%2BP8gsEbJ11tvKGjaUvC1WROB8YGHRalmwHzeTXAgl0nyqxqAgH   00ymKZZ%2FUGMs2kG2zwXN5Msz6vA%2Fe3iIju7WBF1sELyCn04EpmI0ywWaZmO5SiX49F3Fq1%2F   o33UOBh%2BC207iEh%2BKst1vP66KVm0uODeWaSuAbcBd9QVPD0%2BFOzgfUuScwdBdFRnWWL01il   3ShqlyDtdHXyHuo%2FfnxI0nEXLEK7GXv3nCWP3Gq8WqXpH3BBnQ6Nkb9296tC%2FZj7%2FH%2BTn   Nq4sekDPW9MFTuKNRm2dwj3E5%2B%2FjkD2F6EzY6j3GFvmMvyK9zNeXgLZarq3R1SlaGGOf7xwoD   wXzrgMW3VvXKH%2FdTJqk%2FYmu410vlR1SC5XeaajZ%2B3fRlcXnA87fEz5%2FAQ%3D%3D&Relay   State=%2F')
    
            quantity_text = driver.find_element_by_id('userNameInput')
            # student id
            quantity_text.send_keys('')
            quantity_text = driver.find_element_by_id('passwordInput')
            # password
            quantity_text.send_keys('')
            checkbox = driver.find_element_by_id('submitButton')
            checkbox.click()
    
            # need to edit the references
            time.sleep(1)
            forms = driver.find_elements_by_class_name('bookly-form-group')
    
            select_1 =  Select(forms[0].find_element_by_tag_name('div').find_element_by_tag_name('select'))
            select_2 =  Select(forms[1].find_element_by_tag_name('div').find_element_by_tag_name('select'))
    
            # icl
            select_1.select_by_value('1')
    
            #morning slot
            # select_2.select_by_value('33')
    
            # evening slot
            select_2.select_by_value('33')
            # forms[1].find_element_by_tag_name('div').click()
    
            next_button= driver.find_element_by_class_name('bookly-right')# bookly-mobile-next- step.bookly-js-mobile-next-step.bookly-btn.bookly-none.ladda-button')
    
            time.sleep(3)
            
            # need to check that these coordinates are on the next button its a hack but ok i guess
            pyautogui.moveTo(1181, 548)
            pyautogui.click()
    
            time.sleep(3)
    
            buttons = driver.find_element_by_class_name('bookly-column.bookly-column-wide.bookly-js-    first-column')
            all_buttons = buttons.find_elements_by_tag_name('button')
            time.sleep(5)
            #
            ## could iterate over all buttons - but i think the first one is fine
            all_buttons[-1].click()
            time.sleep(3)
    
            # need to check that these coordinates are on the next button its a hack but ok i guess
            # again
            pyautogui.moveTo(1181, 648)
            pyautogui.click()
    
            break
        
        except Exception:
                pass    

time.sleep(5)
driver.close()
driver.quit()

# driver.find_elements_by_xpath('//*[@id="bookly-form-5fc681212cda0"]/div[2]/div[2]/div[2]/div/button')

#driver.find_element_by_name('Select a Location')

#elements = driver.find_elements_by_tag_name('form')

#submit = driver.find_element_by_id('submit')
#submit.click()

