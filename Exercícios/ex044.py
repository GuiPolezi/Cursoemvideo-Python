# Desafio 44 - Gerenciador de pagamentos

"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em ate 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

print('=' * 30, 'Loja', '=' * 30)

produto = float(input('Preço das compras: R$'))
dinheiro = produto * 10 / 100
cartao = produto * 5 / 100
juros = produto * 20 / 100

print('FORMAS DE PAGAMENTO:')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

option = int(input('Qual é a opção? '))
if option > 4:
    print('Opção ínvalida, tente novamente!')
if option == 1:
    desconto = produto - dinheiro
    print(f'Sua compra de R${produto} vai custar {desconto:.2f} no final.')
    print('10% de desconto!!!')
elif option == 2:
    desconto = produto - cartao
    print(f'Sua compra de R${produto} vai custar {desconto:.2f} no final.')
    print('5% de desconto!!!')
elif option == 3:
    total = produto
    parcela = total / 2
    print(f'Sua compra sera parcelada em 2x de R${parcela:.2f}')
    print(f'Em 2x no cartão o preço é normal, sua compra é de R${produto}')
elif option == 4:
    juroos = juros + produto
    parcelamento = int(input('Quantas parcelas? '))
    parcela = juroos / parcelamento
    print(f'Sua compra sera parcelada em {parcelamento}x de R${parcela:.2f} COM JUROS')
    print(f'Sua compra de R${produto} vai custar {juroos:.2f} no final.')