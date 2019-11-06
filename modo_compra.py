from tkinter import *
from fixmenu import *
from random import randint as ri
import locale
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')  # ou pt_BR.UTF-8'


# VARIAVEIS
transacoes = tuple(("comprar vender alugar sair").split())
cp = carros_populares = list(
    (' gol chevette opala corsa parati saveiro palio  ').split())
cl = carros_luxo = list((' camaro porshe bmw ferrari ').split())
cores = tuple(('vermelho azul amarelo branco preto laranja metalico').split())
gerar_veiculos = []
valor_veiculos = []
aluguel_veiculos = []


def setmoeda(valor):
    return locale.currency(valor, grouping=True, symbol='r$')


def VALOR_CP():
    return ri(4000.00, 20000.00)


def VALOR_CL():
    return ri(80000.00, 200000.00)


def GERAR_VEICULOS_ADD():
    cor = cores[ri(0, len(cores)-1)]
    carro = str(f'{reflect}({cor})')
    gerar_veiculos.append(carro)


def ALUGAR():
    aluguel = int(valor_veiculos[-1]) / 100
    aluguel_veiculos.append(aluguel)


# GERAR(CARROS)
for count in range(ri(1, 5)):
    for reflect in carros_populares:
        if ri(1, 2) % 2 == 0:
            GERAR_VEICULOS_ADD()
            valor_veiculos.append(VALOR_CP())
            ALUGAR()

for count in range(ri(1, 3)):
    for reflect in carros_luxo:
        if ri(1, 2) % 2 == 0:
            GERAR_VEICULOS_ADD()
            valor_veiculos.append(VALOR_CL())
            ALUGAR()

max = int(len(gerar_veiculos)-1)
contar = max//2


def CAR():
    return f'{gerar_veiculos[contar]} {setmoeda(valor_veiculos[contar])}'


nomedocarro = CAR()
fix_vendas = 'CARRO COMPRADO: '
fix_finalizado = 'vc ja comprou: '


def COMPRAR(modo):
        # print(gerar_veiculos)
    ver = Tk()
    ver.title('Carros a venda')
    ver.resizable(False, False)
    ver.geometry()
    if modo == 'Alugar':
        global valor_veiculos
        global fix_vendas
        global fix_finalizado
        valor_veiculos = aluguel_veiculos
        fix_vendas = 'CARRO ALUGADO: '
        fix_finalizado = 'vc ja alugou: '
        # print(valor_veiculos)
        # print(aluguel_veiculos)

    def LEVAR():
        if 'R$' in namecar['text']:
            compra_realizada = f"{fix_vendas} {CAR()}"
            namecar['text'] = compra_realizada
            if fix_vendas not in gerar_veiculos[contar]:
                gerar_veiculos[contar] = fix_vendas + gerar_veiculos[contar]
            else:
                namecar['text'] = fix_finalizado + gerar_veiculos[contar][15:] + \
                    str(setmoeda(valor_veiculos[contar]))
        else:
            namecar['text'] = 'Clique em "Proximo" para ver um carro!'

    def PROX():
        global contar
        contar += 1
        if contar > max:
            contar = 0
        namecar['text'] = CAR()

    def ANT():
        global contar
        contar -= 1
        if contar < 0:
            contar = max
        namecar['text'] = CAR()


    def SAIR():
        ver.destroy()
        MENU()

    namecar = Label(
        ver, text='Bem vindo vou mostrar os carros que temos!', font=15)
    namecar.pack(side=TOP, fill=X)
    # tag_cor = Button(ver,bg='red').pack(side=TOP,anchor=W,fill=X) # colocar uma tag com a cor referente do carro

    anterior = Button(ver, text='Anterior', width=10,
                      command=ANT).pack(side=LEFT, anchor=S)
    compra = Button(ver, text=modo, width=20,
                    command=LEVAR).pack(side=LEFT, anchor=S)
    proximo = Button(ver, text='Proximo', width=10,
                     command=PROX).pack(side=LEFT, anchor=S)
    finalizar = Button(ver, text='[Voltar ao menu]', width=10, command=SAIR).pack(
        side=BOTTOM, anchor=S)

    ver.mainloop()
