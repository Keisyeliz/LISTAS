lista_nombre = []
#Lista de nombres
'''lista_nombre.append('Keisy')
lista_nombre.append('Eliza')'''

var_n = input('Ingrese el nombre del usuario: ')
if var_n == '':
    enter = input('Debe ingresar un nombre: ')
else:
    lista_nombre.append(var_n)
    enter = input(f'{var_n} Ha sido almacenado con exito')

print(lista_nombre)

