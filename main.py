from fabrica import productor_A,productor_B,productor_C ,ensamblar_producto
from threading import Thread

def main():
    hilo_A = Thread(target=productor_A).start()
    hilo_B = Thread(target=productor_B).start()
    hilo_C = Thread(target=productor_C).start()

    ensamblar = Thread(target=ensamblar_producto).start()

if __name__ =="__main__":
    main()