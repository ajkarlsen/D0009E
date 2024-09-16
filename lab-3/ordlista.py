def insert_2list():
    word = input("Word to insert: ")
    definition = input("Description of word: ")
    list_words.append(word)
    list_def.append(definition)

def lookup_2list():
    word = input("Word to lookup: ").lower()
    if word in list_words:
        print(f'{list_words[list_words.index(word)]}: {list_def[list_words.index(word)]}')
    else: print("Word not in list")

list_words = ["banan", "substantiv", "fotboll"]
list_def = ["gul suspekt frukt", "namn på ting till exempel boll och ring", "sfär som man sparkar på"]

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
            insert_2list()
        elif choice == "2":
            lookup_2list()
        else: 
            print("Invalid input")



main()

