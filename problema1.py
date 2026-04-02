"""
Pida el nombre del cliente, 
cuantas manzanas comprara y un precio. 
Muestre el nombre y el total a pagar
"""
nom = input("Ingrese nombre:\n")
can = int(input("Ingrese cantidad manzanas:\n"))
pre = float(input("Ingrese precio:\n"))
tot = can * pre
print(f"{nom} compro S/{tot}")