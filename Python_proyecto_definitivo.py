# %% [markdown]
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

# %%
def contador_letras (cadena):
    frecuencia = {}
    for caracter in cadena: ## iteramos por cada caracter del texto
        if caracter != ' ': ## evitamos los espacios y una vez evitados establecemos las condiciones
            if caracter in frecuencia:
                frecuencia [caracter] +=1 ## si ya existe la clave, añadimos uno al valor de esa clave
            else:
                frecuencia [caracter] = 1 ## si no estaba se añade una clave con valor 1
    return frecuencia ## que nos devuelva un diccionario
cadena = "Esto era un poco dificil"
print (contador_letras(cadena))

# %% [markdown]
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# %%
Lista_numeros = [2,4,6,8,10,20,30,100] ##Creamos la lista
el_doble = lambda numero1: numero1 * 2 ##Creamos la funcion que multiplique el numero por 2, para hacer el doble
print (list(map(el_doble,Lista_numeros)))##funcion map donde la funcion aplique a la lista creada. undicamos list para pasar a lista el resultado.

print(list(map(lambda numero1:numero1*2,Lista_numeros))) ##segunda forma, indicando directamente la funcion lambda en map

def doble (numero1):
    return numero1 * 2

Lista_doble = [doble(numero) for numero in Lista_numeros]##tercera forma, crear una lista que se le aplique la funcion iterando por cada elemento de la lista de origen.
print(Lista_doble)


# %% [markdown]
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# %%
lista_inicial = ["Me gusta Python", "Me gusta SQL", "Quiero aprender Python", "Se power Bi"]
def lista_python(lista):
    lista_py = []
    for palabra in lista: ##decimos a la función que itere por toda la lista
        if "Python" in palabra:## establecemos la condición de que si "Python" está en algun elemento de la lista.
            lista_py.append(palabra)##lo lleve a nuestra lista vacia que será el return de la función
        else:
            pass
    return lista_py

print (lista_python(lista_inicial))

# %% [markdown]
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

# %%
lista_primera = [10,20,30,40]
lista_segunda = [4,18,20,35]

def resta(numero1,numero2):##primero calculamos una funcion simple que reste dos numeros
    resultado = numero1 - numero2
    return resultado

def diferencia_lists (lista1,lista2):
    return list(map(resta,lista1,lista2)) ##aplicamos la funcion de resta dentro de una funcion que reste parametros de dos listas

print (diferencia_lists(lista_primera,lista_segunda))

def diferencia_listas(lista1,lista2):
    return list(map(lambda x,y:x-y,lista1,lista2))##aqui lo mismo pero sin el paso previo de la funcion de resta, ya que lo indicamos con la lambda directamente

print (diferencia_listas(lista_primera,lista_segunda))
        

# %% [markdown]
# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5 La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

# %%
notas_Javier = [5,7,9,10,3,6]
notas_Alejandro = [3,2,4,6,5,1,3,3.5]

def notas (lista,aprobado = 5): #establecemos una funcin con una lista y un parametro base
    suma= 0 ##indicamos que la suma empiece desde 0
    for notas in lista: #iteramos por la lista
        suma += notas ##indicamos que sume las notas
    media = suma/len(lista)##establecemos el calculo de la media
    if media >= aprobado:
        estado = "aprobado"##si la media es mayor que el parametro establecido, dame aprobado
    else:
        estado = "suspenso"##si no, suspenso
    return (media,estado)##devuelveme en una tupla, la media y el estado 

print(notas(notas_Javier))
print(notas(notas_Alejandro))

# %% [markdown]
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

# %%
def fact (numero):
  resultado = 1 #damos un valor inicial a la variable resultado
  for valor in range (1,numero + 1,1): ##iteramos por el rango desde el 1 hasta nuestro número elegido, por eso sumamos 1.
    resultado*= valor##indicamos que se multipliquen sucesivamente los valoresdel rango
  return resultado## que nos devuleva esa multiplicación de todos los valores.
print(fact(5))

# %% [markdown]
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

# %%
lista_tupla = [("Hola me gusta Python"), ("Soy del Real Madrid")]
def strings (tupla):
    for texto in tupla: ##Que itere por las diferentes tuplas de la lista
        return tupla[0:1000]  ##Le pido que me devuelva la tupla del caracter 0 al 999 (se podría ampliar)
  
