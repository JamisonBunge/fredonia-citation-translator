import pandas as pd
import os
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from endnote import EndnoteRow, EndNoteEntry, rowsToEntrys, endnote,translate
from googletrans import Translator


ff_options = webdriver.FirefoxOptions()


def scrapy(term):

    res = ""
    err = False

    try:
        service = Service(executable_path="./geckodriver")
        driver = webdriver.Firefox(service=service)

        driver.get('https://cnki.net/kns/defaultresult/index')
        # Navigate to the search page and enter the search term
        print("Nav and search on homepage")
        search_box = driver.find_element(By.XPATH, "//*[@id='txt_search']")
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)

        #notice_popup = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/a")
        #notice_popup.click()



        # search_button = driver.find_element(By.ID,"search")
        # print(search_button)
        # search_button.click()

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
        print("Nav Export Menu 1 - Batch Box")
        batch_ops = driver.find_element(By.XPATH, '//*[@id="batchOpsBox"]')
        batch_ops_hover =  webdriver.ActionChains(driver).move_to_element(batch_ops)
        batch_ops_hover.perform()
        time.sleep(2)

        print("Nav Export Menu 2 - First Menu")
        export_docs = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/ul[1]/li/ul/li[1]')
        nextHover =  webdriver.ActionChains(driver).move_to_element(export_docs)
        nextHover.perform()
        time.sleep(2)

        print("Nav Export Menu 3 - Export Menu Step in ")
        endnote_dropdown = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/ul[1]/li/ul/li[1]/ul/li[1]')
        ennote_dropdown_hover = webdriver.ActionChains(driver).move_to_element(endnote_dropdown)
        ennote_dropdown_hover.perform()
        time.sleep(2)

        # endnote_dropdown.click()

        print("Nav Export Menu 3 - Click EndNote link ")
        endnote_link = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/ul[1]/li/ul/li[1]/ul/li[8]')
        # ennote_dropdown_hover = webdriver.ActionChains(driver).move_to_element(endnote_dropdown)
        # ennote_dropdown_hover.perform()
        time.sleep(2)

        endnote_link.click()
        ###



        # Wait for the export page to load and click the export button
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])  # this is the new tab

        print("sleeping for results to load...")
        time.sleep(20)
        # switch to the next opened ta
        clipboard = driver.find_element(By.XPATH, '//*[@id="result"]/ul')

        print("QUERY: ", term)
        print(clipboard.text)

        res = clipboard.text
        err = False
    except Exception as e:
        print('Error with term: ' + term)
        print(e)
        res = ""
        err = True

    driver.quit()
    #driver.switch_to.window(driver.window_handles[0])


    return res, err

def main():
    # Create Mapping # todo: some sort of struct
    termBlobMap = dict()
    termsSuccessful = dict()

    # Read the CSV file with search terms #todo make this safe
    fn = sys.argv[1]
    if os.path.exists(fn):
        print(os.path.basename(fn))
    termsCVS = pd.read_csv(fn)

    # Scrap the database for each term
    terms = termsCVS["Search"]
    for term in terms:
        blobResult, err = scrapy(term)
        if err == False:
            termBlobMap[term] = blobResult
        termsSuccessful[term] = not err

    # Put into EndNote format & translate content
    allEntrys = dict()
    for term in terms:
        print(f'{term} content scraped: {termsSuccessful[term]}\n')
        if termsSuccessful[term]:


            entrysForTerm = endnote(termBlobMap[term])
            # translate content
            translate(entrysForTerm)
            # group by journal entry
            entrys = rowsToEntrys(entrysForTerm,term)
            print(len(entrys))
            print(entrys)

            allEntrys[term] = entrys


    # write output
    with open('output.txt', 'w') as file:
        for term in allEntrys:
            print(f'\n\nSearch Term "{term}"\n\n')
            file.write(f'\n\nSearch Term "{term}"\n\n')
            for entry in allEntrys[term]:
                print(f"what is this {entry}")
                for i, val in enumerate(entry.native_entry_rows):
                   # comparison works for now but feels hacky; the write code shouldnt have to know about this logic
                    output = ""
                    if val.english_citation_value != val.native_citation_value:
                        output = f'{val.citation_key} {val.english_citation_value} [{val.native_citation_value}]\n'
                    else:
                        output = f'{val.citation_key} {val.native_citation_value}\n'

                    print(output)
                    file.write(output)









# P
if __name__ == "__main__":
    main()
