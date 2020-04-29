from selenium import webdriver
import time
import math


try:
    link = " http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".form-group>.container>button.trollface")
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(10)
    browser.quit()