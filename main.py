

import json
import re
from logic import (find_element_with_key_where_most_symbols,
                   find_value_in_array_with_key_where_most_symbols)


#Read file
with open('pockemon_full.json', 'r', encoding='utf-8') as file: 
    pockemon_list = json.load(file) 


#Generate answers
pockemon_list_str = json.dumps(pockemon_list)
summary_symbols = (len(pockemon_list_str))
summary_symbols_cut = len(
    re.sub(r'[,.;:?!-() ]','',pockemon_list_str).replace(' ','')
    )
elements_with_largest_description = find_element_with_key_where_most_symbols(pockemon_list,'description')
abilities_with_largest_symbols = find_value_in_array_with_key_where_most_symbols(pockemon_list,'abilities') 


#Output
print(f'Summary symbols: {summary_symbols}')
print(f'Summary symbols without spaces and punctuation marks: {summary_symbols_cut}')
print(f'Who have a most description: {elements_with_largest_description}')
print(f'What kind of an abilities most used: {abilities_with_largest_symbols}')