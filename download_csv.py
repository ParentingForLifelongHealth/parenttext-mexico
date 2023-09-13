import os
import subprocess
import sys
# sys.path.append('C:/Users/edmun/Code/parenttext-pipeline/src/parenttext_pipeline')
# from pipelines import run_pipeline
# leave in place for now, above code enables quick local testing

from parenttext_pipeline.google_csv_convertor import google_sheets_as_csv
from config import sources

def main():

    output_folder = "./csv_inputs"

    for source in sources:

        #Dowload all content to csv
        sheet_ids = source["spreadsheet_ids"]    
    
        google_sheets_as_csv(sheet_ids, output_folder)
    
if __name__ == '__main__':    
    main()

