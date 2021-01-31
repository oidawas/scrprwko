from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import time

# Initialisation
folder_path = str(Path('./chromedriver').parents[0])

# Navigate to Url
driver = webdriver.Chrome(os.path.join(folder_path, 'chromedriver'))
driver.get("https://firmen.wko.at/-/?branche=23928&branchenname=friseure&firma=")

# Load Page 1
# Agree to Cookies
# Wait 1 sec
agreed = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/p[3]/button')
agreed.click()

# Loop gets all Results of elements of class_name row and writes them in a .txt then switch to next page
# repeat until page 100
for x in range(2, 101, 1):
    results = driver.find_elements(By.CLASS_NAME, 'row')
    with open('op.csv', 'a') as f:
        for entries in results:
            print(entries.text, ";", file=f)
    nextPage_button = driver.find_element(By.LINK_TEXT, str(x))
    nextPage_button.click()
    time.sleep(1)

# Quit Driver
driver.quit()
