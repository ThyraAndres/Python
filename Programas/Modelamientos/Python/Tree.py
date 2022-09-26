xfile = open('billionaires.csv')
count = 0
for line in xfile:
    count = count + 1 # hace conteo de linea por linea
    line = line.rstrip() # borra espacios en blanco
    # if not line.startswith("Bill Gates") : de esta manera no me funciono, creo es porque se manejan demasiadas columnas
    if not 'Bill Gates' in line : # basicamente aca digo si no esta bill gates en line omitalo. por lo tanto solo va a imprimir
        continue                  # aquellas cadenas que contengan a bill Gates
    print(line)
    print('line count', count)

# .append() es un metodo de agregacion a la ultima posicion
stuff = list()
stuff.append('hola')
stuff.append(90)
print(stuff)

some = [1, 2, 3, 4,5, 6]
print(6 in some)    #pregunta si esta
print(7 not in some) #pregunta si no existe -> debe mandar un true, false

friends = ['x', 'v', 'c']
print("Lista desordenada: ", friends)
friends.sort()      # es un metodo para ordenar listas, digamos
print("Lista ordenada: ", friends)
print("imprimir por array: ", friends[2]) # debe devolverme x porque ya cambiamos el orden con .sort()s

fufu = 'hello my name'
juju = fufu.split()     # solo funciona con cadenas no puede ser un array, ademas esta funcion busca espacios
print("imprimimos con el len las posicionde de juju: ", len(juju), "posiciones ")
for w in juju:
    print(w)

loka = "hello;my;friend"
lo = loka.split()
print("imprimimos la cadena: " ,lo)
print(len(lo))
lc = loka.split(';')
print("se imprime quitando ; : ", lc)
print(len(lc))

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()  # estamos quitando los espacios nos devuelve 4 posiciones
print("ya se le quitaron espacios: ", pieces, len(pieces))
parts = pieces[3].split('-')    # de las 4 posiciones ahora volvemos a quitar algo, esta vez desde la posicon 3 vamos a quitar '-'
print("ahora le quitamos a la posicion 3 los - : ", parts, len(parts))
n = parts[1]    # aca ya le quitamos recordemos que ahora tenemos solo 2 posiciones [0,1], imprimimos posicion 1
print("imprimos posicion 1 de parts", n, "cantidad en n= parts[1]:", len(n))

#vamos a usar diccionarios y listas
#list()

lst1 = list()
lst1.append(21)
lst1.append(183)
print("aca nos debe imprimir 2 valores: ", lst1)
lst1[1] = 22
print("cambiamos 183 por 22: " , lst1)

#ahora vamos a usar diccionarios
#dict()

kuku = dict()
kuku['age'] = 12
kuku['course'] = 12
print("imprimimos el diccionario: ", kuku)
kuku['age'] = 11
print("cambiamos valor age 12 por 11, debe sobrescribir: ", kuku)

william = dict()
william['age'] = 20
william['programacion'] = 40
print("aca imprimimos el diccionario", william)
william['age'] = 21
print(william)

# conteo con un .get(x,y)
names = ['hola', 'viejo', 'como', 'esta', 'age']
for name in names:
    kuku[name] = kuku.get(name, 0) + 1
print("basicamente remplaze la funcion if, con el .get (age debe estar en aumento(anterior valor de age= 11, + 1 del metodo actual)): ", kuku)


# prueba, aca recibimos un texto y basicamente le quito los espacios para que quede como cadena. se hace usando el .split()
#despues lo guardo y en for le pregunto que toda palabra de la lista que se repita aumenta + 1. usamos el get(one_condition, two_condition)
print("--------------------", "Texto_Prueba")
counts = ("We are surrounded in our daily lives with computers ranging from laptops to cell phones. We can think of these computers as our personal assistants who can take care of many things onour behalf. The hardware in our current-day computers is essentially built to continuously ask us the question, What would you like me to do next?")
xi = counts.split()
kuku2 = dict()
for key in xi:
    kuku2[key] = kuku2.get(key, 0) + 1
print(kuku2)
        #print(key, counts[key]) # acordemonos que key son los nombrews, counts[key] son los valores

# items()
# se recorren valores en simultaneidad por ejemplo exa para names, y exu para #numeros o conteos.. etc... 
print("-------------------", "Items()")
example = {'chuck':1 , 'fuck':2 , 'fack':3}
for exa,exu in example.items():
    print(exa,exu)
