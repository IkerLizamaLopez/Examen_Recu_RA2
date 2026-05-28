# Ejercicio 12: Puente Estrecho con Turno y Prioridad (Condition)

### Enunciado
Implementa la simulacion de un puente estrecho de un unico carril.
- Hay vehiculos que quieren cruzar del **Norte al Sur** y otros del **Sur al Norte**.
- Al ser de carril unico, **solo pueden cruzar coches en un mismo sentido al mismo tiempo** (si hay coches cruzando hacia el Norte, los coches del Sur deben esperar, y viceversa).
- Para evitar la hambruna (starvation) de una de las direcciones, implementa un limite de paso consecutivo:
  - No pueden cruzar mas de 3 coches seguidos en la misma direccion si hay coches esperando en el sentido contrario.
  - Cuando se alcance este limite de 3 coches consecutivos y haya coches del sentido opuesto haciendo cola, se debe forzar el cambio de sentido y darles el turno de forma limpia.
- Utiliza `threading.Condition` para sincronizar las esperas de los vehiculos y controlar los contadores de coches cruzando, coches consecutivos y sentido actual.
