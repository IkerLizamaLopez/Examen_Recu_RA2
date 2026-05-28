# Ejercicio 18: El Comedero de Mascotas con Limite de Intentos (Condition + Timeout)

### Enunciado
Implementa una simulacion en la que varios animales acuden a alimentarse a un plato de comida compartido con aforo restringido.
- El comedero tiene capacidad para un maximo de **2 animales simultaneos**.
- Habra 5 animales (hilos) que sienten hambre a intervalos aleatorios y quieren comer.
- Cuando un animal tiene hambre, intenta ocupar un puesto en el comedero:
  - Si el comedero esta lleno (ya hay 2 animales comiendo), el animal espera utilizando `wait(timeout=1.0)` para dar un margen de tiempo.
  - El animal dispone de un **maximo de 3 intentos** para intentar comer.
  - Si en un intento se supera el timeout de 1.0 segundos y sigue lleno, el animal incrementa su contador de intentos, se retira un momento a pasear (con un breve sleep) y vuelve a intentarlo.
  - Si tras agotar sus 3 intentos no ha conseguido comer, se rinde y se va a dormir resignado.
- Utiliza `threading.Condition` con paso de parametro `timeout` en `wait()` para controlar esta espera limitada.
