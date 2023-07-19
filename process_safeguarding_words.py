import os
import subprocess
import sys
# sys.path.append('C:/Users/edmun/Code/parenttext-pipeline/src/parenttext_pipeline')
# from extract_keywords import process_keywords
# leave in place for now, above code enables quick local testing

from parenttext_pipeline.extract_keywords import process_keywords
from config import *

def main():

    sources = [
        {"key": "zul", "path": "./excel_files/safeguarding zulu.xlsx"},
        {"key": "swa", "path": "./excel_files/safeguarding swati.xlsx"}
    ]

    output = "./edits"
 
    process_keywords(sources, output)
    
if __name__ == '__main__':    
    main()

