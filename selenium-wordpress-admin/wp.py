#https://ferhatcicek.com/2021/05/29/python-selenium-kullarak-wordpress-admin-paneline-giris/
from selenium import webdriver
import time

browser = webdriver.Firefox()
url = "https://www.wordpresssitsi.com/wp-admin/" 
browser.get(url)  

username = browser.find_element_by_id("user_login") 
password = browser.find_element_by_id("user_pass") 

username.send_keys("k_adi") # wordpress kullanici adi
password.send_keys("k_adi_sifre") # wordpress kullanici adi

submitButton = browser.find_element_by_id("wp-submit") 
submitButton.click()
time.sleep(10)
browser.close()