print(list(map(strings,lista_tupla)))


# %% [markdown]
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

# %%
try:    
    num_1 = float(input("Escribe un número"))##primer numero
    print(f"El usuario ha introducido un {num_1}")##que se indique para saberlo
    num_2 = float(input("Escribe otro numero"))##segundo numero
    print(f"El usuario ha introducido un {num_2}")##que se indique para saberlo
    division = num_1/num_2##hacemos la division
    print(f"La division es {division}")
except ValueError:
    print("no se puede indicar un valor no númerico")##error si se indica algo que no es un numero
except ZeroDivisionError:
    print("No se puede dividir entre 0")##error si se intenta dividir entre 0.

# %% [markdown]
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

# %%
lista_mascotas = ["Perro","Gato","Pajaro","Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso","Tortuga","Pez","Conejo"]
def masoctas_validas (lista):
    mascotas_prhibidas = ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"] ## establecemos dentro de la función, la lista de mascotas que no queremos
    return lista not in mascotas_prhibidas ## Queremos que nos devuelva una lista cuyos valores no estén dentro de mascotas prohibidas.
print (list(filter(masoctas_validas,lista_mascotas)))

# %% [markdown]
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# %%
lista_numbers = [10,20,30,40]##creamos la lista con numeros
vacio = []##creamos la lista vacia
def promedio (lista):
    try:
        resultado = 0##creamos la variable partiendo de 0
        for numeros in lista:##iteramos
            resultado +=numeros##sumamos a la variable cada elemento de la lista
        return resultado/len(lista)##dividimos entre el numero de elementos de la lista, para sacar la media
    except ZeroDivisionError:##si la lista está vacia y da un error de 0, manejamos el error.
        print ("La lista esta vacia")
print(promedio(lista_numbers))
promedio(vacio) 

# %% [markdown]
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# %%

try:
    edad = int(input("Por favor, incluye tu edad")) ## Preguntamos al usuario su edad   
    if edad not in range(1,121): ##establecemos un rango, y ponemos condicion en caso de que la edad no esté en ese rango
        print (f"La edad {edad} no es válida")
    else:
        print(f"El usuario tiene {edad} años")
except ValueError: ##manejamos el error en caso de que no se indique un numero
    print("No se debe escribir texto")


# %% [markdown]
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

# %%
cancion = "Son mis amigos"
def longitud_string (texto):
    lista = texto.split()##metemos el texto en una lista
    longitudes = []##creamos una lista vacia donde meter las longitudes
    for valor in lista:##iteramos
        if len(valor) > 0:##si la longitud es mas que 0, la incluimos en la lista inicalmente vacia
            longitudes.append(len(valor))
    else:
        pass
    return longitudes##que nos devuelva esa lista
longitud_string(cancion) ##Aqui no utilizamos la funcion map

def long_string (texto):
    return list(map(len,texto.split()))## pedimos que nos devuelva una lista, y con map, aplicamos la funcion ya predefinida len a la lista creada por el método split().

long_string(cancion)
    

# %% [markdown]
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

# %%
Equipo = "Real Madrid"
def letras_unicas_tupla (texto):
    letras_unicas = list(texto)##definimos una variable que convierta un texto dentro de una lista, para usarla con map
    lista_tuplas =  list(map(lambda texto:(texto.upper(),texto.lower()),letras_unicas))##definimos otra variable que sea una lista, y en map, indicamos una funcion lambda que devuelva mayuscula y minuscula, de la anterior variable
    return lista_tuplas
letras_unicas_tupla(Equipo)


# %% [markdown]
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

# %%
Ciudades = ["Sevilla", "Madrid","Barcelona","Salamanaca","Segovia"]
def letras_S(lista):
    lista_vacia = [] ##Creamos una lista vacia, a la que añadiremos los valores que cumplan la condición
    for ciudad in lista:
        if ciudad [0] == "S": ##Indicamos que la condicion es que incluya los valores cuyo primer caracter sea una "S" 
            lista_vacia.append(ciudad)
        else:
            pass
    return lista_vacia 
ciudades_S = list(filter(letras_S,Ciudades))##Filtraamos la funcion para que nos devuelva una lista de las ciudades que empiezan por S.
print (ciudades_S)

