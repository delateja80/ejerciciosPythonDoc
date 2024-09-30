
def es_primo(numero):
    if numero < 0:
        return False
    for n in range(2, numero + 1):
        is_prime = True 
        for divisor in range(2, n):
            if n % divisor == 0:
                is_prime = False
                break
    return(is_prime)

