import os
import subprocess
import sys

from parenttext_pipeline.extract_keywords import process_keywords_to_file
from config import *

def main():

    # Make sure the 3 letter code here aligns with the languages specified in the config file otherwise the safeguarding process will not work properly
    sources = [
        {"key": "zul", "path": "./excel_files/safeguarding zulu.xlsx"},
        {"key": "ssw", "path": "./excel_files/safeguarding swati.xlsx"}
    ]

    output = "./edits"
 
    process_keywords_to_file(sources, output)
    
if __name__ == '__main__':    
    main()

