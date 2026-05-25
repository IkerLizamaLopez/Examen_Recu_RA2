import time
import random
from threading import Thread
from parking import Parking
from coche import Coche


def main():
    parking = Parking(plazas=3, precio=2.5)

    coches = []
    for _ in range(10):
        coche = Coche(parking)
        coches.append(coche)

    hilos = []
    for coche in coches:
        hilo = Thread(target=coche.aparcar, daemon=True)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()
        time.sleep(random.uniform(0.1, 0.5))

    for hilo in hilos:
        hilo.join()

    print(f"\nTotal recaudado: {parking.total_acumulado:.2f}€")


if __name__ == "__main__":
    main()