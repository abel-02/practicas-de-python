import random


#Funciones para probar python

def esPar(num):
    if num%2==0:
        return True
    return False


def maxEntre3(a,b,c):
    if(a > b):
        if(a>c):
            return a
        return c
    if(b>c):
        return b
    return c


def maxEntre3conFuncion(a,b,c):
    return max(a,b,c)

def multiplicarHasta10():
    resultado = 0;
    for i in range (1,11):
        resultado*= i
    return resultado

def sumarTodaLaLista(lista):
    return sum(lista)

def encontrarPrimosHastaN(n):
    cantidadDePrimos = 0
    for i in range (1,n+1):
        if(cantidadDeDivisoresDeUnNum(i) == 2):
            cantidadDePrimos=+1
    return cantidadDePrimos

def cantidadDeDivisoresDeUnNum(numero):
    divisores = 0
    for j in range(1, numero + 1):
        if (numero % j == 1):
            divisores += 1
    return divisores

#Version gpt
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_hasta(n):
    return [x for x in range(2, n+1) if es_primo(x)]



def contarLetrasEnCadena(cadena):
    cantidadLetras = 0
    for char in cadena:
        cantidadLetras=+1
    return cantidadLetras

#JuegoDeAdivinar
def advinarNumEntre(a,b):
    intentos = 5
    numeroSecreto = random.randint(a,b)
    numeroElegido=int(input("Ingrese el número que estoy pensando \n Tienes 5 intentos\n "))

    while(numeroElegido != numeroSecreto and intentos > 1):
        if(numeroElegido > numeroSecreto):
            print("Te pasaste!")
        else:
            print("Te quedaste corto!")
        intentos-=1
        numeroElegido = int(input("Ingrese el número que estoy pensando \n Tienes " + str(intentos) + " intentos\n"))

    if(intentos == 0):
        print("Que lastima! No pudiste adivinar en qué número estaba pensando")
    else:
        print("¡Felicitaciones! ¡Adivinaste el numero que estaba pensando!")


#Ejecutar

advinarNumEntre(1,100)