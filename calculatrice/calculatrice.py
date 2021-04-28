def ask_user(sentence = "Saisir un chiffre"): # do_something == modification of function name
    choice = input(f"{sentence}\n>")
    return choice

def numbers_caption (number): 
    list_numbers = []
    while number.isdigit():
        # supression of if condition 
        list_numbers.append(int(number))
        number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
    return list_numbers


def addition(number): # do_something== correction of function name
    list_numbers=numbers_caption(number)
    result = sum(list_numbers) # do_something ==  sum function to return the sum of list items
    return result

def multplication(number):
    list_numbers=numbers_caption(number)
    for index, list_number in enumerate(list_numbers):   # refactorisation
        if index == 0: # do_something == list elemets types are int not string 
            result = list_number
        else:
            result *= list_number # do_something == we multiply result by the new list_number item
    return result

def division(number):
    list_numbers=numbers_caption(number)
    for index, list_number in enumerate(list_numbers): # refactoriser == done
        if index == 0:
            result = list_number
        else:
            result = result / list_number # do_something == operation to apply is a division
    return result

def soustraction(number):
    list_numbers=numbers_caption(number)
    result = 0    # modification of i to become result
    for list_number in list_numbers:
        print(list_number)
        if list_numbers == 0:    # modification of i to become list_numbers
            result = list_number
        else:
            result = result - list_number
    # deletion of i incrementation 
    return result

def display_interface():
    choice = ask_user("""
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4""")
    while choice.isdigit():
        choice = int(choice) # do_something value type must be int
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou clicker sur '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
            result = multplication(choice)
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à DIVISER ou clicker sur '=' ")    # Correction == division in place of multiplication
            result = division(choice)
        else: 
            print('il y a une erreur dans le choix du chiffre')
        return print(f"Le resultat est ==> {result}")


