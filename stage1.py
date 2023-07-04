import os
import subprocess
import sys
sys.path.append('C:/Users/edmun/Code/parenttext-pipeline')
from rapidpro_flow_tools import flow_converter
from pipelines import prepare_for_translations
from config import sources, ab_testing_sheet_ID

def main():
    outputpath = "./output"
    model = "models.parenttext_models"

    prepare_for_translations(sources, ab_testing_sheet_ID, outputpath, model)
    
if __name__ == '__main__':    
    main()

