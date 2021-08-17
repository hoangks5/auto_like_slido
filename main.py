import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import rd;

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
brower = driver
brower.get('https://app.sli.do/event/1iqpm3jg/login')
time.sleep(5)


while True:
    brower.find_element_by_name('mail').send_keys('hacker'+str(random.randint(1,99999))+'@gmail.com')
    brower.find_element_by_name('name').send_keys(rd.name())
    brower.find_element_by_name('consentsGranted').click()
    brower.find_element_by_name('name').send_keys(Keys.ENTER)
    time.sleep(5)
    brower.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div/live/div[2]/div[4]/div[1]/div/div/div[1]/div[3]/div[2]/button').click()
    time.sleep(1)
    brower.find_element_by_xpath('/html/body/div[4]/div/div/div/div/app-header/div/div/div/button/div/div').click()
    time.sleep(1)
    brower.find_element_by_xpath('/html/body/div[1]/sda-action-sheet/div/div/div/div[3]/button').click()
    time.sleep(1)
   