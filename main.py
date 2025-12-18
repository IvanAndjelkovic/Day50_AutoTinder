from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time 




# Add your credentials at the top of your script
load_dotenv()
ACCOUNT_EMAIL = os.getenv('account_email')
ACCOUNT_PASSWORD = os.getenv('account_password')
URL = os.getenv('url')


# keep Chrome Options open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Create the chrome profile directory path
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")


# Tell your Chrome Driver to use the directory you specified to store a "profile". That way every time you quit Chrome and re-run your Selenium script, it keeps all the preferences and settings from your profile.

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


#driver get
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)




