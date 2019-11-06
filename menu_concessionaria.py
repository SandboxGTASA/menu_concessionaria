from random import randint as ri
import locale
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')# ou pt_BR.UTF-8'



# VARIAVEIS
transacoes = tuple(("comprar vender alugar sair").split())
cp = carros_populares = list((' gol chevette opala corsa parati saveiro palio  ').split())
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


# APRENSENTAÇÃO:
titulo = '[Concessionária Python - Compra, venda, alocação de veiculos]'
print(titulo)
print('[Bem vindo, oq deseja:]')
print('[Digite:]')
for reflect in enumerate(transacoes):
    print( reflect)

while True:
    escolha = input('digite aqui: ')
    if escolha .isnumeric() and escolha in ('0123'):
        escolha = int(escolha)
        break
    else:
        print('faça sua escolha conforme o menu!')



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

# MENU
if {transacoes[escolha]} in ({transacoes[0]}, {transacoes[2]}):
    print(f'[Modelo]{"": ^9}[valor para {transacoes[escolha]}]')
    for count in range(len(gerar_veiculos)):
        print(f'[{count: ^2}]{gerar_veiculos[count]:_<20}', end='')
        if {transacoes[escolha]} == {transacoes[0]}:
            print(f'{setmoeda(valor_veiculos[count]):>13}')
        elif {transacoes[escolha]} == {transacoes[2]}:
            print(f'{setmoeda(aluguel_veiculos[count]):>13}')
    print(f'Qual carro vc quer {transacoes[escolha]} ?')
    while True:
        escolher_carro = input('digite aqui: ')
        if escolher_carro .isnumeric() and escolher_carro in (str(tuple(range(len(gerar_veiculos))))):
            escolher_carro = int(escolher_carro)
            if transacoes[escolha] == transacoes[0]:
                print(f'Parabéns vc comprou {gerar_veiculos[escolher_carro]}, no valor de {setmoeda(valor_veiculos[escolher_carro])}!')
            else:
                print(f'Ok, {gerar_veiculos[escolher_carro]} alugado por {setmoeda(aluguel_veiculos[escolher_carro])} a diaria! ')
            break
        else:
            print('faça sua escolha conforme o menu!')
else:
    if {transacoes[escolha]} == {transacoes[1]}:
        print('Qual carro vc quer vender ?')
        vender = input('Digite o nome do carro: ')
        valor = int(input(f'Qual valor quer em {vender}: ')) # necessario validar int e divisivel por 0
        while True:
        	if ri(1,9) != 7:
        		print('Esse valor está fora do orçamento, faça-nos um desconto, ou não poderemos compra-lo!')
        		if input('([s]Sim [n]Não): ').lower() in ('sim'):
        			print('bacana, vamos conferir com a gerencia, se podemos compra-lo!')
        			valor = (valor)-(valor)/10
        			print(f'valor do {vender} atual : {setmoeda(valor)}')
        		else:
        			print(f'{setmoeda(vender)} não vendido!')
        			break
        	else:
        		print(f'ok, {vender} vendido por {setmoeda(valor)}!')

        		break

    else:
        print('ok, volte sempre!')

input("Fim...")


# FIXES AND ATTS
'''
sistema de saldo, pode ou n pode comprar;
menu de cadastrar/remover ;
formatar moeda  ( biblioteca locale) - SOLVED
mostrar carros por valor decrescente;
sistema de parcelamento da compra;
modo de seguro completo para carros comprado/alugados;
gerar configuração de carros ( ano, em bom estado, etc);
melhorar sistema de valor de compra (mesmo sendo uma zoeira - n da pra levar a serio esses valores );
adicionar carros comprados em vendas;
'''
