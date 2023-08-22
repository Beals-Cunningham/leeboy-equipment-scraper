from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

service = Service(executable_path=os.path.join(os.getcwd(), 'flask', 'sel', 'chromedriver'))

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, service=service)