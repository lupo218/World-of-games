from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--headless')

def Check_URL(url):
    my_driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    my_driver.get(url)
    check = my_driver.find_element(By.XPATH, '/html/body/h1/div')
    return check.text

#
# def Check_resulte(url,min,max):
#

print(Check_URL('http://192.168.0.5/'))