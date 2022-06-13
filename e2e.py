"""
# Filename: run_selenium.py
"""

## Run selenium and chrome driver to scrape data from cloudbytes.dev
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
webdriver_service = Service("/usr/bin/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Get page
browser.get("http://192.168.0.5/")

# Extract description from page and print
description = browser.find_element(By.XPATH, '/html/body/h1/div')
print(f"{description.text}")

#Wait for 10 seconds
time.sleep(10)
browser.quit()