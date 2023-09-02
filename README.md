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
This project is a fork from a Fiverr commission by [Gary](email)

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
