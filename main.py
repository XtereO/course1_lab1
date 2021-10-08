

import json
import re
from api import (find_summary_symbols_in_file,
                            find_summary_symbols_cut_in_file,
                            find_element_with_key_where_most_symbols,
                            find_value_in_array_with_key_where_most_words)
                            
                            
def main():
    
    
    #CONSTS
    FILE_NAME = 'pockemon_full.json'
    
    
    #Read file
    with open(FILE_NAME, 'r') as file: 
        pockemon_list = json.load(file) 
   
   
    #Generate answers
    summary_symbols = find_summary_symbols_in_file(FILE_NAME) 
    summary_symbols_cut = find_summary_symbols_cut_in_file(FILE_NAME)
    elements_with_largest_description = find_element_with_key_where_most_symbols(pockemon_list,'description')
    abilities_with_largest_words = find_value_in_array_with_key_where_most_words(pockemon_list,'abilities') 


    #Output
    print(f'Summary symbols: {summary_symbols}')
    print(f'Summary symbols without spaces and punctuation marks: {summary_symbols_cut}')
    print(f'Who have a most description: {elements_with_largest_description}')
    print(f'What kind of an abilities most used: {abilities_with_largest_words}')
    
main()
