def insert():
    pass

def lookup():
    pass

def main():
    while True:
        print("Menu for dictionary\n")
        print("1. Insert")
        print("2. Lookup")
        print("3. Exit program\n")
        choice = input("Choose alternative: ")

        if choice == "3":
            break
        elif choice == "1":
            insert()
        elif choice == "":
            lookup()
        else: 
            print("Invalid input")

main()