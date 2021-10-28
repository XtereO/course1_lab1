import re


# Validators
def is_empy_list(input_list):
    return False if input_list and isinstance(input_list, list) else True

def is_empy_value(value):
    if isinstance(value, (int, float)):
        return False
    elif value:
        if isinstance(value, str) and not value.isspace():
            return False
        elif isinstance(value, list):
            if '' in [str(i).strip() for i in value]:
                return  False
        elif isinstance(value, dict):
            return False
        return True
    else:
        return True

# Main functions
def find_summary_symbols_in_file(file):
       
     
    # Read file and generate answer
    summary_symbols = 0
    for a in file: summary_symbols+=len(a)
    
    
    # Result
    return summary_symbols

def find_summary_symbols_cut_in_file(file):
    
    
    # Generate answer and close file
    summary_symbols_cut = 0
    for a in file: 
        summary_symbols_cut+=len(
            re.sub(r'[,.;:?!-()]','',a).replace(' ','').replace('[','').replace(']','').replace('"','').strip()
        )
        
    
    # Result
    return summary_symbols_cut

def find_element_with_key_where_most_symbols(list_objects, key):


    # Validation arguments
    if is_empy_list(list_objects):
        return 'List value is incorrect'
    
    
    # Looking for candidates 
    candidates = [list_objects[0]]
    for a in list_objects[1:]:
        if len(a[key]) > len(candidates[0][key]):
            candidates = [a]
        elif (len(a[key]) == len(candidates[0][key]) and not(a in candidates)):
            candidates.append(a)
    

    # Result
    return candidates

def find_value_in_array_with_key_where_most_words(list_objects, key):


    # Validation arguments
    if(is_empy_list(list_objects)):
        return 'List value is incorrect'


    # Looking for a candidates
    candidates = set()
    max_current = 0
    for pokemon in list_objects:
        for param in pokemon[key]:
            amount_word = len(param.split())
            if amount_word > max_current:
                max_current = amount_word
                candidates.clear()
                candidates.add(param)
            elif amount_word == max_current:
                candidates.add(param)


    # Result
    return candidates
