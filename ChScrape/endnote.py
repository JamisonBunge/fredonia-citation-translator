# Define classes and functions
from typing import List
import re

class EndnoteRow:
    def __init__(self, citation_key: str, citation_value: str):
        self.citation_key = citation_key
        self.citation_value = citation_value

class EndNoteEntry:
    def __init__(self, endNoteRows: List[EndnoteRow]):
        self.native_entry_rows = endNoteRows
        self.english_entry_rows = list()
        self.was_translated = False


def rowsToEntrys(endNoteRows: List[EndnoteRow]):

    entrys = list()
    start = 0
    for i, row in enumerate(endNoteRows):
        if row.citation_key=="%0" and i != 0:
            e = endNoteRows[start:i]
            print(f'subentry: {start}:{i}')
            entry = EndNoteEntry(e)
            start = i
            entrys.append(entry)

    return entrys

def endnote(blob):

    lines = blob.splitlines()
    endNotes = list()

    for line in lines:
        print(f'line {line}\n')
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

            print("Letter part:", letter_part)
            print("Rest part:", rest_part)
        else:
            print("No match found")

    entrys = rowsToEntrys(endNotes)
    print(len(entrys))
    print("try printing as endnotes")
    print(entrys)
    return entrys
