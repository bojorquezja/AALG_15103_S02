# Verifica que tenga 11 caracteres y que todos sean números 
def validar_ruc(ruc): 
    if len(ruc) == 11 and ruc.isdigit(): 
        return True
    else: 
        return False 
    
nombre = input("Ingrese el nombre del cliente: ") 
ruc = input("Ingrese el RUC: ") 
if validar_ruc(ruc): 
    print("\n--- RESULTADO ---") 
    print("Cliente:", nombre) 
    print("RUC válido") 
else: 
    print("\nError: El RUC debe tener exactamente 11 dígitos numéricos.")