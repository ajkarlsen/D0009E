def add_person(name, number, dict):
    if check_if_exist(dict, name, number):
        print("duplicate name or number")
        return 
    dict.update({name: number})

def lookup_person(name, dict):
    if name in dict:
        return dict[name]
    
    for key in dict:
        if isinstance(key, tuple) and name in key:
            return dict[key]
    
    else: return f"{name} not in list"

def alias(name, newname, dict):
    if check_if_exist(dict, newname):
        print("duplicate name or number")
        return 
    
    if name in dict:
        dict[(name, newname)] = dict[name]
        del dict[name]
        return
    for key in dict:
        if isinstance(key, tuple) and name in key:
            newKey = key + (newname,)
            dict[newKey] = dict[key]
            del dict[key]
            return
    else: print(f"{name} not in list")
    
def change_num(name, number, dict):
    if check_if_exist(dict, name, number):
        print("duplicate name or number")
        return 
    else:
        if name in dict:
            return dict.update({name: number})
        for key in dict:
            if isinstance(key, tuple) and name in key:
                return dict.update({key: number})
        else: print(f"{name} not in list")

def check_if_exist(dict, name="&", number="&"):
    if number in dict.values():
        return True
    elif name in dict.keys():
        return True
    
    for key in dict:
        if isinstance(key, tuple) and name in key:
            return True
    else: return False

def save():
    pass

def load():
    pass

def main():
    
    phone_book = {}
    
    while True:
        
        user_inp = input("phonebook> ").split()
        
        if user_inp[0] == "add":
            if len(user_inp) == 3:
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
            save()
            
        elif user_inp[0] == "load":
            load()
            
        elif user_inp[0] == "quit":
            break
        
        else: print("Command doesn't exist")
        
main()