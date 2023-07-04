import os
import subprocess
import sys
sys.path.append('C:/Users/edmun/Code/parenttext-pipeline')
from rapidpro_flow_tools import flow_converter
from pipelines import process_post_translation
from config import sources, languages

def main():
    #Ideally would like to have this pulling from online repo to avoid need to locally clone
    translation_repo = "../PLH-Digital-Content/translations/parent_text_v2/"
    outputpath = "./output"
    select_phrases = "./edits/select_phrases.json"
    special_words = "./edits/special_words.json"
    add_selectors = "yes"

    process_post_translation(sources, languages, translation_repo, outputpath, select_phrases, special_words, add_selectors)
    
if __name__ == '__main__':    
    main()

