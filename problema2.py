"""
Pida el nombre y ruc de un cliente y cree una funcion que valide que tenga 11 cifras
tal que si falla le indique al usuario que esta mal escrito 
"""

nombre=input("Ingrese su nombre: ") 
ruc=input("Ingrese el ruc: ") 
if len(ruc)>11: 
    print("Error!, El ruc tiene más de 11 digitos.") 
elif len(ruc)<11: 
    print("Error!, El ruc tiene menos de 11 digitos.") 
else : 
    print("Datos ingresado correctamente!.")