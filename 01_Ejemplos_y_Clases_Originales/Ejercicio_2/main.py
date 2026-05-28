from threading import Thread
from coche import Coche
from parking import Parking
import time
import random

def main():
    parking = Parking(plazas=3,precio=2.5)#Llamamos al parking 
    coches = [Coche(parking) for _ in range (10)] #Llamamos pra que entren los coches 

    for c in coches:
        c.join()
        

    for c in coches:
        c.start()
        time.sleep(random.uniform(1, 1.5))

if __name__ == "__main__":
    main()