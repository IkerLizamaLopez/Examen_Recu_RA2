# Guia de Uso: Carpetas y Ejercicios

## Estructura Total del Repositorio

### 📁 01_Ejemplos_y_Clases_Originales/
- Contenido **original de clase**: lo que se hizo en sesiones presenciales
- **No modificar** - solo para referencia histórica
- Ejemplos básicos y proyectos iniciales

### 📁 02_Coleccion_20_Ejercicios_Concurrencia/ (COLECCIÓN OFICIAL)
- **25 ejercicios resueltos profesionalmente**
- Implementaciones **completas y optimizadas**
- Cada ejercicio en su propia carpeta con README + main.py
- **Para estudiantes avanzados** que ya entienden conceptos básicos
- Ejercicio 21 es el **EXAMEN OFICIAL JOVELLANOS** (solución profesional)

### 📁 03_Nivel_Suave_Basico/ (NUEVO - PRACTICA BASICA)
- **10 ejercicios muy simples**
- Un concepto por ejercicio
- **Para aprender de cero** o como calentamiento
- Código directo y fácil de entender
- Ideal para: "¿por qué sale mal esto?" → busca en este nivel

### 📁 04_Nivel_Intermedio_Medio/ (NUEVO - PRACTICA INTERMEDIA)
- **15 ejercicios de dificultad media**
- Combinaciones de primitivas
- **Para entender patrones**
- Construcción sobre conceptos básicos
- Ideal para: "¿cómo resuelvo esto?" → busca aquí

### 📁 05_Nivel_Avanzado_Dificil/ (NUEVO - PRACTICA AVANZADA)
- **10 ejercicios profesionales**
- Problemas clásicos de concurrencia
- **Orientados a examen**
- Ejercicio 09 es el **EXAMEN JOVELLANOS** (versión educativa con clases)
- Ideal para: "¿cómo domino esto?" → aquí es el lugar

---

## Relación Entre Carpetas 02 y 05

### Ejercicios Relacionados (similar concepto, diferente enfoque)

| Concepto | Carpeta 02 | Carpeta 05 | Diferencia |
|----------|-----------|-----------|-----------|
| Filósofos | Ejercicio 03 | Ejercicio 01 | 02 es más optimizado; 05 es más educativo |
| Barbero | Ejercicio 11 | Ejercicio 02 | 02 usa más primitivas; 05 es más simple |
| Puente | Ejercicio 12 | Ejercicio 03 | 02 con prioridades; 05 básico |
| Parking | Ejercicio 17 | Ejercicio 04 | 02 VIP+standard; 05 simple |
| Productor-Consumidor | Ejercicio 08 | Ejercicio 05 | 02 real; 05 educativo |
| Conejos (EXAMEN) | **Ejercicio 21** | **Ejercicio 09** | **Ambos son válidos - ver sección EXAMEN** |

### Ejercicios Únicos de Carpeta 05
- Ejercicio 06: Fabrica Ensamblador
- Ejercicio 07: Carrera con Prioridad
- Ejercicio 08: Deadlock Recovery
- Ejercicio 10: Transacciones Bancarias

---

## ⚠️ EXAMEN OFICIAL JOVELLANOS - CONEJOS

### Dos Versiones Disponibles:

#### Opción A: Profesional (Carpeta 02, Ejercicio 21)
- **Usar si**: Quieres ver código production-ready
- **Ventajas**: Optimizado, con clases complejas
- **Detalles**: Usa `Semaphore.acquire(blocking=False)`
- **Cuando usar**: Para entregar un examen profesional

#### Opción B: Educativa (Carpeta 05, Ejercicio 09)
- **Usar si**: Quieres entender cada paso
- **Ventajas**: Mejor comentado, estructura clara
- **Detalles**: Enfoque paso a paso con prints detallados
- **Cuando usar**: Para aprender cómo resuelto

**AMBAS SON VÁLIDAS** - El examen acepta cualquier implementación correcta.

---

## 📚 Ruta de Estudio Recomendada

### Opción 1: Principiante → Experto
```
1. Nivel 03 Basico (10 ejercicios) ........... 3-4 horas
2. Nivel 04 Intermedio (15 ejercicios) ..... 6-8 horas
3. Nivel 05 Avanzado (10 ejercicios) ....... 4-6 horas
   ↓
   Total: 13-18 horas de práctica intensiva
4. Ver soluciones Nivel 02 para comparar
5. PRACTICAR EXAMEN: Nivel 05 Ejercicio 09
```

### Opción 2: Aprendizaje Rápido
```
1. Revisar Nivel 02 Ejercicio 21 (EXAMEN) . 30 minutos
2. Practicar Nivel 05 Ejercicio 09 ......... 2 horas
3. Hacer Nivel 04 ejercicios relacionados . 4 horas
4. Dominar cada ejercicio hasta resolver sin ayuda
```

### Opción 3: Experto (Verificación)
```
1. Nivel 02 Coleccion Completa (referencia)
2. Intentar resolver Nivel 05 sin consultar Nivel 02
3. Comparar implementaciones
```

---

## 🎯 Cómo Usar Cada Carpeta

### Si estás EMPEZANDO:
→ Empieza con **Nivel 03** (Carpeta 03_Nivel_Suave_Basico)
- Cada ejercicio es muy simple
- Aprenderás 1 concepto por ejercicio
- Sin confusiones

### Si ya CONOCES básicos:
→ Salta a **Nivel 04** (Carpeta 04_Nivel_Intermedio_Medio)
- Ejercicios realistas
- Combinaciones de primitivas
- Prepare para examen

### Si NECESITAS DOMINAR:
→ Ve a **Nivel 05** (Carpeta 05_Nivel_Avanzado_Dificil)
- Problemas clásicos
- Examen oficial
- Patrones avanzados

### Si NECESITAS REFERENCIA:
→ Consulta **Colección 02** (Carpeta 02_Coleccion_20_Ejercicios_Concurrencia)
- Soluciones profesionales
- Implementaciones optimizadas
- Casos de examen reales

---

## ✅ Checklist de Preparación para Examen

- [ ] Entender Nivel 03 (básicos)
- [ ] Completar Nivel 04 (intermedios)
- [ ] Resolver Ejercicio 09 de Nivel 05 (CONEJOS) sin ayuda
- [ ] Verificar con Ejercicio 21 de Carpeta 02
- [ ] Practicar 2-3 variaciones del examen
- [ ] Temporal: Cambiar nombres, números, etc.
- [ ] Listo para examen ✨

---

## 📞 Preguntas Frecuentes

**P: ¿Hay duplicados? ¿Hago todos?**
R: No son duplicados exactos. Los de Nivel 05 son educativos; los de Colección 02 son profesionales. Practica Nivel 05 y consulta Colección 02 si necesitas idea.

**P: ¿Qué hago para el examen?**
R: Domina el Ejercicio 09 de Nivel 05 (versión educativa) o 21 de Colección 02 (versión pro).

**P: ¿Cuánto tiempo necesito?**
R: 13-18 horas de práctica intensiva si empiezas de cero.

**P: ¿Los nuevos (03, 04, 05) son parte de la clase?**
R: NO - los nuevos son EXTRA que preparé para ti. La clase usa Colección 02 y Ejemplos 01.

**P: ¿Cuál es mejor: Colección 02 o Nivel 05?**
R: Depende: Colección 02 si necesitas ver "cómo lo hacen los expertos"; Nivel 05 si necesitas aprender paso a paso.
