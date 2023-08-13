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


for term in df['Search']:
    try:
        driver.get('https://cnki.net/')
        # Navigate to the search page and enter the search term
        search_box = driver.find_element(By.XPATH, "//*[@id='txt_SearchText']")
        search_box.send_keys(term)
        search_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/input[2]")
        search_button.click()

        # Wait for the results page to load
        time.sleep(3)

        # if this xpath is returned //*[@id="gridTable"]/p then there are no results
        # we go to the next term
        # But the new search xpath becomes //*[@id="txt_search"]
        try:
            no_results = driver.find_element(By.XPATH, "//*[@id='gridTable']/p")
            print('No results for term: ' + term)
            # write a new file called log.txt, if it exists append to it
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write('No results for term: ' + term + '\n')
            continue
        except:
            pass
        
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
        """with open(term + '.txt', 'w', encoding='utf-8') as f:
            f.write(clipboard.text)"""
        # Instead we append to the same csv file. so we have search term and the results
        df.loc[df['Search'] == term, 'Chinese'] = clipboard.text
        # Translate the clipboard text to English
        
        term_en = translator.translate(term, dest='en').text
        clipboard_en = translator.translate(clipboard.text, dest='en').text
        """with open(term_en + '.txt', 'w', encoding='utf-8') as f:
            f.write(clipboard_en)"""
        # append the translated results to the same csv file
        df.loc[df['Search'] == term, 'English'] = clipboard_en

        #save the csv file
        df.to_csv('search_results.csv', index=False)
    except Exception as e:
        df.to_csv('search_results.csv', index=False)
        print('Error with term: ' + term)
        print(e)
        with open('debug.txt', 'a', encoding='utf-8') as f:
            if term in f.read():
                continue
            f.write('Error with term: ' + term + '\n')
            f.write(str(e) + '\n')
            f.write("-----------------------" + '\n')
        # go to the next term
        continue

# Close the browser
driver.quit()

