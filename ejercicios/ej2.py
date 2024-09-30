import ej1 

def siguiente_primo(numero):
    if numero < 0:
        return -1
    bandera = True
    valor = numero+1
    
    while bandera:
        if ej1.es_primo(valor):
            bandera = False
        valor = valor + 1
        
    return valor-1
