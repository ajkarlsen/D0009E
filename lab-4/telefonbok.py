def add_person(name, number, dict):
    dict.update({name: number})

def lookup_person(name, dict):
    if name in dict:
        return dict[name]
    
    for key in dict:
        if isinstance(key, tuple) and name in key:
            return dict[key]
    
    else: return f"{name} not in list"

def alias(name, newname, dict):
    if name in dict:
        dict[(name, newname)] = dict[name]
        del dict[name]
    else: print(f"{name} not in list")
    
def change_num():
    pass

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
                print(phone_book)
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
            change_num()
            
        elif user_inp[0] == "save":
            save()
            
        elif user_inp[0] == "load":
            load()
            
        elif user_inp[0] == "quit":
            break
        
        else: print("Command doesn't exist")
        
main()