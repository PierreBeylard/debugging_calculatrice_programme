from app import control

# welcome function 
def ask_user(sentence = "Saisir un chiffre"): 
    choice = input(f"{sentence}\n>")
    return choice


# Interface de séleciton du programme 
def display_interface(calculette):
    choice = ask_user("""
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4""")
    while choice.isdigit():
        choice = int(choice) 
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
            operator="a"
            result = control.make_operation(choice,calculette, operator)
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou clicker sur '=' ")
            operator="s"
            result = control.make_operation(choice,calculette, operator)
        elif choice == 3:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
            operator="m"
            result = control.make_operation(choice,calculette, operator)
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à DIVISER ou clicker sur '=' ")
            operator="d"
            result = control.make_operation(choice,calculette, operator)
        else: 
            choice = ask_user("""
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4""")
            continue
        return print(f"Le resultat est ==> {result}")
