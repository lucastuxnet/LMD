####################################################################
#cidademaisproxima.py
#
#DDA 28.09.2020
#
#DESC: Programa feito em python para calcular a menor distância entre
#      as cidades escolhidas.
#
#ALUNO: Lucas Albino Martins - Matricula: 12011ECP022
#
######################################################################


from tkinter import *

from tkinter.ttk import *

from tkinter import scrolledtext

from tkinter import messagebox


# Iniciando a janela de opções de cidades.
window = Tk()
 
window.title("Menor distancia")
 
window.geometry('300x200')



# Opções da janela das cidades.

def ir():
    inicio = cbox1.get()
    final = cbox2.get()
    print ("Inicio lido pelo código: "+str(inicio))
    print ("Final lido pelo código: "+str(final))
    dijkstra( inicio, final)

def sair(self):
    self.messagebox.destroy()

# Definindo os pesos e as respectivas cidades.

def dijkstra( inicio, final):
    grafo = {'Araguari': {'Cascalho Rico': 28, 'Estrela do Sul': 34, 'Uberlandia': 30},
         'Capinopolis': {'Centralina': 40, 'Ituiutaba': 30},
         'Cascalho Rico': {'Araguari': 28, 'Grupiara': 32},
         'Centralina': {'Capinopolis': 40, 'Itumbiara': 20, 'Monte Alegre de Minas': 75},
         'Douradinhos': {'Ituiutaba': 90, 'Monte Alegre de Minas': 28, 'Uberlandia': 63},
         'Estrela do Sul': {'Araguari': 34, 'Grupiara': 38, 'Romaria': 27},
         'Grupiara': {'Cascalho Rico': 32, 'Estrela do Sul': 38},
         'Indianopolis': {'Sao Juliana': 40, 'Uberlandia': 45},
         'Ituiutaba': {'Capinopolis': 30, 'Douradinhos': 90, 'Monte Alegre de Minas': 85},
         'Itumbiara': {'Centralina': 20, 'Tupaciguara': 55},
         'Monte Alegre de Minas': {'Centralina': 75, 'Douradinhos': 28, 'Ituiutaba': 85,
                                   'Tupaciguara': 44, 'Uberlandia': 60},
         'Romaria': {'Estrela do Sul': 27, 'Sao Juliana': 28},
         'Sao Juliana': {'Indianopolis': 40, 'Romaria': 28},
         'Tupaciguara': {'Itumbiara': 55, 'Monte Alegre de Minas': 44, 'Uberlandia': 60},
         'Uberlandia': {'Araguari': 30, 'Douradinhos': 63, 'Indianopolis': 45,
                        'Monte Alegre de Minas': 60, 'Romaria': 78, 'Tupaciguara': 60}}
    menordistancia = {}
    antecessor = {}
    nosinvisiveis = grafo
    infinito = 9999999
    caminho = []

# Calculando a menor distância.

    for noh in nosinvisiveis:
        menordistancia[noh] = infinito
    menordistancia[inicio] = 0
    while nosinvisiveis:
        menornoh = None
        for noh in nosinvisiveis:
            if menornoh is None:
                menornoh = noh
            elif menordistancia[noh] < menordistancia[menornoh]:
                menornoh = noh

        for nohfilha, peso in grafo[menornoh].items():
            if peso + menordistancia[menornoh] < menordistancia[nohfilha]:
                menordistancia[nohfilha] = peso + menordistancia[menornoh]
                antecessor[nohfilha] = menornoh
        nosinvisiveis.pop(menornoh)

    nohatual = final
    while nohatual != inicio:
        try:
            caminho.insert(0, nohatual)
            nohatual = antecessor[nohatual]
        except KeyError:
            print('Nao ha caminhos possiveis')
            break
    caminho.insert(0, inicio)

# Imprimindo a distância na tela.

    if menordistancia[final] != infinito:
        messagebox.showinfo('',
        'A menor distancia possivel e: ' + str(menordistancia[final]) + ' Km\n'
        'E o menor caminho e: ' + str(caminho))
      

label1 = Label(window, text="Cidade de saida:")
label1.grid(column=1, row=4, padx= 10)
label2 = Label(window, text="Cidade de destino:   ")
label2.grid(column=1, row=7, padx= 10)

#Criando as dialog com as cidades

cbox1 = Combobox(window, width=15)
cbox1['values']= ('Araguari', 'Capinopolis', 'Cascalho Rico', 'Centralina', 'Douradinhos', 'Estrela do Sul', 'Grupiara',
                'Indianopolis', 'Ituiutaba', 'Itumbiara', 'Monte Alegre de Minas', 'Romaria', 'Sao Juliana',
                'Tupaciguara', 'Uberlandia')
cbox1.current(0) #set the selected item
cbox1.grid(column=2, row=4, rowspan=2, padx= 4, pady=10)

cbox2 = Combobox(window, width=15)
cbox2['values']= ('Araguari', 'Capinopolis', 'Cascalho Rico', 'Centralina', 'Douradinhos', 'Estrela do Sul', 'Grupiara',
                'Indianopolis', 'Ituiutaba', 'Itumbiara', 'Monte Alegre de Minas', 'Romaria', 'Sao Juliana',
                'Tupaciguara', 'Uberlandia')
cbox2.current(1) #set the selected item
cbox2.grid(column=2, row=7, rowspan=2, padx= 4, pady=20)

# Criando o botão pra iniciar o dijkstra

btn = Button(window, text="Ir", command=ir)
btn.grid(column=2, row=26, rowspan=4, padx= 40, pady=40)


window.mainloop()