# %% [markdown]
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

# %%
lista_dada = [1,3,6,10,20,50,100]
print (list(map(lambda numero:numero+3,lista_dada)))


# %% [markdown]
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter() 

# %%
cadena_texto = "Hoy el Real Madrid ha ganado al Manchester City"
def words_higher_than_five(text, number = 5):
    lista = text.split()##inclumos el texto en una lista
    return list(filter(lambda word:len(word)>number,lista))#nos devuelve una lista donde se filtre la palabra que tenga más de 5 letras, dentro de la lista que hemos creado.
print(words_higher_than_five(cadena_texto))

##otra forma sin usar filter:

def mas_de_cinco (texto, numero = 5):
    lista_texto = texto.split()##vovlemos a meter el texto en una lista
    lista_empty = []## creamos lista vacia
    for caracter in lista_texto:##recorremos la lista del texto
        if len(caracter) > numero:##indicamos condición
            lista_empty.append(caracter)##apendeamos las palabras que cumplan la condición
        else:
            pass
    return (lista_empty)##y que nos devuelva las lista con las palabras que cumplen la condición
print (mas_de_cinco(cadena_texto))

# %% [markdown]
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

# %%
from functools import reduce ##importamos reduce
lista_numero = [5,7,2]

def resultado (lista):
      return reduce (lambda x,t: x*10+t,lista)##lo que hace es que 5*10+7 = 57, se conviete de nuevo en x, despues hace 570 + 2 y ya te da 572
resultado(lista_numero)


# %% [markdown]
# 18.Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter() 

# %%
estudiantes = [{"Nombre":"Juan","edad":20,"clasificacion":90},{"Nombre":"Carlos","edad":22,"clasificacion":80},{"Nombre":"Pedro","edad":24,"clasificacion":98}]
print (list(filter(lambda estudiante:estudiante["clasificacion"] >=90,estudiantes))) ##filtramos con lambda los diccionarios donde la clave clasificación sea >=90


# %% [markdown]
# 19. Crea una función lambda que filtre los números impares de una lista dada.

# %%
given_list = [3,4,5,6,11,34,90,45,32,63,12,245]
funcion_lamb = lambda x:x%2!=0 ##establecemos una función que indique solo numeros impares
print(list(filter(funcion_lamb,given_list)))##filtrmos la funcion lambda en la variable con la lista con numeros aleatorios 

# %% [markdown]
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

# %%
lista_int_str = [1,5,23,100,"Hola","Me gusta Python", "Me gusta Power BI"]

def lista_int_2(lista):
    return list(filter(lambda x:type(x)==int,lista))##indicamos que devuelva una lista, filtrando la funcion lambda de que solo de los de tipo int
print(lista_int_2(lista_int_str))

##otra forma,sin filter:

def lista_int(lista):
    lista_vacia = []##creamos una lista vacia
    for caracter in lista:##iteramos por cada carcater de la lista donde apliquemos la función
        if type(caracter) ==int:##establecemos la condición, y incluimos donde se cumpla en la lista creada
            lista_vacia.append(caracter)
        else:
            pass
    return lista_vacia##que nos devuleva la lista donde 
print(lista_int(lista_int_str))

# %% [markdown]
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

# %%
cubo = lambda r:r**3 ##creamos una lambda que calcule el cubo de cualquier numero
print (cubo(3))

# %% [markdown]
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

# %%
from functools import reduce 
lista_numeros_aleatorios = [5,20,100] 
print(reduce(lambda r,t:r*t,lista_numeros_aleatorios))##utilizamos el reduce e indicamos una funcion lambda que multiplique dos numeros. Primero hará 5*20=100 y luego 100*100

# %% [markdown]
# 23. Concatena una lista de palabras.Usa la función reduce() .

# %%
from functools import reduce
lista_de_palabras = ["Mi","nombre","es","Javier"]
print (reduce(lambda r,t:r+" "+t,lista_de_palabras))## va concatenando un texto tras otro, contando los espacios. Si no los quisieramos solo habría que poner "".

# %% [markdown]
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

# %%
lista_a_restar = [20,10,5,3]
print(reduce(lambda r,t:r-t,lista_a_restar)) ##hacemos una lambda que reste los valores a la lista creada 

