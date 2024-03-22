lista_programas = []

import os 
sw = True
def fnt_agregar(p):
    global lista_programas
    if p =='':
        enter = input('Debe ingresar un programa')

    else:
        lista_programas.append(p)
        enter = input(f'El programa {p} ha sido registrado con exito <ENTER>')

def fnt_seleccion(op):
    if op =="1":
        program = input('Ingrese el nombre del programa -> ')
        fnt_agregar(program)
    
    elif op=="2":
        if len(lista_programas) >0:
            fnt_mostrar()
        else:
            enter = input("\nNo hay programas para mostrar <ENTER>")
    
    elif op== "3":
        fnt_eliminar()

    elif  op=="4":
        print(lista_programas,'\n')
        pos = input('\nIngrese la posición del progarma a eliminar-> ')
        fnt_eliminarP(pos)
def fnt_mostrar():
    print(lista_programas)
    enter = input('\n<ENTER>')
def fnt_eliminar():
    lista_programas.pop()
    enter=input('Se elimino correctamente\n<ENTER>')
def fnt_eliminarP(pos):
    print(lista_programas,'\n')
    tamaño = len(lista_programas)
    if len(lista_programas) > 0 :
        if tamaño > int(pos):
            lista_programas.pop(int(pos))
            enter = input('\nPrograma elimindo con exito <ENTER>')
        else:
            enter = input('\nPosición no valida en la lista<ENTER>\n')
    else:
        enter = input('\nLa lista esta vacia, no se puede realizar la operación<ENTER>')
while sw == True:
    os.system("cls") 
    var_opcion = input('---MENÚ---\n1. Agrega\n2. Mostrar\n3. Eliminar programa x orden\n4. Eliminar programa por posición\n -> ')
    fnt_seleccion(var_opcion)
