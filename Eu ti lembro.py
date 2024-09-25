#Desenvolvi esta aplicação ´me recordar de toma um gole de agua enquanto estou ao computador

#bibliotecas usadas
import PySimpleGUI as sg
import time 

escala_tempo=["","1","10","30","60"]#sugestao de tempo em minutos

layout = [
    [sg.P(),sg.T(""),sg.P()],
    [sg.T('Lembrar de:')],
    [sg.I(font=('Any',10,'bold'),size=(43,1),key='lembrete')],       
    [sg.T('Tempo de espera em minutos:')] 
    [sg.DD(values=escala_tempo, size=(42,1),key="tempo")],
    [sg.Button("OK", size=(38, 1), button_color=("white", "blue"),  key='-OK-')],
    [sg.P(),sg.T("",key='display'),sg.P()]]

window = sg.Window("EU TI LEMBRO", layout)
while True:
    try:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Sair"):
            break
        elif event in "-OK-":

            msg=values['lembrete'].title() #recebe o lembrete com maiusculas depois de espaços
            tempo=int(values['tempo'])*60 #recebe o tempo e multiplica por segundo
                
            if tempo> 0:
                window.minimize() #minimia a janela
                for i in range(tempo, 0, -1):
                    window['display'].update(f'Tempo restante: {i} segundos')
                    window.read(timeout=1000)  # aguarda 1 segundo entre atualizações
                
                window.normal()  # Restaura a janel
                window['display'].update(msg)
            else:
                window['display'].update("Por favor, selecione um tempo válido.")
    except:#tratativa generiaca para possiveis erros de execução
        window['display'].update("Por favor, selecione um tempo válido.")