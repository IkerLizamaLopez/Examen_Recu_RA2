from threading import Thread, Lock, Condition
import time
import random

# ---------------- VARIABLES COMPARTIDAS ----------------

lock = Lock()
condition = Condition(lock)

raciones_disponibles = 3
total_comidas = 0
total_raciones_creadas = 3

SIMULACION_ACTIVA = True

# ---------------- CONEJO ----------------

def conejo(id_conejo):

    global raciones_disponibles
    global total_comidas

    comidas_conejo = 0
    fallos_seguidos = 0

    for intento in range(5):

        time.sleep(random.uniform(0.5, 2))

        with condition:

            if raciones_disponibles > 0:

                raciones_disponibles -= 1
                total_comidas += 1
                comidas_conejo += 1

                fallos_seguidos = 0

                print(f"[Conejo {id_conejo}] COMIÓ")
                print(f"Raciones restantes: {raciones_disponibles}")

            else:

                fallos_seguidos += 1

                print(f"[Conejo {id_conejo}] NO pudo comer")
                print(f"Fallos seguidos: {fallos_seguidos}")

                if fallos_seguidos >= 3:
                    print(f"[Conejo {id_conejo}] MURIÓ")
                    break

    print(f"[Conejo {id_conejo}] Total comidas: {comidas_conejo}")


# ---------------- REPONEDOR ----------------

def reponedor():

    global raciones_disponibles
    global total_raciones_creadas
    global SIMULACION_ACTIVA

    for i in range(5):

        time.sleep(2)

        with condition:

            raciones_disponibles += 3
            total_raciones_creadas += 3

            print("\n[REPONEDOR] Añadió 3 raciones")
            print(f"Raciones disponibles: {raciones_disponibles}\n")

            condition.notify_all()

    SIMULACION_ACTIVA = False


# ---------------- MAIN ----------------

conejo_hilos = []

# Crear 3 conejos
for i in range(3):

    t = Thread(target=conejo, args=(i+1,))
    conejo_hilos.append(t)
    t.start()

# Crear reponedor
t_reponedor = Thread(target=reponedor)
t_reponedor.start()

# Esperar a todos
for t in conejo_hilos:
    t.join()

t_reponedor.join()

# ---------------- RESULTADOS ----------------

print("\n===== RESULTADOS FINALES =====")

print(f"Total comidas realizadas: {total_comidas}")
print(f"Raciones sobrantes: {raciones_disponibles}")
print(f"Raciones creadas: {total_raciones_creadas}")