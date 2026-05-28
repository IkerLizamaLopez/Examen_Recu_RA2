# Ejercicio 21: El Comedero de Conejos (Examen Oficial)

### Enunciado
Vamos a simular un ecosistema donde hay conejos y cierta comida en un comedero que se repone de forma regular.

Requisitos generales:
- Cada conejo es un hilo.
- El acceso al comedero para comer o para sacar estadisticas debe estar sincronizado.
- No se permiten las condiciones de carrera.
- No se bloquea mas tiempo del imprescindible.

Requisitos del comedero:
- Tiene unas "raciones disponibles" (entero compartido).
- Un total de comidas (estadistica).
- Lock para proteger la zona critica.
- Semaforo para mostrar las raciones disponibles.

Requisitos del conejo:
- Cada conejo hace 5 intentos de comer (es nuestro tiempo de simulacion).
- Espera un tiempo aleatorio corto (de 0.5 a 2 segundos) antes de cada intento.
- Si come, las raciones disponibles decrementan, y la suma total de comidas crece por una.
- Si despues de 3 intentos seguidos, no consigue comer, se "muere" y termina el hilo.
- Si consigue comer, los intentos se reinician (vuelven a ser 3).

Requisitos del reponedor:
- Hay un hilo "reponedor", que añade 3 raciones cada 2 segundos (5 reposiciones completas para la simulacion).

Al final se muestra:
1. Cuantas veces comio cada conejo.
2. Total de comidas dadas en global.
3. Cuantas raciones se han quedado sin repartir.
