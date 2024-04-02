import os 
sw = True

list_bodega1 = []
list_bodega2 = []

def fnt_registrar():
    os.system('cls')
    año = input('Ingrese el año del vehiculo -> ')
    numero_motor =  input("Ingrese el número de motor ->")
    modelo = input('Ingresa el modelo del vehículo -> ')
    fabricante = input('---MENÚ---\n1. Cherolet\n2. Ford\n3. Renout\n4. Dodge\n5 . Hyundai\n6. Fiat\n -> ')
    
    if año == '2024' and  (fabricante=='1' or fabricante=='2' or fabricante == '3'): 
        list_bodega1.append([año, modelo, numero_motor, fabricante])
        neter = input ('Vehiculo resgistrado correctamente <ENTER>')
while sw == True:
    os.system("cls") 
    var_opcion = input('---MENÚ---\n1. Registrar\n2. Mostrar\n-> ')
    if var_opcion  == '1':
        fnt_registrar()