from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys

def login(username=None, password=None):
    driver = webdriver.Firefox()
    driver.get("http://rivalregions.com")
    time.sleep(2)
    vk_login = driver.find_element_by_xpath("/html/body/div[4]/div[2]/a[3]/div")
    vk_login.click()

    username = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div/div/input[6]")
    username.send_keys("+447546280980")
    password = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div/div/input[7]")
    password.send_keys("123aa321")
    login = driver.find_element_by_xpath('//*[@id="install_allow"]')
    login.click()
    time.sleep(5)

    return driver

def destroy(driver):
    driver.quit()
