#Conversor de Medidas
medida = float(input('Informe um valor em metros: ')) #tente com 1m, assim faz uma regra de 3!
cm = medida * 100
mm = medida * 1000
print(f'A media de {medida}m corresponde á {cm:.0f}cm e {mm:.0f}mm')
#{cm:.0f} = {cm:CARACTERE_RESERVADO.NUMEROS_APÓS_A_VIRGULA(FLOAT)}
#(*) = Sentido de conversão de metros para centimetros:
#(/) = Sentido de conversão de centimetros para metros;