# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.conestogac.on.ca/")

virtual_tour = driver.find_element("xpath","/html/body/div[3]/div[3]/div[2]/div/div/div[2]/div/a[1]")
virtual_tour.click()
time.sleep(5)

waterloo_start = driver.find_element("xpath","/html/body/div/div/div/div/div[3]/div[1]/div[3]/ul/li[3]/div/div/div/div[1]/div/div[2]/button/span")
waterloo_start.click()
time.sleep(5)

got_it = driver.find_element("xpath","/html/body/div/div/div/main/div[3]/div[2]/div/div/div[1]/div/div/div/div/button")
got_it.click()
time.sleep(5)

got_it_2 = driver.find_element("xpath","/html/body/div/div/div/main/div[3]/div[2]/div/div/div[2]/div/div/div/div/button")
got_it_2.click()
time.sleep(5)

start = driver.find_element("xpath","/html/body/div/div/div/main/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/button")
start.click()
time.sleep(5)

cancle = driver.find_element("xpath","/html/body/div/div/div/main/div[1]/div/div/button")
cancle.click()
time.sleep(5)

book_tour = driver.find_element("xpath","/html/body/div/div/div/main/div[3]/div[1]/div[2]/button[2]")
book_tour.click()
time.sleep(5)

# Closing the webdriver
driver.close()