# %% [markdown]
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

# %%
cadena_de_texto = "Hoy juega el Real Madrid contra el Osasuna"
def contar_caracteres(texto):
    contar = len(texto)##creamos una variable que cuente los caracteres del texto
    return contar
print(contar_caracteres(cadena_de_texto))

##otra forma con Lambda
contando = lambda texto:len(texto)##creamos una lambda que cuente los caracteres de un texto, y la guardamos en una variable.
print(contando(cadena_de_texto))

##ahora omitiendo los espacios:
contando_sin_espacios = lambda texto:len(texto.replace(" ",""))##añadimos el metodo replace para quitar los espacios y asi cuente toda la cadena seguida.
print(contando_sin_espacios(cadena_de_texto))

# %% [markdown]
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# %%
funcion_resto = lambda r,t:r%t ##establecemos una lambda que saque el resto de la division entre 2 numeros a tarvés del operador %
print(funcion_resto(10,4))

# %% [markdown]
# 27. Crea una función que calcule el promedio de una lista de números.

# %%
lista_hacer_promedio = [2,5,6,7,3,4,6,7]
def promedio (lista):
    result = 0 ##iniciamos la variable a 0
    for caracter in lista: ##iteramos por la lista
        result += caracter  ##sumamos los elementos de la lista         
    return int(result/len(lista))##que nos devuelva la variable que suma los elementos de la lista, entre la longitud de la lista
promedio(lista_hacer_promedio)

##otra forma

suma_lista = reduce(lambda t,r:t+r,lista_hacer_promedio) ##creamos una variable con la suma de los elementos de la lista
resultado = suma_lista/len(lista_hacer_promedio)##creamos otra variable que divida la anterior variable entre la longitud de la lista
print (int(resultado))

# %% [markdown]
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# %%
lista_a_buscar_primer_duplicado = ["hola",3,56,"adios",6789,56,3]
def duplicados (lista):
    elementos_ya_vistos =[]##creamos una lista vacia donde añadiremos los elementos 
    for ch in lista:
        if ch in elementos_ya_vistos: ##establecemos la condición de que si ya está el elemnto en la lista nos lo devuelva
            return ch
        elementos_ya_vistos.append(ch) ##por último, añadimos los elementos para que salte el primer duplicado, que significa que ya estará dentro de la lista
       
print(duplicados(lista_a_buscar_primer_duplicado))

# %% [markdown]
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

# %%
variable = "Trabajadores"
def enmascarar (variable):
    texto = str(variable)
    return "#"*(len(texto)-4) + texto[-4:]  ##multiplicamos por #todo el texto, y retamos 4 que son los que queremos que se vean. Luego sumamos los ultimos 4 caracteres de la cadena.
print (enmascarar(variable))

# %% [markdown]
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

# %%
anagrama_1 = "Roma"
anagrama_2 = "Amor"
def anagramas (anagrama_1,anagrama_2):
    anagrama_1_lista_ordenada = sorted(anagrama_1.lower())##el metodo sorted crea una lista del texto, y la ordena alfabeticamente. Tambien incluimos el metodo lower para no se sernsible a mayusculas
    anagrama_2_lista_ordenada = sorted(anagrama_2.lower())##el metodo sorted crea una lista del texto, y la ordena alfabeticamente. Tambien incluimos el metodo lower para no se sernsible a mayusculas
    if (anagrama_1_lista_ordenada) == (anagrama_2_lista_ordenada):##ponemos la condición de que si las listas son iguales devuelva que las variables son anagramas
        return "Estas dos variables SI son anagramas"
    else:
        return "Estas dos variables NO son anagramas"    
print(anagramas(anagrama_1,anagrama_2)) 

# %% [markdown]
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

# %%
def lista_nombres ():
    lista_de_nombres = (input(f"Indique varios nombres separados por comas").split(','))##solicitamos que indiquen varios nombres, y lo convertimos a lista, haciendo que cuando vea una coma sea un nuevo elemento de la lista.
    nombre = (input(f"Indica un nombre a buscar en la lista de nombres"))##solicitamos que indiquen un nombre    
    if nombre in lista_de_nombres:
        return (f"El nombre {nombre} esta incluido en la lista")##ponemos una condicion que diga una cosa u otra si el nombre está dentro de la lista
    else:
        return (f"El nombre {nombre} NO esta incluido en la lista")    
