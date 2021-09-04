from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_browser(browser):
    driver = None
    if browser.lower() == "chrome":
        chrome_driver_location = "chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver_location)
    elif browser.lower() == "firefox":
        firefox_driver_location = "geckodriver.exe"
        driver = webdriver.Firefox(executable_path=firefox_driver_location)   
    else:
        print("Browser not supported. Suggested values are [Chrome,Firefox]")
    return driver


