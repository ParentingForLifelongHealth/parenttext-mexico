import os
import subprocess
import sys
# sys.path.append('C:/Users/edmun/Code/parenttext-pipeline/src/parenttext_pipeline')
# from extract_keywords import process_keywords
# leave in place for now, above code enables quick local testing

from parenttext_pipeline.extract_keywords import process_keywords_to_file
from config import *

def main():

    sources = [
        {"key": "zul", "path": "./excel_files/safeguarding zulu.xlsx"},
        {"key": "ssw", "path": "./excel_files/safeguarding swati.xlsx"}
    ]

    output = "./edits"
 
    process_keywords_to_file(sources, output)
    
if __name__ == '__main__':    
    main()

