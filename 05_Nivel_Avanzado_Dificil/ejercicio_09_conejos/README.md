# Ejercicio 09: Conejos y Comedero (Examen Oficial Jovellanos)

## Enunciado Oficial
Simula un ecosistema donde conejos (hilos) comparten un comedero que se repone de forma regular.

---

## Requisitos Generales

### Del Sistema:
- Cada conejo es un hilo independiente
- El acceso al comedero debe estar sincronizado (sin race conditions)
- No se bloquea mas tiempo del imprescindible
- Manejo de excepciones para casos problematicos

### Del Comedero:
- **Raciones disponibles**: entero compartido
- **Total de comidas**: estadistica global
- **Lock**: para proteger la zona critica
- **Semaphore**: para gestionar y contar raciones disponibles

### De Cada Conejo:
- **5 intentos** de comer (tiempo de simulacion)
- **Espera aleatoria**: 0.5 a 2 segundos antes de cada intento
- **Si logra comer**:
  - Decrementa raciones disponibles
  - Incrementa total de comidas
  - Reinicia contador de fallos consecutivos
- **Fallo consecutivo**:
  - Si falla 3 veces seguidas, el conejo **MUERE**
  - Si logra comer, vuelve a 0 fallos

### Del Reponedor (hilo especial):
- Anade 3 raciones cada 2 segundos
- Realiza **5 reposiciones completas**
- Notifica al Semaphore cuando anade raciones

---

## Salida Final Requerida

Al terminar la simulacion, mostrar:

1. **Comidas por conejo**: cuantas veces comio cada uno
2. **Total de comidas dadas**: suma global de todas las comidas
3. **Raciones sin repartir**: cuantas quedaron en el comedero

---

## Ejemplo de Ejecucion

```
======================================================================
EXAMEN OFICIAL JOVELLANOS - CONEJOS Y COMEDERO
======================================================================

Configuracion:
  - 4 conejos (hilos independientes)
  - Cada conejo: 5 intentos de comer
  - Muerte: tras 3 fallos consecutivos
  - Reponedor: 3 raciones cada 2 segundos (5 ciclos)
  - Raciones iniciales: 0 (esperan reponedor)

[CONEJO] Conejo-Blanco nace
[CONEJO] Conejo-Gris nace
[CONEJO] Conejo-Cafe nace
[CONEJO] Conejo-Negro nace
[REPONEDOR] Iniciado

[CONEJO] Conejo-Blanco intento 1/5 (fallos: 0/3)
  [COMEDERO] Conejo-Blanco NO HAY COMIDA
[CONEJO] Conejo-Gris intento 1/5 (fallos: 0/3)
  [COMEDERO] Conejo-Gris NO HAY COMIDA
[REPONEDOR] Ciclo 1/5
[REPONEDOR] Anade 3 raciones. Total: 3

[CONEJO] Conejo-Blanco intento 2/5 (fallos: 1/3)
  [COMEDERO] Conejo-Blanco COME. Raciones restantes: 2
[CONEJO] Conejo-Gris intento 2/5 (fallos: 1/3)
  [COMEDERO] Conejo-Gris COME. Raciones restantes: 1
  
  ...

======================================================================
ESTADISTICAS FINALES
======================================================================

Comidas por conejo:
  Conejo-Blanco: 3 comidas
  Conejo-Gris: 2 comidas
  Conejo-Cafe: 2 comidas
  Conejo-Negro: 1 comidas

Total de comidas dadas: 8
Raciones sin repartir: 7
======================================================================
```

---

## Concepto Pedagogico

Este ejercicio demuestra:

1. **Orientacion a Objetos en Concurrencia**:
   - Clase `Comedero`: encapsula logica de recurso compartido
   - Clase `Conejo(Thread)`: herencia para crear hilos

2. **Sincronizacion Multiprimitiva**:
   - **Lock**: protege zona critica del comedero
   - **Semaphore**: gestiona recurso limitado (raciones)

3. **Coordinacion Compleja**:
   - Productor (reponedor) genera raciones
   - Multiples consumidores (conejos) compiten
   - Estados de conejo (vivo/muerto)

4. **Prevencion de Problemas**:
   - Evita race conditions con Lock
   - Evita deadlock con acquire(blocking=False)
   - Maneja ciclo de vida del conejo

5. **Patrones de Examen Real**:
   - Estructura similar a examen oficial
   - Estadisticas complejas
   - Ciclos de reintento y fallo
