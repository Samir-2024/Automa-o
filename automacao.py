import speech_recognition as sr
import pywhatkit

# Inicializar o reconhecedor de fala
rec = sr.Recognizer()
while True:
    decisao = input("Deseja Continuar [s] ou [n]: ")
    
    if decisao == 'n':
        break
    
    if decisao == 's':
        print("Pode falar:")
        with sr.Microphone() as mic:
            audio = rec.listen(mic)
            try:
                t1 = rec.recognize_google(audio, language="pt-BR")
                print("Você disse: " + t1)
            except sr.UnknownValueError:
                print("Não consegui entender o que foi dito")

            except sr.RequestError:
                print("Erro ao se comunicar com o serviço de reconhecimento de fala")

            if 'tocar música' in t1 :
                print("Qual música você quer ouvir?")
                try:
                    audio1 = rec.listen(mic)
                    t2 = rec.recognize_google(audio1, language="pt-BR")
                    print("Tocando:", t2)
                    pywhatkit.playonyt(t2)
            
                except sr.UnknownValueError:
                    print("Não consegui entender o que você disse")

            if 'Enviar mensagem' in t1 or 'mensagem' in t1:
                from datetimee import enviar_mensagem_user
        
            else:
                pass
