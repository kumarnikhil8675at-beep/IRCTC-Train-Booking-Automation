#Before Runing this program you need to run this cmd in win+r
#"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222"
#This program only books the sleeper coach tickets.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_option=webdriver.ChromeOptions()

#--------------Details---------------
Train_name='S KRANTI SUP EX (12393)'
From='PATNA JN. - PNBE'
To='NEW DELHI - NDLS (NEW DELHI)'
Date='03/12/2026'
Username='irctcusername'
Password='irctcpass'
Member=6 # Members in Master List
#-----------------------------------

chrome_option.add_experimental_option(
    "debuggerAddress",
    "127.0.0.1:9222"
)
driver=webdriver.Chrome(options=chrome_option)

driver.get("https://www.irctc.co.in/nget/train-search")


language_select=driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button[2]')
language_select.click()

login=driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[2]/nav/ul/li[2]/a')
login.click()

username=driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[2]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div/div/div[2]/form/div[2]/input')
username.send_keys(Username)

password=driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[2]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div/div/div[2]/form/div[3]/input')
password.send_keys(Password)

password.send_keys(Keys.ENTER)


from_location = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/app-root/app-home/div[2]/div/app-main-page/div/div/div[3]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div/p-autocomplete/span/input")
    )
)

from_location.send_keys(From)
sleep(0.5)
from_location.send_keys(Keys.ENTER)
sleep(1)

to_location=driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[2]/div/app-main-page/div/div/div[3]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[2]/div/p-autocomplete/span/input')
to_location.send_keys(To)
sleep(0.5)
to_location.send_keys(Keys.ENTER)
sleep(1)

date_journey=driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[2]/div/app-main-page/div/div/div[3]/div[2]/div[1]/app-jp-input/div/form/div[3]/div[1]/div/p-calendar/span/input')
date_journey.click()
date_journey.send_keys(Keys.CONTROL,'a')
date_journey.send_keys(Keys.BACKSPACE)
date_journey.send_keys(Date)
date_journey.send_keys(Keys.ENTER)

sleep(2)
list_of_train=driver.find_elements(
    By.CSS_SELECTOR,
    "div.form-group.no-pad.col-xs-12.bull-back.border-all"
)
sleep(0.3)
for a in list_of_train:
    name=a.find_element(By.TAG_NAME,value='strong')
    if Train_name == name.text:
        print("Your train no is found : ",name.text)
        sleeper_class=a.find_element(By.CSS_SELECTOR,value='div.white-back.col-xs-12.ng-star-inserted table td.ng-star-inserted')
        sleeper_class.click()
        sleep(0.5)
        sleeper_class_show=a.find_element(By.CSS_SELECTOR,value='div.ng-star-inserted table tr td.link.ng-star-inserted div.pre-avl')
        sleeper_class_show.click()
        
        sleep(0.5)
        book_button=a.find_element(By.CSS_SELECTOR,value='div.col-xs-12 div span.pull-left span button.btnDefault.train_Search.ng-star-inserted')
        book_button.click()
        break

sleep(1)
print("--Register your details through Master List from you irctc account ---")

for count_no in range(Member):
    book_name=driver.find_element(By.CSS_SELECTOR,value="ul.ui-autocomplete-list > li:first-child")
    book_name.click()
    sleep(0.5)
    if count_no==Member-1:
        break
    book_add_passenger=driver.find_element(By.CSS_SELECTOR,value="div.zeroPadding.pull-left.ng-star-inserted > a")
    book_add_passenger.click()
    sleep(1)
    

print("Everthing is done Now you can Select the payment method and complete you transaction to get you ticket")
print("---End-----")