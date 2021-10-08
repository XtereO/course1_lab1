
#Validators
def validation_list(value):
    if(not(value) or 
       type(value) != type([]) or len(value)==0):
        return False
    return True

def validation_key_list(list_objects, key):
    if(not(key) or 
       type(key) != type('str') or not(key in list_objects[0])):
        return False
    return True

def validation_emty_elements_list(check_list):
    if(type('str')==type(check_list)):
        check_list=check_list.split(' ')
    if(not('' in check_list) and not(' ' in  check_list)):
        return True
    return False


#Main functions
def find_summary_symbols_in_file(file_name):
    
    
    #Validation arguments
    if(type('str')!=type(file_name)):
        return 'File name must be string'
        
     
    #Read file and generate answer
    file = open(file_name, 'r') 
    
    summary_symbols = 0
    for a in file: summary_symbols+=len(a)
    file.close()
    
    
    #Result
    return summary_symbols

def find_summary_symbols_cut_in_file(file_name):
    
    
    #Validation arguments
    if(type('str')!=type(file_name)):
        return 'File name must be string'
        
     
    #Read file and generate answer
    file = open(file_name, 'r') 
    
    summary_symbols_cut = 0
    for a in file: 
        summary_symbols_cut+=len(
            re.sub(r'[,.;:?!-() ]','',a).replace(' ','')
        )
    file.close()
    
    
    #Result
    return summary_symbols_cut

def find_element_with_key_where_most_symbols(list_objects, key):


    #Validation arguments
    if(not(validation_list(list_objects))):
        return 'List value is incorrect'
    if(not(validation_key_list(list_objects,key))):
        return 'Key value is incorrect'
    
    
    #Looking for candidates 
    candidates = [list_objects[0]]
    for a in list_objects[1:]:
        if(len(a[key]) > len(candidates[0][key])):
            candidates = [a]
        elif(len(a[key]) == len(candidates[0][key]) and not(a in candidates)):
            candidates.append(a)
    

    #Result
    return candidates

def find_value_in_array_with_key_where_most_words(list_objects, key):


    #Validation arguments
    if(not(validation_list(list_objects))):
        return 'List value is incorrect'
    if(not(validation_key_list(list_objects,key))):
        return 'Key value is incorrect'
    
    
    
    #Looking for a candidates 
    candidates = ['']
    for a in list_objects:
        for i in a[key]:
            if(len(i.split(' ')) > len(candidates[0].split(' ')) and validation_emty_elements_list(i)):
                candidates = [i]
            elif(len(i.split(' ')) == len(candidates[0].split(' ')) and not(i in candidates) 
                  and validation_emty_elements_list(i)):
                candidates.append(i)
    
    #Result
    return candidates
