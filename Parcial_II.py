''' 2- Analice la complejidad temporal del siguiente código: '''
def operacion(n):
    suma = 0                    #Aqui no se hace nada asi que es O(1)
    for i in range(n):          #Aqui entramos en un bucle que se repite N veces, por lo tanto es O(n)   
        for j in range(i, n):   #Dentro del bucle anterior encontramos otro mas que se repite n veces, y este al ser O(n) = n*n = n**2   
            suma += i * j       #No se hace nada asi que mantiene la comp. O(n**2)
    return suma

''' 3- Escriba una función en Python que tenga complejidad O(n) y cuente el número de elementos pares en una lista '''
def contar_pares(lista):
    contador = 0
    for i in lista:             #Este es el unico bucle que se repite N veces, por lo tanto la comp. es O(n)
        if i % 2 == 0:          #Este es una operacion constante por lo tanto la comp. es O(n)
            contador += 1
    return contador
    
numeros = [1,2,4,5,6,7,8]
print(contar_pares(numeros))

''' 4- Describa la diferencia entre una pila (LIFO) y una cola (FIFO). Implemente dichas estructuras en python, 
    explicando cada una de sus operaciones '''

class Pila:
    def __init__(self):
        self.pila = []
    
    def insertar(self, elemento): #Agregar un elemento a la pila
        self.pila.append(elemento)
        
    def esta_vacia(self):         #Verificar si la pila esta vacia
        return len(self.pila) == 0
        
    def quitar(self):             #Esto quita un elemento de la pila <==> la pila tiene al menos un elemento 
        if self.esta_vacia():
            raise IndexError("La pila está vacía") #Devuelve error si la pila esta vacia
        return self.pila.pop()
    
    def size(self):               #Tamanio de la pila
        return len(self.pila)
    
    def inspeccionar(self):       #Devuelve el ultimo elemento de la pila
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.pila[-1]
    
    def __str__(self):
        return str(self.pila)
    
class Cola:
    def __init__(self):
        self.cola = []

    def esta_vacia(self):           #Si la cola esta vacia, devuelve un bool
        if len(self.cola) == 0:
            return True
        else:
            return False

    def encolar(self, elemento):    #Agregar un elemento a la cola, encolar
        return self.cola.append(elemento)

    def desencolar(self):           #Quitar un elemento de la cola, desencolar
        return self.cola.pop(0)
    
    def size(self):                 #Tamanio de la cola 
        return len(self.cola)
    
    def inspeccionar(self):         #Devuelve el primer elemento de la cola
        return self.cola[0]

    def __str__(self):
        return str(self.cola)
    
''' 5- Implemente una función en Python que use una pila para invertir una lista '''

def invertir_lista(lista):
    pila = Pila() #Asigno una variable a la clase Pila
    for c in lista: #Recorro la cadena
        pila.insertar(c) #Inserto cada elemento de la cadena en la pila
    cadena_invertida = [] #Como necesito devolver la lista vacia, creo una una variable para guardar
    while not pila.esta_vacia(): #Uso el metodo esta_vacia de la clase Pila para recorrer hasta que el bucle se termine
        cadena_invertida.append(pila.quitar()) #Aqui quito el ultimo elemento de la pila y lo agrego a la variable cadena_invertida
    return cadena_invertida

p = Pila()
p = [1,2,3,"hola mundo"]
print(invertir_lista(p))

''' 6- Escriba una función que verifique si los paréntesis, corchetes y llaves en una
    expresión están balanceados usando una pila. Ejemplo: "{[()]}" Válido, "{[(])}" → →
    Inválido.'''

def checkBalance(cadena):
    p = Pila()
    parejas = {")": "(", "]": "[", "}": "{"} #Diccionario que relaciona su simbolo de cierre con el de su apertura
    for caracter in cadena: #Recorremos la cadena de simbolos
        if caracter in parejas.values(): #Si caracter es un simbolo de apertura
            p.insertar(caracter) #Se inserta en la pila
        elif caracter in parejas.keys():
            if p.esta_vacia() or p.inspeccionar() != parejas[caracter]: 
                return "Revisar cadena" #Si cadena esta vacia o el tope no es igual al simbolo de apertura, salta un error
            else:
                p.quitar() #En caso contrario, se quita el simbolo de la pila
    if p.esta_vacia():
        return "Cadena balanceada"
    else:
        return "Cadena no balanceada"
        
simbolos = Pila()
simbolos = "{[()]}"
print(checkBalance(simbolos))
simbolos = "{[(])}"
print(checkBalance(simbolos))
            