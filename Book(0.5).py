#viagem de carro

kilometros = float(input('Quantos kilometros você pretende viajar: '))#s=v.t
metros = kilometros // 1000 #s=v.t
velocidade = float(input('Qual a sua velocidade: ')) #v=s/t
tempo = metros / velocidade #t=s/v
tempo_minutos = tempo * 60
print(f'Seu tempo de viagem será de: {tempo_minutos:.2f}s')


#ESSE ESTÀ CERTO, NÃO SEI O QUE FIZ ACIMA, MAS ESTÁ 70% ERRADO!!!
distanciax = 60 #metros
velocidadex = 30 #velocidade
tempo_de_viagem = distanciax / velocidadex
print(f'{tempo_de_viagem}s')