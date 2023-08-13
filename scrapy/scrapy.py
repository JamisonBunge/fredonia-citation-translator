import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from googletrans import Translator
translator = Translator()

# Read the CSV file with search terms
df = pd.read_csv('search_terms.csv')

driver = webdriver.Edge()
driver.get('https://cnki.net/')

for term in df['Search']:
    try:
        # Navigate to the search page and enter the search term
        search_box = driver.find_element(By.XPATH, "//*[@id='txt_SearchText']")
        search_box.send_keys(term)
        search_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/input[2]")
        search_button.click()

        # Wait for the results page to load
        time.sleep(3)

        # Click the first checkbox
        checkbox = driver.find_element(By.XPATH, "//*[@id='gridTable']/table/tbody/tr[1]/td[1]/input")
        checkbox.click()

        # Hover over the "Batch Operations" tab and click the "EndNote" dropdown
        batch_ops = driver.find_element(By.XPATH, '//*[@id="batchOpsBox"]/li[2]/a')    
        hover = webdriver.ActionChains(driver).move_to_element(batch_ops)
        hover.perform()
        export_docs = driver.find_element(By.XPATH, '//*[@id="batchOpsBox"]/li[2]/ul/li[1]/a')
        hover = webdriver.ActionChains(driver).move_to_element(export_docs)
        hover.perform()
        endnote_dropdown = driver.find_element(By.XPATH, "//*[@id='batchOpsBox']/li[2]/ul/li[1]/ul/li[9]/a")
        endnote_dropdown.click()

        # Wait for the export page to load and click the export button
        time.sleep(3)

        # switch to the next opened tab
        driver.switch_to.window(driver.window_handles[1])  # this is the new tab
        clipboard = driver.find_element(By.XPATH, '//*[@id="result"]/ul')
        print(clipboard.text)

        # Save to a file as searchterm.txt
        # Save the clipboard text to a file
        with open(term + '.txt', 'w', encoding='utf-8') as f:
            f.write(clipboard.text)

        # Translate the clipboard text to English
        
        term_en = translator.translate(term, dest='en').text
        clipboard_en = translator.translate(clipboard.text, dest='en').text
        # we shall save this as the translated term.txt..where the contents wi;; be the translated clipboard text
        with open(term_en + '.txt', 'w', encoding='utf-8') as f:
            f.write(clipboard_en)
    except:
        print('Error with term: ' + term)
# Close the browser
driver.quit()
