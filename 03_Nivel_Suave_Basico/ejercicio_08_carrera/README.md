# Ejercicio 08: Carrera - Barrier

## Enunciado
Implementa una carrera donde 4 atletas deben empezar sincronizados usando una Barrier.

- 4 atletas quieren correr
- Cada uno se prepara (imprime "preparando")
- Los 4 esperan en la linea de salida
- Cuando todos estan listos (barrera), comienzan simultaneamente

## Concepto
Una `threading.Barrier(N)` sincroniza N hilos para que continuen juntos:

- Cada hilo llama a `barrier.wait()` para llegar a la barrera
- Se bloquean hasta que todos N hilos lleguen
- Cuando llegan todos, se despiertan y continuan simultaneamente

## Salida esperada
```
Atleta 1 preparando...
Atleta 2 preparando...
Atleta 3 preparando...
Atleta 4 preparando...
Atleta 1 listo en linea de salida
Atleta 2 listo en linea de salida
Atleta 3 listo en linea de salida
Atleta 4 listo en linea de salida
[Aqui TODOS esperan hasta que los 4 lleguen]
SALIDA! Atleta 1 corriendo
SALIDA! Atleta 2 corriendo
SALIDA! Atleta 3 corriendo
SALIDA! Atleta 4 corriendo
```

## Pistas
- Importa `from threading import Barrier`
- Crea con `barrier = Barrier(4)`
- Llama `barrier.wait()` cuando este listo
- NO continua hasta que todos llamen a wait()
