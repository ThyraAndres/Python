data = 'From stephen.marquard@uct.ac.za Sat Jan509:14:16 2008'
atpos = data.find('@') #cuenta las posiciones hasta el @
print("1er find(): ", atpos)
sspos = data.find(' ', atpos) #hay que tener en cuenta el espacio entre ''
print("2er find(): ", sspos)
host = data[atpos+1 : sspos] #concatena con find creo paraunir ambos e imprimir hasta la posicion 31.(a) desde la 21(d)
print("Concatenamos y mandamos dentro de data[] ambos .find guardados: ", host)

#split divide lineas
line = 'From stephen.marquard@uct.ac.za Sat Jan509:14:16 2008'
print("Completo: ",line)
word =line.split()
print("1er split:", word) #recordemos que el split me divide la cadena en subcadenas
email =word[1]
print("subdvision guardada, nos paramos en la posicion[1]: ", email)
pieces = email.split('@') # subdividomos dependiendo al @
print("Nos paramos en la posicion 1 y la volvemos a subdividr: ", pieces[1])

#usamos import re y expresiones regulares. pilas con esto
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan509:14:16 2008'
y = re.findall('@([^ ]*)', lin) #dice busquemos desde @, si lo encuentra luego extraigame[busquemos caracteres que no esten en blanco]
print(y)                        #el espacio [^ ] forma no blanco todos menos los espacios en blanco. *->recorrer hasta que encuentre un
                                #espacio en blanco que lo detendra
                                #otra forma mas refinada es: '^From .*@([^ ]*)' si no se obtiene la linea se omite, si no se reccore normal

linda = 'ajajajaja $10.0 asd'
si = re.findall('\$([0-9.]+)',linda) # el 0-9 es para indicar q es numero y + para que me devulve este numero
print(si)


 #Libreria socket a investigar
import socket
xa = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#xa.connect(('data.pr43.org', 80))


# funcion tells numerica que evalua simple ASCII character
print(ord('H'))
print(ord('e'))
print(ord('\n')) # esto significa nueva linea, su valor es 10
print(ord('c'))  # a es 97, b 98, c 99

# b significa bytes
x = b'abc'  #variable bytes, estos bytes pueden tener un tamaño entre 3 a 12 bytes de longitud.
print(type(x))

# u significa str
xx = u'abc'
print(type(xx))

# recv -->
# decode -->

"""
HOST = 'data.pr4e.org'
PORT = 80
mysock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock1.connect(HOST, PORT)
cmd = 'GET http://data.pr4e.org/romeo.txt HTPP/1.0\n\n'.encode()
mysock1.send(cmd)
"""

import socket

HOST = 'data.pr4e.org'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
cmd = 'GET http://data.pr4e.org/romeo.txt HTPP/1.0\n\n'.encode()
s.send(cmd)
ss =s.send(cmd)
print('cmd: ', ss)

while True:
    data = s.recv(512)
    if (len (data)<1):
        break
    print('decode(): ', data.decode())
s.close()

""" se usarara la libreria creo urllib.

"""

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print("liberia urllib: ",line.decode().strip())

from bs4 import BeautifulSoup
url = input('Enter - ')
html= urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

#Retrieve all of the anchor tags
tags= soup('a')
for tag in tags:
   print(tag.get('href', None))
