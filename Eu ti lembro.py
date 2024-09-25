#Ja tomou seu gole de VIDA hoje???
import PySimpleGUI as sg
import time

escala_tempo=["","1","10","30","60"]

layout = [
    [sg.P(),sg.T(""),sg.P()],
    [sg.T('Lembrar de:')],
    [sg.I(font=('Any',10,'bold'),size=(43,1),key='lembrete')],       
    [sg.T('Tempo de espera em minutos:')],
    [sg.DD(values=escala_tempo, size=(42,1),key="tempo")],
    [sg.Button("OK", size=(38, 1), button_color=("white", "blue"),  key='-OK-')],
    [sg.P(),sg.T("",key='cronometro'),sg.P()]]

window = sg.Window("EU TI LEMBRO", layout)
while True:
    try:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Sair"):
            break
        elif event in "-OK-":
            msg=values['lembrete'].title()
            tempo=int(values['tempo'])*60
                
            
                
            if tempo> 0:
                
                window.minimize()
                #time.sleep(tempo)  # Espera 30 segundos
                for i in range(tempo, 0, -1):
                    window['cronometro'].update(f'Tempo restante: {i} segundos')
                    window.read(timeout=1000)  # Aguarda 1 segundo entre atualizações
                window['cronometro'].update('Tempo finalizado!')
                window.normal()  # Restaura a janel
                window['cronometro'].update(msg)
            else:
                window['cronometro'].update("Por favor, selecione um tempo válido.")
    except:
        window['cronometro'].update("Por favor, selecione um tempo válido.")