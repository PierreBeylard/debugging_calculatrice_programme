def ask_user(sentence = "Saisir un chiffre"): # do_something == modification of function name
    choice = input(f"{sentence}\n>")
    return choice

def addition(number): # do_something== correction of function name
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
    result = sum(list_numbers) # do_something ==  sum function to return the sum of list items
    return result

def multplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number)) # do_something=== modification of the type of variable 'number' 
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
    for index, list_number in enumerate(list_numbers):   # refactorisation
        if index == 0: # do_something == list elemets types are int not string 
            result = list_number
        else:
            result *= list_number # do_something == we multiply result by the new list_number item
    return result

def division(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(number) # do_something
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == 0:
            result = list_number
        else:
            result = result + list_number # do_something
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit(): # do_something == refactoring possible ici 
        if number.isdigit():
            list_numbers.append(int(number)) # do_something== modification of variable type
        number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
    result = 0    # modification of i to become result
    for list_number in list_numbers:
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
            choice = ask_user("Saisir un ciffre à ADDITIONNER ou clicker sur '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un ciffre à SOUSTRAIRE ou clicker sur '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = ask_user("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = multplication(choice)
        elif choice == 4:
            choice = ask_user("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = division(choice)
        else: 
            print('il y a une erreur dans le choix du chiffre')
        return print(f"Le resultat est ==> {result}")


