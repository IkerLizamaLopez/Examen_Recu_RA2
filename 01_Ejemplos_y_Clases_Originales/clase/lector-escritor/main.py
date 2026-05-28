from threading import Thread, Lock, Event
import time

valor = 0
lock = Lock()
evento = Event()

def lector():
    global valor
    while not evento.is_set():
        evento.wait()
    while True:
        with lock:
            with open("compartido.txt", "r") as file:
                try:
                    valor = int(file.read())
                    print("El lector ha leído", valor)
                except Exception as e:
                    print(e)
        time.sleep(2)


def escritor():
    global valor
    while True:
        with lock:
            valor = valor + 1
            with open("compartido.txt", "w") as file:
                try:
                    file.write(str(valor))
                    print("El escritor ha escrito", valor)
                    evento.set()
                except Exception as e:
                    print(e)
        time.sleep(0.2)

Thread(target=lector).start()
Thread(target=escritor).start()
