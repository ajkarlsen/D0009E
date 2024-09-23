def insert1(list_words, list_def): #Function that allows user to add word to dictionary. Takes 2 lists in, one with desc and one with word
    word = input("\nWord to insert: ")
    if word in list_words: #Checks if word already is there, if so returns and prints failsafe
        print("Word already in list")
        return
    description = input("Description of word: ") 

    list_words.append(word) #Appends word and description to the 2 lists
    list_def.append(description)

def lookup1(list_words, list_def): #Function which checks for the description of chosen word
    word = input("\nWord to lookup: ")
    if word in list_words: #Checks if the asked for word exists in the dictionary, if not, prints failsafe
        print(f'{list_words[list_words.index(word)]}: {list_def[list_words.index(word)]}') #Finds index of given word and prints it out with its definition
    else: print("Word not in list") #Failsafe if word is not in dictionary

def insert2(list_tuple): #Inserts word into dictionary with list of tuples, Takes in a list of tuples
    word = input("\nWord to insert: ")
    for i in list_tuple: #Checks if the first element of any tuple is the word that wants to be added, if so prints failsafe and return
        if i[0] == word:
            print("Word already in list")
            return
    description = input("Description of word: ") # If word not already in list it appends it as a tuple to the list
    list_tuple.append((word, description))

def lookup2(list_tuple): #Inputs list of tuples, finds the word and description of the word that the user wants to check
    inp = input("\nWord to lookup: ")
    for word, description in list_tuple: #Goes through the list and creates 2 variables for the 2 values
        if word == inp: #Checks if its there
            print(f"{word}: {description}")  
            break   
    else: print("Word not in list\n") #Failsafe if not there
    
def insert3(word_dict): #Function which handles the user input of word and desc and then adds it to dictionary, takes a dictionary
    word = input("\nWord to insert: ")
    if word in word_dict:
        print("Word already in list")
        return
    description = input("Description of word: ")
    word_dict.update({word:description})

def lookup3(word_dict): #Function which asks user for a word to check description for, takes a dictionary
    word = input("\nWord to lookup: ")
    if word in word_dict:
        print(f"{word}: {word_dict[word]}")
    else: print("Word not in list")
    
def main1(): #Main function which outputs the user interface and handles inputs using 2 separate lists
    list_words = []
    list_def = []
    
    print("Menu for dictionary, 2 lists")
    while True:
        print("\n1. Insert")
        print("2. Lookup")
        print("3. Exit program\n")
        choice = input("Choose alternative: ")

        if choice == "3": #Checks the choice of the user, depending of choice runs different functions
            break
        elif choice == "1":
            insert1(list_words, list_def)
        elif choice == "2":
            lookup1(list_words, list_def)
        else: 
            print("Invalid input")

def main2(): #Main function which outputs the user interface and handles inputs using list of tuples
    list_tuple = []
    
    print("Menu for dictionary, list of tuple")
    while True:
        print("\n1. Insert")
        print("2. Lookup")
        print("3. Exit program\n")
        choice = input("Choose alternative: ")

        if choice == "3": #Checks the choice of the user, depending of choice runs different functions
            break
        elif choice == "1":
            insert2(list_tuple)
        elif choice == "2":
            lookup2(list_tuple)
        else: 
            print("Invalid input")
            
def main3(): #Main function which outputs the user interface and handles inputs using dictionary
    word_dict = {}
    
    print("Menu for dictionary, dictionary")
    while True:
        print("\n1. Insert")
        print("2. Lookup")
        print("3. Exit program\n")
        choice = input("Choose alternative: ")

        if choice == "3": #Checks the choice of the user, depending of choice runs different functions
            break
        elif choice == "1":
            insert3(word_dict)
        elif choice == "2":
            lookup3(word_dict)
        else: 
            print("Invalid input")

main1()
main2()
main3()