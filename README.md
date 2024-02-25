# fredonia-citation-translator

## Table Of Contents
- todo
## Prerequisites
todo
//add pyenv, required python version, virtualenv, etc

## Running Locally

`pip install -r requirements.txt`

## Project History
-todo
<<<<<<< HEAD
<<<<<<< HEAD
This project is a fork from a Fiverr commission by [Gary](email)
=======
This project is a fork from a Fivver commission done by [Gary](email)
>>>>>>> eceff1f (add author place holder)
=======
This project is a fork from a Fiverr commission by [Gary](email)
>>>>>>> 32a23da (quick fix)

### Orinigal Scraper Program README

This document provides instructions for using the Scraper Program.

Prerequisites

Before using the Scraper Program, make sure to follow these prerequisites:

Write your search terms to a CSV file with the column header as "Search" (capital S).
Ensure that each search term is entered as a separate row in the CSV file, as the site being scraped does not recognize multiple search terms.
Save the CSV file in the same folder as the Scraper Program, and save it as a comma-delimited file (CSV).
Usage

To use the Scraper Program, follow these steps:

Run the Scraper Program. You can do this by running on the terminal python path/to/scrapy.py. “Path to scrapy.py” eg python “D:MyFolder/scrapy.py”.
The program will navigate to the search page and enter each search term from the CSV file, one by one.
If a search term returns no results, the program will skip to the next search term.
If an error occurs during the program's execution, it will be saved to a file called "debug.txt".
If a search term returns no results, it will be saved to a file called "log.txt".
For each search term that returns results, the program will select the first result and export it as an EndNote file.
The EndNote file will be saved as "searchterm.txt" and a translated version will be saved as "searchterm_en.txt", where "searchterm" is the original search term.
The program will repeat steps 2-7 for each search term in the CSV file.
Customization

The Scraper Program can be customized to suit your needs as different requirements arise. Please contact us for any customization requests.

You will notice I am attaching a requirement.txt file. This is a file that contains all the packages you need to run the code. You can install all the packages by running the following command in your terminal:
pip install -r requirements.txt

That will install all the packages you need to run the code.
So, according to the feedback you provided us with, we have made the following changes:
- We are now saving the output to csv file so that you can have the chinese and translated text in the same file.
You mentioned integrating with a database, well csv will make the work lot easier when integrating with a database. You can use the cav to create a database and then use the cav to insert the data into the database. You can also use the cav to create a table in the database. You can find more information about cav here:
- We added print statements to the terminal but you have a log file which you can use to gain insight into results of the code.
- We added a debug file that you can send us so that we can check what is going on with the code. and also add improvements based on the
 use case you would require.
 Have a look at the readme we sent before, for more instructions on how to use the code.
 - You can use this on the terminal or if you want a bit more control in the jupyter notebook. You can find the jupyter notebook in the notebook folder.
 - But i would suggest terminal unless your are comfortable with jupyter notebook.