#Aluguel de carro

kilometros = int(input('Quantos kilometros o carro alugado já andou: '))
aluguel = int(input('Por quantos dias o carro foi alugado: '))
cobkilometros = kilometros * 60
cobaluguel = aluguel * 0.15

pagamento = cobkilometros * cobaluguel

print(f'A diaria do carro vai ficar: R${pagamento}')


