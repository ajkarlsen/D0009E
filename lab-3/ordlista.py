def insert1(): #Function which allows user to input a word and a definition to be added to the dictionary
    word = input("Word to insert: ")
    description = input("Description of word: ") #Saves the word and definition to variables and appends to the lists
    list_words.append(word)
    list_def.append(description)

def lookup1():
    word = input("Word to lookup: ")
    if word in list_words:
        print(f'{list_words[list_words.index(word)]}: {list_def[list_words.index(word)]}') #Finds index of given word and prints it out with its definition
    else: print("Word not in list") #Failsafe if word is not in dictionary

def insert2():
    word = input("Word to insert: ")
    description = input("Description of word: ")
    list_tuple.append((word, description))

def lookup2():
    inp = input("Word to lookup: ")
    for word, description in list_tuple:
        if word == inp:
            print(f"{word}: {description}")  
            break   
    else: print("Word not in list")
    
def insert3():
    word = input("Word to insert: ")
    description = input("Description of word: ")
    word_dict.update({word:description})

def lookup3():
    word = input("Word to lookup: ")
    if word in word_dict:
        print(f"{word}: {word_dict[word]}")
    else: print("Word not in list")
    
list_words = ["banan", "substantiv", "fotboll"]
list_def = ["gul suspekt frukt", "namn på ting till exempel boll och ring", "sfär som man sparkar på"]

list_tuple = [("banan", "gul suspekt frukt"), ("substantiv", "namn på ting till exempel boll och ring"), ("fotboll", "sfär som man sparkar på")]

word_dict = {"banan":"gul suspekt frukt", "substantiv":"namn på ting till exempel boll och ring", "fotboll":"sfär som man sparkar på"}

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
            #insert1()
            #insert2()
            insert3()
        elif choice == "2":
            #lookup1()
            #lookup2()
            lookup3()
        else: 
            print("Invalid input")



main()

