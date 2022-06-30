from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
import ctypes  # An included library with Python install.   
import sys

def clickattempt(xref):
    try:
        driver.find_element_by_xpath(xref).click()
        time.sleep(0.5)
    except:
        pass
    
username = 'xxxxxx@mail.com' #Your e-mail
password = 'xxxxx' #Your password
driver = webdriver.Chrome('C:/chromedriver') #Locate your chromedriver. You can find the source at https://chromedriver.chromium.org/,
#Once you put your chromedriver under C:/, you don't need to manually adjust this path. Otherwise please specify.
driver.get("https://lobby.gladiatus.gameforge.com/tr_TR/")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginRegisterTabs"]/ul/li[1]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/p/button[1]').click()
time.sleep(2)
ref = driver.find_element_by_xpath('/html')
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(ref,400,630) #works only in 1920x1080 ****TODO
action.click()
action.perform()
time.sleep(0.5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(0.5)

while True: #dungeoning loop simply by forcing to click every possible sub-image that are all fight initiators.
    clickattempt('//*[@id="cooldown_bar_dungeon"]/a')
    clickattempt('//*[@id="content"]/div[1]/h3/span[1]')
    for k in range(0,12):
        clickattempt('//*[@id="content"]/div[2]/div/img['+str(k)+']')
    clickattempt('//*[@id="linkLoginBonus"]')
    clickattempt('//*[@id="content"]/div[2]/div/form/table/tbody/tr/td[1]/input')
    clickattempt('//*[@id="content"]/div[2]/div/form/table/tbody/tr/td[1]/input')
    clickattempt('//*[@id="linknotification"]')
    time.sleep(30)
