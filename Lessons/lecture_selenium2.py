# Executing JS Snippets
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pickle

service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com/")

driver.execute_script('console.log(document.getElementById("SIvCob").innerHTML)')
# This works on an old web version of Google.
