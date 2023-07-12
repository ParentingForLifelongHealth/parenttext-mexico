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
        {"key": "zul", "path": "./excel_files/zul_mod_v2.xlsx"},
        {"key": "sis", "path": "./excel_files/sis_mod_v2.xlsx"}
    ]

    
    process_keywords("./excel_files/sis_mod_v2.xlsx", "./edits/sis_safeguarding.json")
    process_keywords("./excel_files/zul_mod_v2.xlsx", "./edits/zul_safeguarding.json")
    
if __name__ == '__main__':    
    main()

