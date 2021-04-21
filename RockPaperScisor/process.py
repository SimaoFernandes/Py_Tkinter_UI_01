def process(userInput, choice):
    ppt = ['pedra','papel','tesoura']
    if userInput not in ppt:
        return 'Palavra Invalida' 
    if userInput != choice:
        if ppt.index(userInput) - 1 == ppt.index(choice) or (ppt.index(userInput) == 0 and ppt.index(choice) == 2):
            return 'Ganhou'
        if ppt.index(userInput) + 1  == ppt.index(choice) or (ppt.index(userInput) == 2 and ppt.index(choice) == 0):
            return 'Perdeu'
    return 'Empate'