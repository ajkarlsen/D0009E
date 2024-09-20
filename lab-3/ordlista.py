def insert1(): #Function which allows user to input a word and a definition to be added to the dictionary
    word = input("\nWord to insert: ")
    if word in list_words:
        print("Word already in list\n")
        return
    description = input("Description of word: ") #Saves the word and definition to variables and appends to the lists

    list_words.append(word)
    list_def.append(description)

def lookup1():
    word = input("\nWord to lookup: ")
    if word in list_words:
        print(f'{list_words[list_words.index(word)]}: {list_def[list_words.index(word)]}') #Finds index of given word and prints it out with its definition
    else: print("Word not in list") #Failsafe if word is not in dictionary

def insert2():
    word = input("\nWord to insert: ")
    for i in list_tuple:
        if i[0] == word:
            print("Word already in list\n")
            return
    description = input("Description of word: ")
    list_tuple.append((word, description))

def lookup2():
    inp = input("\nWord to lookup: ")
    for word, description in list_tuple:
        if word == inp:
            print(f"{word}: {description}")  
            break   
    else: print("Word not in list\n")
    
def insert3():
    word = input("\nWord to insert: ")
    if word in word_dict:
        print("Word already in list")
        return
    description = input("Description of word: ")
    word_dict.update({word:description})

def lookup3():
    word = input("\nWord to lookup: ")
    if word in word_dict:
        print(f"{word}: {word_dict[word]}")
    else: print("Word not in list")
    
list_words = []
list_def = []

list_tuple = []

word_dict = {}

def main(): #Main function which outputs the user interface and handles inputs
    print("Menu for dictionary")

    while True:
        print("\n1. Insert")
        print("2. Lookup")
        print("3. Exit program\n")
        choice = input("Choose alternative: ")

        if choice == "3":
            break
        elif choice == "1":
            insert1()
            #insert2()
            #insert3()
        elif choice == "2":
            lookup1()
            #lookup2()
            #lookup3()
        else: 
            print("Invalid input")

main()

