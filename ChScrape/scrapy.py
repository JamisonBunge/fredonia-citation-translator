import pandas as pd
import os
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from googletrans import Translator
translator = Translator()
from selenium import webdriver
from selenium.webdriver.edge.service import Service



def scrapy(term):
    try:
        service = Service(executable_path="../geckodriver")

        # options = webdriver.EdgeOptions()
        driver = webdriver.Firefox(service=service)
        driver.get('https://cnki.net/')
        # Navigate to the search page and enter the search term
        print("Nav and search on homepage")
        search_box = driver.find_element(By.XPATH, "//*[@id='txt_SearchText']")
        search_box.send_keys(term)

        notice_popup = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/a")
        notice_popup.click()



        search_button = driver.find_element(By.ID,"search")
        print(search_button)
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
        except:
            pass

        # Click the first checkbox
        checkbox = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[1]/label")
        checkbox.click()

        # Hover over the "Batch Operations" tab and click the "EndNote" dropdown
        print("hover over element")
        batch_ops = driver.find_element(By.XPATH, '//*[@id="batchOpsBox"]')
        hover = webdriver.ActionChains(driver).move_to_element(batch_ops)
        hover.perform()

        print("nav to drop down")
        export_docs = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/ul[1]/li/ul/li[1]')
        hover = webdriver.ActionChains(driver).move_to_element(export_docs)
        hover.perform()
        endnote_dropdown = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/ul[1]/li/ul/li[1]/ul/li[8]")
        endnote_dropdown.click()

        # Wait for the export page to load and click the export button
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])  # this is the new tab

        print("sleeping for results to load...")
        time.sleep(20)
        # switch to the next opened ta
        clipboard = driver.find_element(By.XPATH, '//*[@id="result"]/ul')

        print("QUERY: ", term)
        print(clipboard.text)
        driver.quit()
        return clipboard.txt, False



        #save the csv file
        #df.to_csv('search_results.csv', index=False)
    except Exception as e:
        print('Error with term: ' + term)
        print(e)
        driver.quit()
        return "", True

    # Close the browser





def main():
    # Create Mapping
    termMap = dict()
    termsSuccessful = dict()
    # Read the CSV file with search terms

    #todo make this safe
    fn = sys.argv[1]
    if os.path.exists(fn):
        print(os.path.basename(fn))
    termsCVS = pd.read_csv(fn)

    terms = termsCVS["Search"]
    for term in terms:
        blobResult, err = scrapy(term)
        if err == False:
            termMap[term] = blobResult
        termsSuccessful[term] = not err





    # Read in terms
    print("Hello World!")


# P
if __name__ == "__main__":
    main()