print (lista_nombres())   

# %% [markdown]
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

# %%
empleado = "Pepe Castro"
lista_empleados_en_thepower = [{"nombre":"Alex Garcia","posicion":"Analista de datos"},{"nombre":"Juan Cruz","posicion":"Conserje"},{"nombre":"Pepe Castro","posicion":"CEO"}]
def nombre_empleado(nombre_completo,lista):
    for empleado in lista:##iteramos por la lista, que se compone de diccionarios
        if empleado ["nombre"] == nombre_completo:##ponemos condición de que si el valor de la clave "nombre" es igual al primer parametro
            return empleado ["posicion"]##devuelva el valor de la clave posición
    return (f"La persona no trabaja aquí")## y si no, decir que no trabaja aquí.
print(nombre_empleado(empleado,lista_empleados_en_thepower))


# %% [markdown]
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# %%
lista_100 = [100,50,25]
lista_200 = [200,50,25] 

suma_listas = list(map(lambda c,t:c+t,lista_100,lista_200))##dame una lista y con map, suma los valores entre las dos listas dadas.
print(suma_listas)
##Además, para saber el resultado de la suma total: 
print(reduce(lambda x,r:x+r,suma_listas))##resultado total, con la lista derivada de la suma de dos listas, sumar sus valores con reduce y lambda
##segunda forma
suma_lista_100 = (reduce(lambda s,j:s+j,lista_100))##identificar el resultado de sumar los valores de la primera lista
suma_lista_200 = (reduce(lambda s,j:s+j,lista_200))##identificar el resultado de sumar los valores de la primera lista
print (suma_lista_100+suma_lista_200)##sumar ambas variables


# %% [markdown]
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

# %%

class arbol:
    def __init__(self,tronco,ramas): 
        self.tronco = tronco
        self.ramas = ramas
    def crecer_tronco(self):
        self.tronco +=1##hacemos que el tronco incremente en 1 cada vez que se aplique este método
        return (f"La nueva longitud del tronco es {self.tronco}")
    def nueva_rama(self):
        self.ramas.append(1)##creamos un metodo que añada un 1 a la lista de ramas.
        return (f"se ha añadido una nueva rama. Ramas totales : {self.ramas}")
    def crecer_ramas(self):      
        self.ramas = [ram +1 for ram in self.ramas]##llamamos ram a todas las ramas de la lista y decimos que sume 1
        return f"se ha aumentado una unidad a todas las ramas. Ramas totales : {self.ramas}"
    def quitar_rama(self):
        self.ramas.pop(1)##indicamos que elimine la posición 2 de la lista
        return (f"Se ha eliminado la rama de la posición 2. Ramas totales : {self.ramas}")
    def info_arbol(self):
        return (f"información: su tronco mide {self.tronco}, tiene {len(self.ramas)} ramas y sus longitudes son {self.ramas}")      

# %%
##Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
naranjo = arbol(1,[])##creamos el arbol naranjo
##Hacer crecer el tronco del árbol una unidad.
naranjo.crecer_tronco()
##Añadir una nueva rama al árbol.
naranjo.nueva_rama()
##Hacer crecer todas las ramas del árbol una unidad.
naranjo.crecer_ramas()
##Añadir dos nuevas ramas al árbol.
naranjo.nueva_rama()
naranjo.nueva_rama()
##Retirar la rama situada en la posición 2.
naranjo.quitar_rama()
##Obtener información sobre el árbol.
naranjo.info_arbol()




# %% [markdown]
# 35. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

