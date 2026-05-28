# Ejercicio 03: Lector-Escritor

## Enunciado
Implementa el problema clasico lector-escritor.

- Multiples lectores pueden leer simultaneamente
- Un escritor excluye a todos (lectores y otros escritores)
- Usa Locks y variables de estado

## Concepto
Coordinacion compleja: permitir concurrencia donde es seguro (multiples lectores)
pero exclusion donde es necesario (escritor).
