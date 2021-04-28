from app import control

class Calculette: 
    def __init__(self, message='Bonjour à tous'):
        self.welcome = message
        print(self.welcome)

    def make_operation(self, choice, operator):
        list_numbers = Calculette.numbers_caption(choice)
        result = Calculette.calculation(choice, operator)  
        return result

    @classmethod
    def numbers_caption(cls,number): 
        list_numbers = []
        while number.isdigit():
            list_numbers.append(int(number))
            number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
        return list_numbers

    @classmethod
    def calculation(cls,list_numbers,operator):
        for index, list_number in enumerate(list_numbers):   # refactorisation
            if index == 0: # do_something == list elemets types are int not string 
                result = list_number
            else:
                if operator == 'a':
                    result += list_number 
                elif operator == 'd':
                    result = result / list_number
                elif operator == 's':
                    paresult = result - list_numberss
                elif operator == 'm':
                    result *= list_number 
        return result
"""

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
        for index, list_number in enumerate(list_numbers):
            if index == 0:    # modification of i to become list_numbers
                result = list_number
            else:
                result = result - list_number
        # deletion of i incrementation 
        return result
"""


