from threading import Thread, Condition
import time

# Stocks
pieza_A = 0
pieza_B = 0
pieza_C = 0
productos = 0

multiplicador = 1.0

condition = Condition()

def productor_A():
    global pieza_A

    while True:
        time.sleep(2 / multiplicador)

        with condition:
            pieza_A += 1

            total = pieza_A + pieza_B + pieza_C

            print(f"[Productor A] Produjo 1 pieza A. Almacén: {total} piezas")
            condition.notify_all()


def productor_B():
    global pieza_B

    while True:
        time.sleep(3 / multiplicador)

        with condition:
            pieza_B += 1

            total = pieza_A + pieza_B + pieza_C

            print(f"[Productor B] Produjo 1 pieza B. Almacén: {total} piezas")

            condition.notify_all()


def productor_C():
    global pieza_C

    while True:
        time.sleep(1.5 / multiplicador)

        with condition:
            pieza_C += 1

            total = pieza_A + pieza_B + pieza_C

            print(f"[Productor C] Produjo 1 pieza C. Almacén: {total} piezas")

            condition.notify_all()

def ensamblar_producto():
    global pieza_A, pieza_B, pieza_C, productos

    while True:

        with condition:

            while not (pieza_A >= 2 and pieza_B >= 1 and pieza_C >= 3):
                print("[Ensamblador] No hay suficientes piezas, esperando...")
                condition.wait()

            # Consumir piezas
            pieza_A -= 2
            pieza_B -= 1
            pieza_C -= 3

        # Simular tiempo de ensamblaje
        time.sleep(1)

        productos += 1

        total = pieza_A + pieza_B + pieza_C

        print(f"[Ensamblador] Producto nuevo fabricado. "
              f"Productos: {productos}, Almacén: {total}")
