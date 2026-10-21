# Ingeniería Electrónica (UNSAM) — repo de estudio

Material de cátedra, resúmenes, prácticas y parciales de cada materia. Lo uso para
estudiar: cuando pido resolver algo, quiero aprender a hacerlo como lo pide la cátedra.

## Cómo resolver ejercicios, prácticas y parciales (todas las materias)

1. **Solo con los contenidos de la materia.** Antes de resolver, buscar en la carpeta de
   la materia qué herramientas dio la cátedra para ese tema (teoría, diapositivas,
   apuntes, "definiciones y propiedades", resúmenes `.md`). No usar métodos que la
   materia no da o que todavía no entraron en ese parcial (en Análisis: nada de Taylor,
   integrales ni L'Hôpital antes de la práctica 7). Si algo sale más rápido con una
   herramienta de afuera, resolverlo igual con la de la materia.
2. **Como lo espera la cátedra.**
   - Mirar los parciales resueltos y corregidos de la misma materia (las marcas del
     docente dicen qué se premia y qué se baja) y las guías `guia-*.md`, que tienen el
     patrón de cada ejercicio.
   - Usar la notación de la cátedra: $\operatorname{sen}$, $\operatorname{Dom}(f)$,
     "recta tangente en $(a, f(a))$", etc.
   - "JUSTIFICÁ TODAS LAS RESPUESTAS": cada paso nombra el teorema, la propiedad o la
     definición que usa, y cada conclusión va en palabras.
   - Responder exactamente lo que se pregunta y cerrar con la respuesta destacada.
3. **Fórmula antes que números.** En cada paso: nombre de la herramienta → fórmula en
   símbolos → despeje → reemplazo numérico → resultado. Nunca el número primero.
4. **Verificar y descartar.** Reemplazar el resultado, chequear dominio y unidades, y
   explicar por qué se descarta cada solución que no sirve.
5. **Si el repo tiene la resolución de ese mismo ejercicio**, no copiarla: resolver
   primero y después comparar, marcando errores o lo que le faltó para la nota máxima.
6. **Formato:** español rioplatense (voseo, como las consignas). LaTeX se ve renderizado
   con KaTeX: nunca subíndices ni superíndices dentro de `\text{}`; fórmulas químicas en
   `\mathrm{}` (`\text{g de } \mathrm{KO_2}`, no `\text{g de KO_2}`).

## Dónde está el material de cada materia

| Materia | Teoría de la cátedra | Ejercitación | Resúmenes / guías propias | Parciales |
| --- | --- | --- | --- | --- |
| Análisis Matemático (IAM, comisión M1) | `teoria/Material de lectura/definiciones y propiedades practica N.pdf`, `teoria/Pases de diapositivas M1/`, apuntes de Ceretani y Comas | `practicas/N) ....pdf` | `Teoria-2do-parcial.md`, `Formulario.md`, `Limites-Trucos.md`, `guia-2do-parcial.md` | `Parciales/<N> parcial/` (`para resolver/` y `otros/` con resueltos) |
| Química General | `Quimica/practicas/teoria/` (clases en PDF), `Tabla termodinamica.pdf` | `practicas/SERIE N_2C_2026.pdf`, `Laboratorio/` | `Resumen-Serie-N.md`, `Resumen-Parcial-N.md`, `guia-2do-parcial.md` | `Parciales/Nª Parcial/` (`Para resolver/`, `Resueltos/`) |
| Física I | `Fisica-I/apuntes/<N-tema>/` | `practicas/Guias de Problemas.pdf` | — | — |
| CTS | `CTS/Contenidos/Unidad-N/` | — | `Resumenes-unidad-N.md`, `Resumen-Parcial-Conceptos.md`, `Guia-Estudio-Parcial-1.md`, `Parciales-Resueltos.md` | `Parciales/` (imágenes) |

`Fisica-I/practicas/Guías resueltas (2c 2018) Física I.pdf` es de otra cursada: sirve
para comparar, no como referencia de método.

## Trabajos escritos (TPs, informes)

Todo dato que se agregue va con una fuente real que se haya abierto y verificado, citada
con autor, medio, fecha y URL. Si una fuente no se pudo verificar, avisar en vez de citarla.

## "El parcial / archivo que estoy viendo"

Si no llega la selección del editor (pasa con PDFs e imágenes), la pestaña activa de VS Code
está en `%APPDATA%/Code/User/workspaceStorage/e868a9ed50afaf63f49926ff7e030be9/state.vscdb`
(SQLite, tabla `ItemTable`, clave `memento/workbench.parts.editor`): el primer índice de
`mru` en el grupo activo es la pestaña que tengo al frente.
