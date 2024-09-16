def insert_2list(): #Function which allows user to input a word and a definition to be added to the dictionary
    word = input("Word to insert: ")
    definition = input("Description of word: ") #Saves the word and definition to variables and appends to the lists
    list_words.append(word)
    list_def.append(definition)

def lookup_2list():
    word = input("Word to lookup: ").lower() 
    if word in list_words:
        print(f'{list_words[list_words.index(word)]}: {list_def[list_words.index(word)]}') #Finds index of given word and prints it out with its definition
    else: print("Word not in list") #Failsafe if word is not in dictionary

list_words = ["banan", "substantiv", "fotboll"]
list_def = ["gul suspekt frukt", "namn på ting till exempel boll och ring", "sfär som man sparkar på"]

def main(): #Main function which outputs the user interface and handles inputs
    while True:
        print("Menu for dictionary\n")
        print("1. Insert")
        print("2. Lookup")
        print("3. Exit program\n")
        choice = input("Choose alternative: ")

        if choice == "3":
            break
        elif choice == "1":
            insert_2list()
        elif choice == "2":
            lookup_2list()
        else: 
            print("Invalid input")



main()

