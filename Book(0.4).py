#consulta de mercadorias, descontos e valores

tomate = 9.99
cebola = 10.99
frango = 15.99

destomate = (tomate * 5.00) /100
descebola = (cebola * 5.00) /100
desfrango = (frango * 5.00) /100

pretomate = tomate + destomate
precebola = cebola + descebola
prefrango = frango + desfrango

print('Quais os valores das sopas?')
print(f'Sopa de tomate: R${tomate:.2f}')
print(f'Sopa de cebola: R${cebola:.2f}')
print(f'Sopa de frango: R${frango:.2f}')

print(f'\nE os descontos?')
print(f'A sopa de tomate tem: R${destomate:0.2f} de desconto')
print(f'A sopa de cebola tem: R${descebola:0.2f} de desconto')
print(f'A sopa de frango tem: R${desfrango:0.2f} de desconto')

print('\nQuanto ficaria cada sopa com os descontos?')
print(f'Com desconto a sopa de tomate fica: R${pretomate:0.2f}')
print(f'Com desconto a sopa de cebola fica: R${precebola:0.2f}')
print(f'Com desconto a sopa de frango fica: R${prefrango:0.2f}')