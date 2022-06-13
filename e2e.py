import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_scores_service(url,xpt):
    ## Setup chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")

    # Set path to chromedriver as per your configuration
    webdriver_service = Service("/usr/bin/chromedriver")

    # Choose Chrome Browser
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Get page
    browser.get(url)

    # Extract description from page and print
    description = browser.find_element(By.XPATH, xpt)
    result =None
    result = description.text

    #Wait for 10 seconds
    time.sleep(2)
    browser.quit()
    return result

def main_function(url,xpt):
    result = test_scores_service(url,xpt)
    if int(result) >1 and int(result)< 1000:
        return True
    else:
        return False



result = test_scores_service("http://192.168.0.5/",'/html/body/h1/div')
print(result)