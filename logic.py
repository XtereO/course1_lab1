
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


#Main functions
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

def find_value_in_array_with_key_where_most_symbols(list_objects, key):


    #Validation arguments
    if(not(validation_list(list_objects))):
        return 'List value is incorrect'
    if(not(validation_key_list(list_objects,key))):
        return 'Key value is incorrect'
    
    
    
    #Looking for a candidates 
    candidates = ['']
    for a in list_objects:
        for i in a[key]:
            if(len(i) > len(candidates[0])):
                candidates = [i]
            elif(len(i) == len(candidates[0]) and not(i in candidates)):
                candidates.append(i)
    

    #Result
    return candidates
