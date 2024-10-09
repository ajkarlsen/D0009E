def add_person(name, number, dict): #Adds new name and number
    if check_if_exist(dict, name, number): #Checks if already exists
        print("duplicate name or number")
        return 
    dict.update({name: number})

def lookup_person(name, dict): #Looksup person in dictionary
    if name in dict:
        return dict[name]
    
    for key in dict: #For loop which handles if the key is a tuple
        if isinstance(key, tuple) and name in key:
            return dict[key]
    
    else: return f"{name} not in list"

def alias(name, newname, dict): #Takes a name and a new name and gives the person both names
    if check_if_exist(dict, newname): 
        print("duplicate name or number")
        return 
    
    if name in dict: #Makes a new dictionary object with a tuple as key, removes previous object
        dict[(name, newname)] = dict[name]
        del dict[name]
        return
    for key in dict: #Adds the previous dict object with a tuple of the new alias, cant append to tuple
        if isinstance(key, tuple) and name in key:
            newKey = key + (newname,)
            dict[newKey] = dict[key]
            del dict[key]
            return
    else: print(f"{name} not in list")
    
def change_num(name, number, dict): #Inputs name, number and the dictionary. Updates the dictionary with a new value for the given key
    if number in dict.values():
        print("duplicate name or number")
        return
    
    if name in dict:
        return dict.update({name: number})
    
    for key in dict: #Checks if key is tuple then updates that tuple with new value
        if isinstance(key, tuple) and name in key:
            return dict.update({key: number})
    else: print(f"{name} not in list")

def check_if_exist(dict, name="&", number="&"): #Function which checks if a key or value already exists in the dictionary. Returns True if it does
    if number in dict.values():
        return True
    elif name in dict.keys():
        return True
    
    for key in dict:
        if isinstance(key, tuple) and name in key:
            return True
    else: return False

def save(filename, dict): #Types the dictionary to a file with a given filename
    try: 
        file = open(filename, "w")
        for key in dict:
            if isinstance(key, tuple): #If it has alias it types them out too
                file.write(f"{dict[key]};{";".join(key)};\n")
            else:
                file.write(f"{dict[key]};{key};\n")
                
    except: print("no such file")
        
def load(filename, dict): #Loads the dictionary with the file content. 
    try:
        file = open(filename, "r")
        line_list = file.read().splitlines() 
        for line in line_list: 
            element = line.split(";")
            element.pop() #Pop to remove last whitespace
            value = element.pop(0) #Pops out the value fro the list
            if len(element) > 1: #If tuples then tuple the remainder of the list and give as key
                dict.update({tuple(element): value}) 
            else: 
                dict.update({element.pop(): value})
        return dict
    except: print("no such file")
    
def main(): #Main function which handles users commands, declares the dictionary and filename
    
    phone_book = {}
    
    while True:
        
        user_inp = input("phonebook> ").split()
        
        try: #Handles incase the user inputs something that cant be split
            
            if user_inp[0] == "add": 
                if len(user_inp) == 3: #Checks so that the command is the correct length
                    add_person((user_inp[1]), user_inp[2], phone_book)
                else:
                    print("Incorrect input")
                    
            elif user_inp[0] == "lookup":
                if len(user_inp) == 2:
                    print(lookup_person(user_inp[1], phone_book))
                else: print("Incorrect input")
                
            elif user_inp[0] == "alias":
                if len(user_inp) == 3:
                    alias(user_inp[1], user_inp[2], phone_book)
                else: print("Incorrect input")
            
            elif user_inp[0] == "change":
                if len(user_inp) == 3:
                    change_num(user_inp[1], user_inp[2], phone_book)
                
            elif user_inp[0] == "save":
                if len(user_inp) == 2:
                    save(user_inp[1], phone_book)
                else: print("Incorrect input")
                
            elif user_inp[0] == "load":
                
                if len(user_inp) == 2:
                    phone_book = load(user_inp[1], phone_book)
                else: print("Incorrect input")
                
            elif user_inp[0] == "quit":
                break
            
            else: print("Command doesn't exist")
        
        except: 
            print("Invalid input")
        
main()