#Desafio-00-1
'''
print('Olá Mundo')

name = input('Qual o seu nome? ')
print('Bem vindo',name)

print(f'É um prazer te conhecer, {name}')
print('É um prazer te conhecer, {}!' .format(name))
'''

#Desafio-00-1
'''
number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))

soma = number1 + number2

print(f'A soma dos números {number1} + {number2} é {soma}')
'''

#Desafio-00-2
'''
algo = input('Digite algo:')

print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É um alfabético?' , algo.isalpha())
print('É um alfanumérico' , algo.isalnum())
print('Está em maiúsculas? ' , algo.isupper())
print('Está em minúsculas ' , algo.islower())
print('Está capitalizada?', algo.istitle())
'''
#Desafio-00-3

#00
'''
number = int(input('Digite um número: '))
print(f"O número é {number}, seu sucessor é {number+1} e seu antecessor é {number-1}" )
'''

#01
'''
number = int(input('Digite um número: '))
print(f'O número escolhido foi {number}, o dobro {number*2}, o triplo {number*3} e a raiz quadrada {number**(1/2):.2f}')
'''

#02
'''
primeiraNota = float(input('Digite a primeira nota: '))
segundaNota = float(input('Digite a segunda nota: '))

media = (primeiraNota + segundaNota) / 2

print("Sua média é : ", media)
'''

#03
'''
metros = float(input('Digite a quantidade em metros: '))
conversao_centimetros = metros*100
conversao_milimetros = metros*1000

print(f'metros: {metros}, conversao_centimetros:{conversao_centimetros}, conversao_milimetros: {conversao_milimetros}')

'''

#04
'''
numero = int(input('Digite um numero para ver sua tabuada: '))

for i in range(1, 11):
    print(f'{i} x {numero} = {i*numero}')
'''

#05
'''
valor_em_real = float(input('Digite os reais para converter: '))
valor_em_dolar = 5.30
valor_convertido = valor_em_real/valor_em_dolar

print(f'O valor de R${valor_em_real:.2f} equívale a US{valor_convertido:.2f}')

'''

#06
'''
altura = (float(input('Digite a altura da parede: ')))
largura = (float(input('Digite a largura da parede: ')))
area = largura * altura
#2m²
tinta_cobre = 2
quantidade_tinta = area / tinta_cobre

print(f'1 litro de tinta cobre 2m², então para cobrir {area:.2f}m² precisara de {quantidade_tinta:.2f} litros de tinta')

'''

#07
'''
produto = float(input('O preço do produto: '))
desconto_5 = 0.95

valor_com_desconto = produto * desconto_5

print(f'Valor original: {produto:.2f}\nValor com desconto de 5%: {valor_com_desconto:.2f}')

'''
#08
'''
salario = float(input('Digite seu salário: '))
aumento_de_15 = 1.15

salario_com_aumento = salario * aumento_de_15

print(f'Salário original: {salario:.2f}\nValor com aumento de 15%: {salario_com_aumento:.2f}')

'''
#09
'''
dias = int(input('Quantos dias alugado: '))
km = int(input('Quantos km rodados: '))

valor_para_pagar = (dias * 60) + (km *0.15)
print(f'O total a pagar é de RS{valor_para_pagar:.2f}')

'''



