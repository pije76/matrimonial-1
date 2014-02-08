from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
import time
import os


#Read username and password
if not os.path.exists("secure/.login"):
    raise "Login details not found"

with open("secure/.login") as fin:
    exec("login=%s"%(fin.read().strip()))

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.shaadi.com")

# the page is ajaxy so the title is originally this:
print driver.title

login_arrow = driver.find_element_by_id('login_box_arrow')
login_arrow.click()

login_id = driver.find_element_by_id('login')
login_pass = driver.find_element_by_id('password')

login_id.send_keys(login['id'])
login_pass.send_keys(login['pass'])

submit = driver.find_element_by_class_name("pos_act_btn_green_med")
submit.submit()



