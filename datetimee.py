import pywhatkit as pk
import datetime

with open("PyWhatKit_DB.txt", "r") as file:
    texto = file.read()
    print(texto)

def enviar_mensagem_user(contato, msg, horas, minutos):
    pk.sendwhatmsg(contato, msg,horas, minutos + 1)
    return enviar_mensagem_user

def enviar_mensagem_group(contato, msg, horas, minutos):
    pk.sendwhatmsg_to_group(contato, msg ,horas, minutos)
    return enviar_mensagem_group


opcao = input("Deseja enviar uma mensagem [s] ou [n]: ")

if opcao == 's':
    contato = input("Qual o número ou grupo deseja enviar: ")
    msg = input("Qual mensagem deseja enviar: ")
    horas = int(input("Informe as horas: "))
    minutos = int(input("Informe os minutos: "))

    lista_contato = (enumerate(contato))
        
    if contato == ("+55"):
        enviar_mensagem_user(contato, msg,horas, minutos + 1)

    elif contato != ("+55"):
        enviar_mensagem_group(contato, msg, horas, minutos + 1)
        
if opcao == 'n':
    pass