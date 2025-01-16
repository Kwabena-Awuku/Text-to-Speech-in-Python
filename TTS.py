import PySimpleGUI as sg
import pyttsx3
speaker = pyttsx3.init()

layout = [
    [sg.Input(key = 'INPUT'), sg.Button('Speak', key= 'Speak_BTN')],
   
]

window = sg.Window('Kasa Ma ME', layout=layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == "Speak_BTN":
        data = values['INPUT']
        speaker.say(data)
        speaker.runAndWait()
window.close()
