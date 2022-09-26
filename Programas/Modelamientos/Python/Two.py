
# ejercicio 5.1 de python clase ciencia datos frecode_camp

num = 0
tot = 0.0
while True :
    sval =input('enter a number: ')
    if sval == 'done' :
        break
    try:
        fval =float(sval)
    except:
        print('invalid input')
        continue
    print(fval)
    num = num +1
    tot = tot + fval

print('ALL DONE')
print(tot, num, tot/num)


# es un bucle con una entrada por teclado, una condicion que me permite salir y un try: que despues de un error de input
# permite continue con la entrada de datos.