# %%
class UsuarioBanco:
    def __init__(self,nombre,saldo,cuenta_correiente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_correinte = cuenta_correiente
    def retirar_dinero(self,cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return (f"El usuario {self.nombre} ha retirado {cantidad}. Su saldo ahora es: {self.saldo}")
        else:
            return (f"La cantidad {cantidad} es mayor al saldo disponible")
    def agregar_dinero(self,dinero):
        self.saldo = self.saldo + dinero
        return (f"El usuario {self.nombre} ha agregado {dinero}. Su saldo ahora es: {self.saldo}")
    def transferir_dinero(self,otro_usuario,amount):
        if self.saldo >= amount:
            self.saldo -= amount
            otro_usuario += amount 
            return (f"{self.nombre} ha hecho una transferencia de {amount} a {otro_usuario}")
        else:
            return (f"el usuario {self.nombre} no puede transferir {amount} porque su saldo es: {self.saldo}")   

# %%
##1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
Alicia = UsuarioBanco("Alcia",100,True)
Bob = UsuarioBanco("Bob",50,True)

# %%
##2. Agregar 20 unidades de saldo de "Bob".
print(Bob.agregar_dinero(20))

# %%
##3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
print(Bob.transferir_dinero(Alicia,80))

# %%
##4. Retirar 50 unidades de saldo a "Alicia".
print(Alicia.retirar_dinero(50))

# %% [markdown]
# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .

# %%
##Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
def contar_palabras (texto):
    cadena = texto.split()##pasamos el texto a una lista
    diccionario_conteo = {}##cremoa un diccionario vacio
    for palabra in cadena:##iteramos por la lista
        palabra.lower()##pasamos las palabras de la lista a minusculas, para qur todas las palabras sean iguales.
        if palabra in diccionario_conteo:##establecemos condición de que si la palabra ya esta, sumemos +1 el valor de esa clave 
            diccionario_conteo[palabra] +=1
        else:
            diccionario_conteo [palabra] =1##y si no está, que se añada esa calve, con contador de 1
    return diccionario_conteo
##Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
def remplazar_palabras (texto,palabra_antigua,palabra_nueva):
    cadena = texto.split()##pasamos el texto a lista
    lista_vacia = []##creamos una lista vacia
    for palabras in cadena:
        if palabras == palabra_antigua:##si encontramos la palabra antigua, añadimos la nueva a la nueva lista
            lista_vacia.append(palabra_nueva)            
        else:
            lista_vacia.append(palabras)##añadimos las demas palabras a la lista
    return ' '.join(lista_vacia)##cambiamos la lista a texto y decimos que nos devuelva ese texto
##Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
def eliminar_palabra(texto,palabra_eliminada):
    cadena = texto.split()##una vez mas, pasamos a lista el texto
    lista_vacia = []
    for palabrita in cadena:##iteramos
        if palabrita == palabra_eliminada:##si algun elemento de la lista es la palabra que queremos eliminar, pasamos
            continue
        else:
            lista_vacia.append(palabrita)##si no, la añadimos
    return ' '.join(lista_vacia)##devolvemos texto sin la palabra eliminada y con las demas palabras

def procesar_texto(texto,opcion,*args):##tendra el parametro texto asegurado, el parametro opción, para saber que opcion estamos elijiendo, y posibilidad de mas parametros segun la funcion que se elija.
    if opcion == "contar":##primra opcion es contar
        if len(args) !=0:##que no tiene parametros adicionales
            raise ValueError ("Para la opción 'Contar', no se necesitan parametros adicionales")##sacamos un error en caso de que se pongan parametros adicionales
        return contar_palabras(texto)##y que devuelva la funcion de contar
    elif opcion =="reemplazar":##segunda opcion es reemplazar
        if len(args)!=2:##que tendra dos argumentos adicionales a los ya establecidos
            raise ValueError("Para la opción 'reemplazar', solo hacen falta dos paramteros")##sacamos un error en caso de que se pongan distintos parametros adicionales a 2.
        return remplazar_palabras (texto,args[0],args[1])##que nos devuelva la funcion reemplazar,con el parametro ya establecido de texto, y dos parametros adicionales que podrá ser cualquier cosa.
    elif opcion == "eliminar":##por ultimo, opcion eliminar
        if len(args)!=1:##que tendra solo un parametro adicional
            raise ValueError("Para la opción 'eliminar', solo se necesita un parametro")##error en caso de parametros adicionales disitinto de 1
        return eliminar_palabra(texto,args[0])##que devuelva la funcion eliminar, que tendra el parametro texto, y uno adicional. 
    else:
        raise ValueError("opción no disponible. Las opciones son : 'contar', 'remeplazar' y 'eliminar'")##en caso de que no elijan las alguna de las tres opciones, indicar un error

texto = "Soy del Madrid y del Ateltico"
print(procesar_texto(texto,"contar"))
print(procesar_texto(texto,"reemplazar","Madrid","Barcelona"))
print(procesar_texto(texto,"eliminar","del"))


# %% [markdown]
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

# %%
import datetime
def noche_dia_tarde():
    hora_str = input(f"Establece la hora actual de esta manera: HH:MM:SS (por ejemplo, 14:30:00):")##solicitamos la hora al usuario, en el formato que queremos
    try:
        hora = datetime.datetime.strptime(hora_str,"%H:%M:%S").time()##con strptime, pasamos a formato datetime. con time nos quedamos solo con la hora
        if 0<=hora.hour < 6:##ponemos las condiciones segun las horas
            return "Es de noche"
        elif 6 <= hora.hour < 12:
            return "Es de día"
        elif 12 <= hora.hour < 18:
            return "Es tarde"
        elif 18 <= hora.hour < 24:
            return "Es de noche"
        else:
            return "Hora no válida"
    except ValueError:
        return "Por favor, introduce una hora válida en formato HH:MM:SS."##en caso de que no meta el formato deseado, saldra un error
    
print(noche_dia_tarde())

# %% [markdown]
# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son: - 0 - 69 insuficiente - 70 - 79 bien - 80 - 89 muy bien - 90 - 100 excelente

# %%
def notas (clasificacion):
    try:
        clasificacion = int(clasificacion)##hacemos que clasificacion se cambie siempre a tipo int.
    except ValueError:##ponemos manejo de errores en caso de que el valor que incluyan no pueda transformarse a valor numerico.
        return "Por favor, indica un valor numérico"        
    if clasificacion in range(0,70):##vamos poniendo las condiciones para que de las notas segun clasificacion
        return "Insuficiente"
    elif clasificacion in range(70,80):
        return "Bien"
    elif clasificacion in range (80,90):
        return "Muy bien"
    elif clasificacion in range (90,101):
        return "Excelente"
    else:
        return "Por favor, incluye un valor entre 0-100" ##si meten un valor que no esté en el rango, salta el error. 
Alumno1_nota = 90
print(notas(Alumno1_nota))

# %% [markdown]
# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

# %%
def figuras (figura,datos): ##definimos dos parametros
    if figura == "rectangulo": ##establecemos las condiciones del primer parametro, según cada figura
        (base,altura) = datos ##indicamos los datos necesarios en cada figura, en una tupla, y hacemos que eso sea el segundo parámetro
        return base * altura ##que nos devuelva el calculo necesario con los datos indicados en el segundo parametro
    elif figura == "circulo":##hacemos lo mismo poniendo mas condicionales segun la figura indicada, y los datos necesarios para cada figura, 
        (pi ,radio) = datos
        return pi * radio**2
    elif figura == "triangulo":
        (base,altura) = datos
        return 0.5 * (base*altura)
    else:
        return "Introduce una de estas opciones: rectangulo, circulo o triangulo"
    
print (figuras("rectangulo",(5,3)))
print (figuras("circulo",(3.14,4)))
print (figuras("triangulo",(2,6)))

# %% [markdown]
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente: 1.Solicita al usuario que ingrese el precio original de un artículo. 2.Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). 3.Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento. 4.Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 5.Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 6.Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

# %%
precio_articulo = float(input("Por favor, indica el precio del artículo comprado"))##preguntamos el precio del artículo
descuento = (input("¿tiene descuento el artículo?, responde con un si o no").lower())##preguntamos si tiene descuento, y para evitar errores lo pasamos a minusculas
descuento_valor = 0##creamos la variable descuento
try: ##manejamos errores por si se indica un valor no numerico
    if descuento == "si" or descuento == "sí":##si han indicado que tiene descuento, que lo indicquen
        descuento_valor = float(input("Por favor, introduce el valor del cupon descuento"))
    if descuento_valor >0:##si su descuento es mayor que 0 , restamos el precio menos el descuento
        precio_total = precio_articulo - descuento_valor
        print (f"El precio tras el descuento es: {precio_total}")##printeamos el precio final      
    else:
        print (f"El articulo no tiene descuento y su precio es: {precio_articulo}")##si han indicado que no tiene descuento, lo indicamos y sacamos su precio final
except ValueError:
    print ("Introduce un valor numerico valido")



