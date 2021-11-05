# Palindromo un ejercicio de cadena de texto
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es pali­ndromo')
    else:
        print('No es pali­ndromo')

# Esta linea indicque que debe correr la función run()
if __name__ == '__main__':
    run()