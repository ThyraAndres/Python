fname = input("Enter file: ")
if len(fname) < 1: fname ="Not Exist"
hand = open(fname)
di = dict()

#el archivo recibido entra al for para que posicion a posicion quite espacios en blanco
for lin in hand:
    lin = lin.rstrip()  # quita los espacios en blanco a la derecha
    # print(lin)

    wsd = lin.split()   # quita todos los espacios en blanco
        # print(wsd)
    for w in wsd:   #ahora vamos a usar el diccionario
        """
        # if the key is not there the count is zero
        oldcount = di.get(w, 0) # recupera lo datos, si no estan manda 0
        print(w, "old ", oldcount)
        newcount = oldcount + 1     #crea un nuevo contador si existe el dato
        di[w] = newcount    # se actualiza este dato puesto que si existe
        print(w, "new ", newcount)
        """
        #recupere, cree, actualize el contador todo en una sola linea
        di[w] = di.get(w,0) + 1 # resume todo los pasos de la linea 14 a la 17
        #print(w, 'new', di[w])
#print(di)

langest = -1
theworld = None
for k,v in di.items():
    if v > langest :
        langest = v
        theworld = k
print(theworld, langest)
