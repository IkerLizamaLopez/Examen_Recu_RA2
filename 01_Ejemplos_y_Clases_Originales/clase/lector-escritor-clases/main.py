from escritor import Escritor
from lector import Lector
from fichero import Fichero
from threading import Thread

fichero = Fichero(ruta="numero.txt")

escritor = Escritor(fichero, 0.2)
lector = Lector(fichero, 2)

Thread(target=escritor.escribir).start()
Thread(target=lector.leer).start()