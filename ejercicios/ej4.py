import random

def generar_contraseña():
    contraseña=''
    longitud = random.randint(7, 10)
    for n in range(longitud):
        contraseña = contraseña + chr(random.randint(33, 126)) 
    
    return contraseña
