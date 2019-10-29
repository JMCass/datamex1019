#PRIMER PROYECTO IRONHACK JORGE LUIS MONTAÑO CASILLAS

######################## INICIO #######################
#El programa permite seleccionar de manera aleatoria una palabra dentro de una lista
#de palabras con diversas longitudes y dificultades de adivinar
import random

#Primero, se construye lo que será la horca y el espacio que ocupará la víctima, la cual tendrá 6 oportunidades antes
#de perder el juego

#Se contruyen las imágenes del juego que serán fijas siempre; es decir, serán una constante
#por esta razón, la constante asociada a las imágenes se escribe en mayúsculas
AHORCADO = ['''
+---+
    |
    |
    |
    ===''', '''
+---+
O   |
    |
    |
    ===''', '''
+---+
O   |
|   |
    |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']

#Se genera la lista de palabras que compnen el juego de ahorcado. La lista de palabras están en español y tienen diferentes
#longitudes y grados de dificultad

#Construí un bloque de texto utilizando triples comillas dentro de una variable que llamé palabras

palabras = '''anarquia agudo antibiotico artritis ataxia avenida abismo atrofia afecto axioma ardilla babuino bate baseball bikini bromuro barcelona buffalo bufon banjo 
        boleto camello catrina clamato cobra circulacion controversia caramelo caligrafia croqueta criptografia curacao cadena ciervo duplex diurno durazno dictado dormir
        durango dulce estomago estado elasticidad espina espiritu evaluacion ejercicio ensamble estrategia exodo ferreteria feria futbol francia francisco ferrocarril frente
        gusano gansito gamesa goleador general galaxia galvanizado gerente huracan huasteca hormiga honduras hotel italia irlanda insolvencia inteligente indio ilusion indiferente
        jaguar jabon jazz jicama jinete jiujitsu jazmin jugo jumbo kayak khaki kilobyte kiosko kermes kiwi kenya longitud lujo leon limon linaza lagartija ligamento mole mono mexico
        monterrey mañanero matriz microhondas misterio novedad navidad negocio noruega ninfomana oso oxigeno oviparo orangutan ocupacion ortopedia panda pestaña pixel pizza parasito 
        polka psicologia perro peru paloma python queso quilmes quorum queretaro quejido quechua raton rostizado rabino rinoceronte ritmo rebaja salmon soledad sociedad sabado sabor 
        sabiduria serpiente sonaja sentimiento staff submarino sucursal tigre tortuga torta terminal transcripcion transgenero transplante temerario uniforme unicornio ulcera universo 
        ubicacion utensilio universidad union vacante viajar vapor vodka voodoo vortice wimbledon wisconsin waterpolo whiskey ximena xenofobia xoloitzcuintle xilofono yate yacimiento
        yunque yegua yeso zigzag zipper zodiaco zebra zoologico'''.split()


#La siguiente función selcciona de manera aleatoria una palabra que será la que deberemos de adivinar. La longitud de la lista de palabras son 195
#por lo que para evitar que nos salgamos de rango, empezaremos en 0 y terminaremos en el índice 194
#El resultado es una palabra aleatoria buscada a través de su correspondiente índice

def getRandomWord(palabraList):
    palabraIndex = random.randint(0, len(palabraList) - 1)
    return palabraList[palabraIndex]

#La siguiente función mostrará los 6 displays de la horca conforme el jugador acierte o falle en su adivinanza

def displayBoard(letrasfaltantes, letrascorrectas, palabrasecreta):
    print(AHORCADO[len(letrasfaltantes)])
    print()
#letrasfaltantes, se refiere a un string de letras que el jugador a intentado adivinar, pero no forman parte de la palabra secreta
#letrascorrectas un string con las letras correctas que el jugador ha adivinado y forman parte de la palabra secreta
#palabra secreta es un string con la palabra que el jugador intenta adivinar
    print('Letras faltantes:', end=' ')
    for letra in letrasfaltantes:
        print(letra, end=' ')
        print()
#El for mostrará tantos espacios en blanco como letras tenga la palabra que intentamos adivinar
#pero sobre una misma línea en lugar de un salto de línea
#La variable espacios multiplica tantos espacios en blanco como letras tenga la palabra
    espacios = '_' * len(palabrasecreta)

    #Reemplaza los espacios en blanco por la letra adivinada
    for i in range(len(palabrasecreta)):
        if palabrasecreta[i] in letrascorrectas:
            espacios = espacios[:i] + palabrasecreta[i] + espacios[i+1:]
    
    #Muestra la palabra correcta con los espacios entre cada letra
    for letra in espacios:
        print(letra, end=' ')
    print()

    #Regresa la palabra que el jugador ingresó. La función se asegura que entre una letra y no otro tipo de caracteres
def getGuess(alreadyGuessed):
    
    while True:
        print('Adivina una letra.')
        adivina = input()
        adivina = adivina.lower()
        if len(adivina) != 1:
            print('Por favor, ingresa una letra')
        elif adivina in alreadyGuessed:
            print('Ya adivinaste esa letra. Escoge otra')
        elif adivina not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor, ingresa una letra')
        else:
             return adivina

# La función regresa un TRUE si el jugador quiere jugar de nuevo, en otro caso regresa FALSE
def playAgain():
    
    print('¿Quieres volver a jugar? (si o no)')
    return input().lower().startswith('s')

print('--J U E G O--D E L--A H O R C A D O--')
letrasfaltantes = ''
letrascorrectas = ''
palabrasecreta = getRandomWord(palabras)
gameIsDone = False

while True:
    displayBoard(letrasfaltantes, letrascorrectas, palabrasecreta)

    #Permite al jugador ingresar una letra
    adivina = getGuess(letrasfaltantes + letrascorrectas)

    if adivina in palabrasecreta:
        letrascorrectas = letrascorrectas + adivina

        #Revisa si el jugador ganó
        foundAllLetters = True
        for i in range(len(palabrasecreta)):
            if palabrasecreta[i] not in letrascorrectas:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Correcto! La palabra secreta es: "' + palabrasecreta + '" ¡Ganaste!')
            gameIsDone = True
    else:
         letrasfaltantes = letrasfaltantes + adivina

        #Revisa si el player no ha hecho demasiados intentos y perdido
    if len(letrasfaltantes) == len(AHORCADO) - 1:
        displayBoard(letrasfaltantes, letrascorrectas, palabrasecreta)
        print('¡Se te acabaron los intentos!\n Después de ' + str(len(letrasfaltantes)) + ' intentos fallidos ' +
              str(len(letrascorrectas)) + ' aciertos, la palabra era: "' + palabrasecreta + '"')
        gameIsDone = True
     #Pregunta al jugador si quiere jugar de nuevo (solo si el juego terminó)
    if gameIsDone:
        if playAgain():
            letrasfaltantes = ''
            letrascorrectas = ''
            gameIsDone = False
            palabrasecreta = getRandomWord(palabras)
        else:
            break
