# Ejercicio 09: Conejos y Comedero (Examen Jovellanos - OFICIAL)

## Enunciado Oficial
Simular un ecosistema donde hay conejos y cierta comida en un comedero que se repone de forma regular.

### Requisitos Generales:
- Cada conejo es un hilo
- El acceso al comedero para comer o sacar estadisticas debe estar sincronizado
- No se permiten condiciones de carrera
- Manejo de excepciones para casos problematicos

### Requisitos del Comedero:
- Tiene unas "raciones disponibles" (entero compartido)
- Un total de comidas (estadistica)
- Lock para proteger la zona critica
- Semaphore para mostrar las raciones disponibles

### Requisitos del Conejo:
- Cada conejo hace 5 intentos de comer (es nuestro tiempo de simulacion)
- Espera un tiempo aleatorio corto (de 0.5 a 2 segundos) antes de cada intento
- Si come, los intentos se reinician (vuelven a ser 3)
- Si despues de 3 intentos seguidos no consigue comer, se "muere" y termina el hilo

### Requisitos del Reponedor:
- Hay un hilo reponedor que anade 3 raciones cada 2 segundos
- Realiza 5 reposiciones completas para la simulacion

### Salida Esperada (Al Final):
1. Cuantas veces comio cada conejo
2. Total de comidas dadas en global
3. Cuantas raciones se han quedado sin repartir
