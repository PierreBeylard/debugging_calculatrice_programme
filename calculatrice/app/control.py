from app import calculatrice
from app import view


def start_programm(message='Bienvenue'):
    calculette=calculatrice.Calculette(message="C'est un programme orienté objet")
    view.display_interface(calculette)

def make_operation(choice,operator,calculette): 
    result= calculatrice.numbers_caption(choice,operator)
    return result 
    
def ask_user(message=''):
    response = view.ask_user(message)
    return response
