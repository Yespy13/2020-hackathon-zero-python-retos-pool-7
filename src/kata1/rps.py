from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    mensaje = ""
    if(player.lower() == "papel"):
        if(ai.lower() == "piedra"):
            mensaje = "Ganaste!"
        elif(ai.lower() == "papel"):
            mensaje = "Empate!"
        elif(ai.lower() == "tijeras"):
            mensaje = "Perdiste!"
    elif(player.lower() == "piedra"):
        if(ai.lower() == "piedra"):
            mensaje = "Empate!"
        elif(ai.lower() == "papel"):
            mensaje = "Perdiste!"
        elif(ai.lower() == "tijeras"):
            mensaje = "Ganaste!"
    elif(player.lower() == "tijeras"):
        if(ai.lower() == "piedra"):
            mensaje = "Perdiste!"
        elif(ai.lower() == "papel"):
            mensaje = "Ganaste!"
        elif(ai.lower() == "tijeras"):
            mensaje = "Empate!"
    return mensaje

def playerChoice():
    return input("Piedra, papel o tijera: ")

def aiChoice():
    aiChoice = randint (1, 3)
    if(aiChoice == 1):
        return "Piedra"
    elif(aiChoice == 2):
        return "Papel"
    elif(aiChoice == 3):
        return "Tijeras"

# Entry Point
def Game():
    player = playerChoice()
    ai = aiChoice()
    
    winner = quienGana(player, ai)

    print("Elección jugador: " + player)
    print("Elección ai: " + ai)

    print(winner)