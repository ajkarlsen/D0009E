def add_person(name, number, dict):
    dict.update({name: number})

def lookup_person():
    pass

def alias():
    pass

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
                add_person(user_inp[1], user_inp[2], phone_book)
                print(phone_book)
            else:
                print("Incorrect input")
                
        elif user_inp[0] == "lookup":
            lookup_person()
            
        elif user_inp[0] == "alias":
            alias()
            
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