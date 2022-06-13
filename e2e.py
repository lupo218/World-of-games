from selenium import webdriver
from  selenium.webdriver.common.by import  By


def Check_URL(url):
    my_driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
    my_driver.get(url)
    check = my_driver.find_element(By.XPATH, '/html/body/h1/div')
    return check.text

#
# def Check_resulte(url,min,max):
#

print(Check_URL('http://192.168.0.5/'))