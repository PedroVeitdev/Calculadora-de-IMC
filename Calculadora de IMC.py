print('Cálculo do Índice de Massa Corporal (IMC)')

nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

print('Calculando seu IMC, aguarde...')

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'{nome}, seu IMC é {imc:.1f}. Você está abaixo do peso ideal.')
elif imc <= 24.9:
    print(f'{nome}, seu IMC é {imc:.1f}. Você está no peso normal.')
elif imc <= 29.9:
    print(f'{nome}, seu IMC é {imc:.1f}. Você está com sobrepeso.')
elif imc <= 34.9:
    print(f'{nome}, seu IMC é {imc:.1f}. Você está com obesidade grau I.')
elif imc <= 39.9:
    print(f'{nome}, seu IMC é {imc:.1f}. Você está com obesidade grau II.')
else:
    print(f'{nome}, seu IMC é {imc:.1f}. Você está com obesidade grau III (mórbida).')