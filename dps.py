import time

from  selenium import webdriver
from selenium.webdriver.common.by import By

from sadikshya.impdoc import thisdict

driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(thisdict["url"])
driver.maximize_window()
#           xpath for sign up page
username= "//*[@id='username-25046']"
password="//*[@id='user_password-25046']"
login="//input[@value='Login']"

# hi=driver.find_element(By.XPATH,"//*[@id='um-submit-btn']")
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)"),
# driver.find_element(By.XPATH,login).click()
# time.sleep(5)
def send_keysfunc(path,message):
    {
        driver.find_element(By.XPATH,path).send_keys(message)
    }

def clickfun(path):
        {
            driver.find_element(By.XPATH,path).click()
        }
def empty_data():
    {
        clickfun(login),
        time.sleep(3),
    }
# def valid_data():
#     {
#         send_keysfunc(username,"sadi00"),
#         send_keysfunc(password,"abc@1234"),
#
#
#         clickfun(login),
#     }
# def invalid_data():
#     {
#        send_keysfunc(username,"welcome"),
#        send_keysfunc(password,"welcome"),
#        clickfun(login)
#     }
# # valid_data()
empty_data()
#
