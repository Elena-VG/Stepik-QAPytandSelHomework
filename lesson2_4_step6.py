from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")
browser.find_element_by_id("button")
time.sleep(10)
browser.quit()
