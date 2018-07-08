from tasktimer import call_repeatedly

liste = [
    "toto",
    "titi"
]

# fonction appelÃ©e pÃ©riodiquement
def urlcall(toBeProcessed):
    if toBeProcessed["elements"]:
        for i in range(len(toBeProcessed["elements"])):
            call = toBeProcessed["elements"].pop(i)

        return False
    else:
        return True

# mise en route d'un appel toutes les 5s de la fonction urlcall avec un dictionnaire
# qui contient les paramÃ¨tres passÃ©s Ã  chaque appel de la fonction
call_repeatedly(5, urlcall, { "elements": liste })
