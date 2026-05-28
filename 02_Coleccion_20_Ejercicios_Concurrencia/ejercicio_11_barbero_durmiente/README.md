# Ejercicio 11: El Barbero Durmiente (Sincronizacion Clasica)

### Enunciado
Resuelve el problema clasico de sincronizacion del Barbero Durmiente.
- En una barberia hay:
  - 1 barbero que atiende a los clientes en su silla de afeitar.
  - 3 sillas de espera en la sala de espera.
- La dinamica del negocio es la siguiente:
  - Si no hay clientes en la barberia, el barbero se sienta en su silla de afeitar y se queda profundamente dormido.
  - Cuando llega un cliente:
    - Si el barbero esta durmiendo, lo despierta y se le corta el pelo de inmediato.
    - Si el barbero esta ocupado afeitando a alguien y hay sillas libres en la sala de espera, el cliente se sienta a esperar su turno.
    - Si el barbero esta ocupado y todas las sillas de espera estan llenas, el cliente se marcha enfadado de la tienda sin cortarse el pelo.
  - Al terminar el corte, el barbero despide al cliente y comprueba si hay clientes esperando en la sala. Si los hay, llama al siguiente; si no, se vuelve a dormir.
- Resuelve esta coordinacion de hilos utilizando `threading.Condition` y variables de estado para las sillas y los clientes en espera.
