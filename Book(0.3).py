#Aumento salarial

salario = float(input('Entre com o salário: R$ '))
aumento = float(input('Entre com a porcentagem do aumento pretendido: R$ '))
aumento_salarial = (salario * aumento) /100
salariototal = salario + aumento_salarial

print(f'O aumento salarial foi de: R${aumento_salarial:.2f}, seu saralio atualmente é de R${salariototal:.2f}')