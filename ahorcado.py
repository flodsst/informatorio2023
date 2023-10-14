import random

'''Defino mi lista de palabras y elijo una al azar'''
lista_palabras = ["chocolate", "elefante", "guitarra", "aventura", "manzana", "universo", "serenidad", "montaña", "esmeralda", "melodía"]

palabra_incognita = random.choice(lista_palabras)

print(palabra_incognita)

'''inicializo intentos y lista de letras correctas e incorrectas'''
intentos = 6
letras_adivinadas = []
letras_incorrectas = []


'''Codigo para verificar si la letra ingresada está en la palabra incognita y actualizar el estado'''
print('La palabra secreta es: ' + ('_'*len(palabra_incognita)))

while intentos > 0:
    letra = input('Elige una letra: ').lower()
    
    if letra in palabra_incognita:
        letras_adivinadas.append(letra)
        print(f'La letra {letra} está en la palabra')
    else:
        letras_incorrectas.append(letra)
        print(f'La letra {letra} no está en la palabra')
        intentos -= 1
    
    palabra_oculta = ''
    for letra in palabra_incognita:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += '_'
        

    print(palabra_oculta)
    print(f'Letras adivinadas: {letras_adivinadas}')
    print(f'Letras incorrectas: {letras_incorrectas}')
    print(f'Te quedan {intentos} intentos')

    if palabra_oculta == palabra_incognita:
        print(f'Bravo! Ganaste. La palabra es {palabra_incognita}')
    else:
        print(f'Perdiste. La palabra es  {palabra_incognita}')


