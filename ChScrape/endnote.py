# Define classes and functions
from typing import List
from googletrans import Translator
import re

# todo: docouple translation

class EndnoteRow:
    def __init__(self, citation_key: str, citation_value: str):
        self.citation_key = citation_key
        self.native_citation_value = citation_value
        self.english_citation_value = ""
        self.was_translated = False
        self.combined_citation_value = ""

class EndNoteEntry:
    def __init__(self, term: str):

        self.native_search_term = term
        translator = Translator()
        res = translator.translate(term)
        self.english_search_term = res.text

        self.english_entry_rows = list()



    def __init__(self, endNoteRows: List[EndnoteRow],term: str):
        self.native_entry_rows = endNoteRows
        self.english_entry_rows = list()


def translate(endNoteRows: List[EndnoteRow]):
    translator = Translator()
    print(translator)

    for i, row in enumerate(endNoteRows):
        print(f' to translate: {row.native_citation_value}')
        res = translator.translate(row.native_citation_value)
        row.english_citation_value = res.text
        print(f't:{res.text}')



 # ([]EndnoteRow, term ) -> []EndnoteEntry
def rowsToEntrys(endNoteRows: List[EndnoteRow],term: str):

    entrys = list()
    start = 0
    for i, row in enumerate(endNoteRows):
        if row.citation_key=="%0" and i != 0:
            e = endNoteRows[start:i]
            print(f'Entry indexs: {start}:{i}')
            entry = EndNoteEntry(e,term)
            start = i
            entrys.append(entry)

    return entrys

# (blob: endnote_scraped) -> []EndnoteRow
def endnote(blob):

    lines = blob.splitlines()
    endNotes = list()

    for line in lines:
        # Define the regular expression pattern
        pattern = r'^(%\w+)\s*(.*)$'
        # Use re.match() to find the matches
        match = re.match(pattern, line)

        if match:
            # Extract the parts
            letter_part = match.group(1)
            rest_part = match.group(2)

            row = EndnoteRow(letter_part,rest_part)
            endNotes.append(row)

            #print("Letter part:", letter_part)
            #print("Rest part:", rest_part)
        else:
            print(f'line {line}\n')
            print("No match found")

    return endNotes
