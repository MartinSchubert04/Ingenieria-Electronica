# Resumen Química General – Primer Parcial

> **Alcance confirmado por el Cronograma 2C 2026**: el 1er Parcial (31 de agosto) evalúa las **Series 1 a 4**:
> Serie 1 (Átomos y configuración electrónica) → Serie 2 (Lewis, TREPEV y Polaridad) → Serie 3 (Interacciones intermoleculares) → Serie 4 (Soluciones).
> Fuentes: carpetas `teoria/` (Clase 1 a 5, Lewis y resonancia) y `practicas/` (Series 1 a 4) + Programa de la materia.

---

# SERIE 1 – Átomos, iones y configuración electrónica

> Temas: Estructura atómica. Cuantización de la energía. Orbitales atómicos. Números cuánticos. Estructura electrónica. Fenómenos de emisión y absorción atómica. Iones más estables para elementos representativos según CEE. Iones más estables para elementos de transición.

## Constantes y datos útiles

| Constante | Valor |
|---|---|
| $h$ (Planck) | $6,63\times10^{-34}\ J.s$ |
| $c$ (luz) | $3,0\times10^{8}\ m/s$ |
| $N_A$ (Avogadro) | $6,022\times10^{23}\ mol^{-1}$ |
| $R_H$ (Rydberg) | $1,097\times10^{7}\ m^{-1}$ ($=2,18\times10^{-18}\ J$) |
| $1\ \text{Å}$ | $10^{-10}\ m$ |
| $1\ nm$ | $10^{-9}\ m$ |

## 1. Cuantización de la energía

$$E = h\nu = h\frac{c}{\lambda}$$

- $\nu$ = frecuencia (Hz), $\lambda$ = longitud de onda (m)
- Energía **por mol** de fotones/átomos: multiplicar por $N_A$

$$E_{mol} = E_{foton} \times N_A$$

Cuidado con las unidades: $\lambda$ en metros $\to$ $E$ en Joule $\to$ pasar a kJ/mol dividiendo por 1000. A menor $\lambda$ (o mayor frecuencia) $\Rightarrow$ mayor energía del fotón.

**Ejemplo** (luz amarilla de sodio, $\lambda=589\ nm$):
$$E = 6,63\times10^{-34}\times\frac{3,0\times10^{8}}{589\times10^{-9}} = 3,38\times10^{-19}\ J$$
$$E_{mol} = 3,38\times10^{-19}\times6,02\times10^{23} = 203,3\ \frac{kJ}{mol}$$

## 2. Espectro de emisión/absorción del hidrógeno

- **Emisión**: el electrón cae de un nivel superior a uno inferior y libera un fotón (línea de emisión).
- **Absorción**: el electrón sube de nivel absorbiendo un fotón de energía exacta.
- Ecuación de Rydberg para las transiciones del H:

$$\frac{1}{\lambda} = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right), \quad n_1 < n_2$$

- La serie de Balmer (líneas visibles: 410, 434, 486, 656 nm) corresponde a transiciones que terminan en $n_1=2$.
- A mayor diferencia de energía entre niveles $\Rightarrow$ mayor energía y menor $\lambda$ del fotón emitido/absorbido.
- Un experimento de lámpara + prisma muestra que la energía del átomo está **cuantizada**: solo existen ciertos niveles permitidos.

## 3. Números cuánticos

| Número | Símbolo | Qué describe | Valores posibles |
|---|---|---|---|
| Principal | $n$ | Nivel de energía / tamaño del orbital | $1, 2, 3, \dots$ |
| Secundario (azimutal) | $l$ | Forma del orbital (subnivel) | $0$ a $n-1$ ($s=0, p=1, d=2, f=3$) |
| Magnético | $m_l$ | Orientación espacial del orbital | $-l$ a $+l$ |
| Espín | $m_s$ | Sentido de giro del electrón | $+\tfrac12$ o $-\tfrac12$ |

## 4. Formas de los orbitales

- **s**: esférico, 1 orientación.
- **p**: dos lóbulos ("8"), 3 orientaciones ($p_x, p_y, p_z$), cada uno con un plano nodal.
- **d**: 5 orientaciones ($d_{xy}, d_{xz}, d_{yz}, d_{x^2-y^2}, d_{z^2}$).
- **f**: 7 orientaciones (formas más complejas).
- El tamaño del orbital aumenta con $n$ (ej. $1s < 2s < 3s < 4s$).

## 5. Reglas para armar la configuración electrónica

- **Principio de Aufbau** (regla de las diagonales): orden de llenado
$$1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p,\ 5s,\ 4d,\ 5p,\ 6s,\ 4f,\ 5d,\ 6p,\dots$$
- **Principio de exclusión de Pauli**: cada orbital admite máximo **2 electrones**, con espines opuestos.
- **Regla de Hund**: en subniveles degenerados (ej. los 3 orbitales $p$), los electrones ocupan primero orbitales distintos con espín paralelo antes de aparearse.
- Un orbital **no es** una trayectoria fija; describe una región de probabilidad. La mecánica cuántica **sí** es la herramienta apropiada para describir la materia a nivel atómico.

**Ejemplo** – diagrama de orbitales del Na ($Z=11$):

$$1s\!\uparrow\downarrow \quad 2s\!\uparrow\downarrow \quad 2p\!\uparrow\downarrow\ \uparrow\downarrow\ \uparrow\downarrow \quad 3s\!\uparrow$$

## 6. Configuración electrónica (CE) y externa (CEE)

- **CE**: se listan todos los subniveles ocupados siguiendo Aufbau. Ej: $Na\ (Z=11) = 1s^2\,2s^2\,2p^6\,3s^1$
- **CEE**: subniveles del **último nivel** ($n$ más alto, incluyendo $d$ del penúltimo nivel si corresponde) — determina propiedades químicas y ubicación en la tabla.
- Notación abreviada con gas noble: se reemplaza el "core" interno por el gas noble anterior entre corchetes. Ej: $Na = [Ne]\,3s^1$

**Ejemplos**:
$$Cl\ (Z=17) = 1s^2\,2s^2\,2p^6\,3s^2\,3p^5 \implies \text{CEE}=3s^2\,3p^5$$
$$Ti\ (Z=22) = 1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^2 \implies \text{CEE}=4s^2\,3d^2$$

## 7. Grupo y período a partir de la CEE

- **Período** = valor de $n$ del nivel más externo.
- **Grupo**:
  - Elementos representativos (bloque s/p): $ns^1 \to$ grupo 1, $ns^2 \to$ grupo 2, ..., $ns^2np^6 \to$ grupo 18.
  - Elementos de transición (bloque d): grupo = suma de electrones en $(n-1)d + ns$.

**Ejemplo**: $[Kr]\,4d^{10}\,5s^2\,5p^6 \implies$ CEE $5s^2\,5p^6$, Grupo 18, Período 5 (es un gas noble).

## 8. Formación de iones estables

- **Cationes**: se forman perdiendo electrones, primero los del subnivel de **mayor $n$** (en transición se pierden primero los $s$, aunque en la CE el $d$ se llenó después). Ej: $Zn^{2+} = 1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,3d^{10}$ (se van los $4s^2$, no los $3d$).
- **Aniones**: se forman ganando electrones hasta completar el octeto del subnivel $p$ más externo. Ej: $O^{2-} = 1s^2\,2s^2\,2p^6$.
- **Regla de estabilidad**: los iones más estables son **isoelectrónicos** con el gas noble más cercano.
- **Metales de transición**: no siempre siguen la isoelectronicidad con gases nobles; puede haber estabilidad extra en subniveles $d$ llenos o semillenos (ej. $Fe^{3+}$ con $3d^5$ semilleno).

## 9. Isoelectronicidad

Dos especies son **isoelectrónicas** si tienen la misma cantidad de electrones (y por lo tanto, en general, la misma CE), aunque tengan distinto número atómico. Se usa para deducir la CE de iones o compararlos con gases nobles.

**Ejemplo típico de examen**: "Un átomo Q gana 1 electrón y forma un ion isoelectrónico con $R^{2+}$ ($Z_R=38$)". Como $R^{2+}$ tiene $36$ electrones, $Q^-$ también debe tener $36$ $\Rightarrow$ $Q$ tiene $Z=35$ (Br):
$$Q^- = 1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^{10}\,4p^6$$

*Ejercicios: ver [SERIE 1_2C_2026.pdf](practicas/SERIE%201_2C_2026.pdf) y [Practica-1.md](Practica-1.md).*

---

# SERIE 2 – Estructuras de Lewis, TREPEV y Polaridad

> Temas: Moléculas. Estructuras de Lewis. Regla del octeto y excepciones. Geometría molecular. TREPEV. Polaridad de enlaces. Momento dipolar. Polaridad de moléculas diatómicas y poliatómicas.

## Datos útiles

- Electronegatividad (Pauling): **aumenta** hacia la derecha y hacia arriba en la tabla (los gases nobles quedan fuera de esta tendencia).
- $1$ Debye $(D) = 3,336\times10^{-30}\ C.m$

## 1. Electrones de valencia

Cantidad de electrones en la CEE de cada átomo. En una molécula o ion, el total de electrones de valencia se obtiene **sumando** los de cada átomo, y sumando/restando 1 e⁻ por cada carga negativa/positiva si es un ion.

## 2. Cómo construir una estructura de Lewis

1. Contar el total de electrones de valencia disponibles.
2. Elegir el átomo central (generalmente el de **menor** electronegatividad, nunca el H).
3. Unir los átomos periféricos al central con enlaces simples (2 e⁻ cada uno).
4. Completar el octeto de los átomos periféricos con pares libres.
5. Colocar los electrones restantes como pares libres en el átomo central.
6. Si el átomo central no completa el octeto, formar enlaces múltiples convirtiendo pares libres vecinos en pares compartidos.
7. Verificar las **cargas formales** para elegir la estructura más razonable.

**Ejemplos resueltos** (ver [Practica-2.md](Practica-2.md)):
- $N_2$: $:\!N\equiv N\!:$ (triple enlace, cada N con 1 par libre)
- $CO_2$: $:\!\overset{..}{O}\!=\!C=\overset{..}{O}\!:$ (lineal, sin pares libres en C)
- $NH_3$: N central con 3 enlaces simples a H y 1 par libre
- $CH_4$: C central con 4 enlaces simples a H, sin pares libres

## 3. Regla del octeto y excepciones

- Regla general: los átomos tienden a rodearse de **8 electrones** (2 en el caso del H).
- **Octeto incompleto**: $Be$ (4 e⁻ alrededor), $B/Al$ (6 e⁻ alrededor).
- **Octeto expandido**: elementos del período 3 en adelante ($S, P, Cl, Xe,\dots$) pueden superar 8 e⁻ por disponer de orbitales $d$ de valencia. Ej: $SF_6$, $PF_5$.
- **Radicales**: moléculas con número impar de electrones de valencia totales no pueden cumplir el octeto en todos sus átomos (ej. $NO$).
- Los **compuestos iónicos** (ej. $CaCl_2$) no se representan con una única estructura covalente: se dibujan los iones por separado, cada uno con su octeto y su carga.

## 4. Carga formal (CF)

$$CF = (e^-\ \text{de valencia del átomo libre}) - (e^-\ \text{no enlazantes}) - \frac{e^-\ \text{enlazantes}}{2}$$

- La suma de las CF de todos los átomos = carga neta de la especie.
- La estructura **más estable** entre varias posibles es la que tiene:
  - Cargas formales lo más cercanas a 0 posible.
  - Cargas negativas sobre los átomos más electronegativos.

## 5. Resonancia

Cuando una molécula/ion puede representarse con **más de una estructura de Lewis válida** que difieren solo en la posición de los electrones, la estructura real es un **híbrido de resonancia** entre todas ellas. Ejemplos típicos: $NO_3^-$, $CO_3^{2-}$, $O_3$.

## 6. Compuestos iónicos vs. moleculares

- **Iónicos**: metal + no metal (o catión + anión poliatómico). Iones separados con su carga, unidos por atracción electrostática. Ej: $CaCl_2$, $Na_2CO_3$.
- **Moleculares (covalentes)**: no metal + no metal. Comparten pares de electrones.

## 7. TREPEV (Teoría de Repulsión de Pares Electrónicos de Valencia)

Los grupos de electrones (enlazantes y libres) alrededor del átomo central se repelen y se ubican lo más alejados posible, determinando la geometría.

**Pasos:**
1. Dibujar la estructura de Lewis.
2. Contar **grupos electrónicos** alrededor del átomo central (enlace simple/doble/triple = 1 grupo; cada par libre = 1 grupo).
3. Determinar la **geometría electrónica** según el número total de grupos.
4. Determinar la **geometría molecular** según cuántos grupos son enlazantes y cuántos libres.
5. Los pares libres ocupan más espacio y comprimen levemente los ángulos reales respecto del ideal.

### Tabla de geometrías (notación $AX_nE_m$)

| Grupos e⁻ | Pares libres ($E$) | Geom. electrónica | Geom. molecular | Ángulo(s) ideal | Ejemplo |
|---|---|---|---|---|---|
| 2 | 0 | Lineal | Lineal | $180°$ | $CO_2$ |
| 3 | 0 | Trigonal plana | Trigonal plana | $120°$ | $BF_3$ |
| 3 | 1 | Trigonal plana | Angular | $\approx120°$ | $O_3$, $SO_2$ |
| 4 | 0 | Tetraédrica | Tetraédrica | $109,5°$ | $CH_4$ |
| 4 | 1 | Tetraédrica | Piramidal trigonal | $\approx107°$ | $NH_3$ |
| 4 | 2 | Tetraédrica | Angular | $\approx104,5°$ | $H_2O$ |
| 5 | 0 | Bipiramidal trigonal | Bipiramidal trigonal | $90°/120°$ | $PCl_5$ |
| 5 | 1 | Bipiramidal trigonal | Balancín (sierra) | $<90°/<120°$ | $SF_4$ |
| 5 | 2 | Bipiramidal trigonal | Forma de T | $\approx90°$ | $ClF_3$ |
| 5 | 3 | Bipiramidal trigonal | Lineal | $180°$ | $XeF_2$, $I_3^-$ |
| 6 | 0 | Octaédrica | Octaédrica | $90°$ | $SF_6$ |
| 6 | 1 | Octaédrica | Piramidal cuadrada | $\approx90°$ | $BrF_5$ |
| 6 | 2 | Octaédrica | Plana cuadrada | $90°$ | $XeF_4$ |

*(En posiciones bipiramidal trigonal/octaédrica, los pares libres ocupan primero las posiciones que minimizan repulsiones a 90°.)*

## 8. Electronegatividad y polaridad de enlace

- La diferencia de electronegatividad $\Delta EN$ entre dos átomos enlazados determina qué tan polar es el enlace.
- $\Delta EN = 0 \Rightarrow$ enlace **no polar** (átomos iguales).
- $\Delta EN$ pequeña ($0 < \Delta EN < 1,7$ aprox.) $\Rightarrow$ **polar**.
- $\Delta EN$ grande ($\geq 1,7$ aprox.) $\Rightarrow$ carácter **iónico**.
- Para ordenar sin calcular: comparar posición relativa en la tabla periódica.

## 9. Momento dipolar

- De un enlace: $\mu = Q \times d$ ($Q$ = carga parcial en C, $d$ = distancia entre átomos en m). El vector apunta del extremo $\delta^+$ al $\delta^-$.
- Unidad usual: **Debye** ($1\ D = 3,336\times10^{-30}\ C.m$).
- El **momento dipolar molecular** es la **suma vectorial** de los momentos de todos los enlaces (y del efecto de pares libres).

## 10. Polaridad de moléculas

- **Molécula polar** ($\mu \neq 0$): sus vectores de enlace **no se cancelan** por simetría.
- **Molécula no polar** ($\mu = 0$):
  - Todos sus enlaces son no polares, **o**
  - Tiene enlaces polares pero la geometría es simétrica y se cancelan (ej: $CO_2$ lineal, $CH_4$ tetraédrico, $BF_3$ trigonal plana, $SF_6$ octaédrico).
- Los **pares libres** sobre el átomo central rompen la simetría y suelen generar polaridad neta (ej: $H_2O$, $NH_3$).
- La polaridad **solo se evalúa en moléculas neutras**.

## 11. Qué predice (y qué no) el TREPEV

| Predice | No predice |
|---|---|
| Geometría electrónica | Longitud de enlace |
| Geometría molecular | Reactividad química |
| Ángulos de enlace aproximados | — |

La **polaridad** no la predice directamente el TREPEV: se deduce combinando la geometría (TREPEV) con la polaridad de cada enlace (electronegatividad).

*Ejercicios: ver [SERIE 2_2C_2026.pdf](practicas/SERIE%202_2C_2026.pdf) y [Practica-2.md](Practica-2.md).*

---

# SERIE 3 – Interacciones intermoleculares

> Temas: Interacciones intermoleculares. Interacciones ion-ion, ion-dipolo y dipolo-dipolo. Polarizabilidad. Fuerzas dispersivas o de London. Puentes de hidrógeno. Relación entre fuerzas intermoleculares y puntos de fusión/ebullición. Criterios de solubilidad.

## 1. Por qué importan: la "ruta de estudio"

$$\text{Átomos} \to \text{Molécula} \to \text{Lewis} \to \text{TREPEV (geometría)} \to \textbf{¿molécula polar o no polar?} \to \textbf{fuerzas intermoleculares}$$

Las fuerzas intermoleculares determinan si una sustancia es **sólido, líquido o gas** a una dada temperatura, y sus puntos de fusión (Pf) y ebullición (Pe). Son consecuencia de:
- **Energía cinética** de las partículas: depende de la temperatura, tiende a separarlas.
- **Energía potencial**: surge de las fuerzas de atracción intermoleculares (aprox. independiente de T).

| Relación $E_c$ vs $E_p$ | Estado |
|---|---|
| $E_c \gg E_p$ (T alta o atracciones débiles) | **Gas** |
| $E_c \approx E_p$ | **Líquido** |
| $E_c \ll E_p$ (T baja o atracciones fuertes) | **Sólido** |

## 2. Clasificación de las interacciones

### a) Electrostáticas — entre especies con carga neta o dipolo permanente
- **Ion–ion**: entre iones (ej. red cristalina de $NaCl$). Dependen de la carga $Q_1Q_2$.
- **Ion–dipolo**: un ion atrae al polo de signo opuesto de una molécula polar (ej. $Na^+$ rodeado de $H_2O$).
- **Dipolo–dipolo**: entre dos moléculas polares (ej. $HCl$/$HCl$). Aumenta con el momento dipolar $\mu$, para moléculas de masa molar (Mr) similar.

### b) Inductivas — un ion o dipolo **induce** una distribución asimétrica de cargas en una molécula no polar
- **Ion–dipolo inducido**: ej. $Na^+$ junto a $Cl_2$.
- **Dipolo–dipolo inducido**: ej. $H_2O$ junto a $Cl_2$.

### c) Dispersivas o de London — entre **dipolos instantáneos/transitorios**
Ocurren en **todas** las sustancias (polares y no polares), porque en cualquier instante la nube electrónica puede distorsionarse y generar un dipolo transitorio que induce otro dipolo en la molécula vecina. Es la **única** fuerza posible entre especies no polares (ej. gases nobles, $Cl_2$, $CH_4$).

### d) Puente de hidrógeno — caso particular (muy intenso) de dipolo-dipolo
- Ocurre quando un **H está unido covalentemente a N, O o F** (átomos muy electronegativos y chicos) y ese H interactúa con un par libre de N/O/F de **otra** molécula.
- Ejemplos: $H_2O$, $NH_3$, alcoholes ($CH_3OH$). Es clave en la estructura del hielo, en la doble hélice del ADN (pares A–T con 2 puentes H, G–C con 3) y en muchas biomoléculas.

## 3. Tabla comparativa de magnitudes (orden de intensidad típico)

| Tipo | Ejemplo | Magnitud depende de | Magnitud típica |
|---|---|---|---|
| Ion–ion | $Na^+Cl^-$ | $Q_1 Q_2$ | $\sim 250\ kJ/mol$ |
| Puente de hidrógeno | $H_2O$/$H_2O$ | — (direccional) | $\sim 20\ kJ/mol$ |
| Ion–dipolo | $Na^+$/$HCl$ | $Q_1 \mu_2$ | $\sim 15\ kJ/mol$ |
| Ion–dipolo inducido | $Na^+$/$Cl_2$ | $Q_1 \alpha_2$ | $\sim 10\ kJ/mol$ |
| Dispersión (London) | $Cl_2$/$Cl_2$ | $\alpha_1 \alpha_2$ | $\sim 5\ kJ/mol$ (crece mucho con el tamaño) |
| Dipolo–dipolo | $HCl$/$HCl$ | $\mu_1 \mu_2$ | $\sim 0,6\ kJ/mol$ |
| Dipolo–dipolo inducido | $HCl$/$Cl_2$ | $\mu_1 \alpha_2$ | $< 1\ kJ/mol$ |

$Q$ = carga, $\mu$ = momento dipolar, $\alpha$ = polarizabilidad.

**Importante**: las fuerzas de London, aunque "débiles" en moléculas chicas, **crecen mucho con el tamaño/masa molar** y pueden llegar a dominar sobre interacciones dipolo-dipolo en moléculas grandes (por eso $CCl_4$, apolar, es líquido a 25°C mientras $NH_3$, polar, es gas).

## 4. Polarizabilidad ($\alpha$)

Capacidad de una molécula/átomo de deformar su nube electrónica ante un dipolo o carga cercana.

- **Aumenta** con: el número de electrones, una nube electrónica más difusa (átomos/moléculas más grandes), y la masa molar.
- A mayor polarizabilidad $\Rightarrow$ mayor fuerza de London $\Rightarrow$ mayor Pf/Pe.
- La **forma** también influye: moléculas más alargadas (mayor superficie de contacto) tienen fuerzas de London más intensas que sus isómeros más compactos/esféricos. Ej: pentano lineal $T_{eb}=36°C$ vs 2,2-dimetilpropano (más compacto, misma fórmula) $T_{eb}=10°C$.

**Ejemplo clásico — halógenos a temperatura ambiente**:
$$F_2\ (gas) < Cl_2\ (gas) < Br_2\ (líquido) < I_2\ (sólido)$$
A mayor $Z$, los electrones de valencia están más alejados del núcleo, la nube es más difusa y más polarizable $\Rightarrow$ fuerzas de London más intensas $\Rightarrow$ mayor Pf/Pe.

## 5. Relación fuerzas intermoleculares ↔ Pf y Pe

**Regla general**: a mayor intensidad de las fuerzas intermoleculares, mayor energía hay que entregar para separar las moléculas $\Rightarrow$ mayor Pf y Pe.

**Ejemplo comparativo** (hidruros del grupo 14, todos con **solo** fuerzas de London, geometría tetraédrica y $\mu=0$):

| Compuesto | Estado a 25°C | $P_{eb}$ (°C) |
|---|---|---|
| $CH_4$ | Gas | $-161$ |
| $SiH_4$ | Gas | $-111$ |
| $CCl_4$ | Líquido | $77$ |

El $P_{eb}$ crece con la masa molar/polarizabilidad ($CH_4 \to SiH_4 \to CCl_4$).

**Ejemplo con puente H** (comparar $CH_4$, $CH_2O$, $H_2O$): $CH_4$ (solo London, $\mu=0$) $<$ $CH_2O$ (dipolo-dipolo, $\mu\neq0$) $<$ $H_2O$ (puente de hidrógeno) — orden creciente de $P_{eb}$.

**Anomalía de los grupos 15-17** (hidruros del grupo 16, 15 y 17): el primer hidruro de cada grupo ($H_2O$, $NH_3$, $HF$) tiene $P_{eb}$ **anormalmente alto** respecto a la tendencia del resto del grupo, porque forma puente de hidrógeno (a diferencia del grupo 14, donde ningún hidruro forma puente H). Por eso el $H_2O$ es líquido a temperatura ambiente mientras el $H_2S$ (misma geometría, sin puente H, solo dipolo-dipolo + London) es gas.

## 6. Criterios de solubilidad — "Lo semejante disuelve a lo semejante"

Para que un soluto se disuelva bien en un solvente, las fuerzas de interacción soluto-soluto y solvente-solvente deben ser reemplazadas por fuerzas soluto-solvente de **magnitud similar**.

| Soluto | Solvente adecuado | Por qué |
|---|---|---|
| Iónico (ej. $NaCl$) o polar (ej. glucosa) | Polar (ej. $H_2O$) | Interacciones ion-dipolo o dipolo-dipolo/puente H |
| No polar (ej. $I_2$, hexano) | No polar (ej. $CCl_4$, benceno) | Solo fuerzas de London en ambos |

**Ejemplos**:
- $I_2$ (no polar) **no** se disuelve en agua (polar) pero sí en $CCl_4$ (no polar).
- $Br_2$ es más soluble en $C_6H_6$ ($\mu=0$) que en agua, porque el $Br_2$ es no polar.
- $KCl$ (iónico) es más soluble en $NH_3$ líquido (polar) que en $CCl_4$ ($\mu=0$).

## 7. Sistemas típicos y sus interacciones (ejercicio guía de la Serie 3)

| Sistema | Interacciones presentes |
|---|---|
| Agua líquida | Puente de hidrógeno (+ dipolo-dipolo, London) |
| Argón gaseoso | Solo London (dipolo instantáneo–dipolo instantáneo) |
| Solución acuosa de Ar | Dipolo–dipolo inducido ($H_2O$ induce dipolo en Ar) + puente H entre moléculas de agua |
| $NaCl$ sólido | Ion–ion (red cristalina) |
| Solución acuosa de $NaCl$ | Ion–dipolo (iones hidratados por $H_2O$) + puente H entre las moléculas de agua |

*Ejercicios: ver [SERIE 3_2C_2026.pdf](practicas/SERIE%203_2C_2026.pdf).*

---

# SERIE 4 – Soluciones

> Temas: Visión microscópica de la solubilidad. Densidad. Concentración. % m/m y m/V. Molaridad. Fracción molar. Dependencia de la solubilidad con la temperatura. Diluciones. Factor de dilución. Técnicas de preparación de soluciones y diluciones.

## 1. Sistemas materiales — repaso de base

- **Propiedades físicas**: se miden sin cambiar la composición/identidad de la sustancia. **Químicas**: implican un cambio de composición.
- **Extensivas**: dependen de la cantidad de materia (ej. masa, volumen). **Intensivas**: no dependen de la cantidad (ej. densidad, temperatura, concentración) — **caracterizan** al material.
- **Densidad**: $\delta = m/V$.
- **Sistema homogéneo** (1 fase, propiedades intensivas iguales en toda porción) vs **heterogéneo** (2+ fases, con interfaces).
- **Sustancia pura** (1 componente) vs **mezcla** (2+ componentes). Una **solución** es una **mezcla homogénea** (1 fase, 2+ componentes) que no reaccionan entre sí.

| | Sustancia pura | Mezcla |
|---|---|---|
| Homogéneo | Agua pura | Alcohol en agua (solución) |
| Heterogéneo | Agua + hielo | Agua + aceite |

## 2. Soluto y solvente

- **Soluto**: sustancia(s) en **menor** cantidad.
- **Solvente**: sustancia en **mayor** cantidad.
- Pueden combinarse gas+gas, gas+líquido (ej. agua gaseosa, $CO_2$ en agua), líquido+líquido (etanol en agua), sólido+líquido (NaCl en agua), sólido+sólido (bronce).

## 3. Proceso de disolución: "lo semejante disuelve lo semejante"

Al disolverse, el soluto **cambia** su interacción consigo mismo por una interacción con el solvente: para que el proceso sea favorable, ambas interacciones deben ser de **magnitud similar** (ver también Serie 3, punto 6).

- Hexano (no polar) es soluble en $CCl_4$ (no polar): ambos con solo fuerzas de London.
- Glucosa (polar) es soluble en agua (polar): puente de hidrógeno.
- $NaCl$ (iónico) es soluble en agua (polar): interacción ion-dipolo, el agua rodea e "hidrata" cada ion.
- $I_2$ (no polar) no se disuelve en agua pero sí en $CCl_4$.

En un sólido, se disuelven más fácilmente las partículas de la **superficie** de la red (menos ligadas al resto, más accesibles al solvente). Cuanto más dividido (pulverizado) está el sólido, mayor superficie de contacto y mayor velocidad de disolución.

## 4. Concentración

$$\text{Concentración} = \frac{\text{Cantidad de soluto}}{\text{Cantidad de solución (o de solvente)}}$$

Cualitativamente: **diluida** (poco soluto) < **concentrada** (mucho soluto) $\leq$ **saturada** (el máximo que admite a esa T).

### Las 7 formas de expresar concentración

| Magnitud | Fórmula | Unidad |
|---|---|---|
| % m/m | $\%\,m/m = \dfrac{m_{sto}}{m_{sc}}\times100$ | masa sto / 100 g sc |
| % m/V | $\%\,m/V = \dfrac{m_{sto}(g)}{V_{sc}(cm^3)}\times100$ | g sto / 100 cm³ sc |
| % V/V | análogo, en volúmenes | cm³ sto / 100 cm³ sc |
| Molaridad ($M$) | $M = \dfrac{n_{sto}}{V_{sc}(L)}$ | $mol/L$ |
| Molalidad ($m$) | $m = \dfrac{n_{sto}}{m_{sv}(kg)}$ | $mol/kg$ |
| Fracción molar ($\chi$) | $\chi_{sto} = \dfrac{n_{sto}}{n_{sto}+n_{sv}}$ | adimensional, $0<\chi<1$ |
| Partes por millón (ppm) | $ppm = \dfrac{m_{sto}(mg)}{m_{sc}(mg)}\times10^6$ | mg sto / kg sc |

**Ejemplos**:
- $0,5\ g$ de HCl cada $100\ g$ de solución $\Rightarrow \%m/m = 0,5$.
- $1,5\ g$ de HCl en $75\ cm^3$ de solución $\Rightarrow \%m/V = 2\,g/cm^3\cdot 10^{-2}$, es decir $1,5/75\times100=2\ \%m/V$.
- $0,5\ mol$ de HCl en $0,2\ L$ de solución $\Rightarrow M = 0,5/0,2 = 2,5\ M$.
- $0,5\ mol$ de HCl en $1\ kg$ de solvente $\Rightarrow m = 0,5\ mol/kg$.
- Una solución **100 ppm** contiene 100 mg de soluto cada 1.000.000 mg (1 kg) de solución.

**ppm simplificado para soluciones acuosas muy diluidas**: como en ese caso $\delta_{sc}\approx\delta_{sv}\approx1\ g/mL$, entonces $1.000.000\ mg$ de solución $\approx 1\ L$, y:
$$ppm \approx \frac{m_{sto}(mg)}{V_{sc}(L)} \quad \text{(solo si el solvente es agua y la solución es muy diluida)}$$

### Relaciones útiles

- Moles y masa: $n_{sto}=\dfrac{m_{sto}}{Mr_{sto}}$, y $n_{sto}+n_{sv}=n_{totales}$.
- Masas: $m_{sto}+m_{sv}=m_{sc}$ **(salvo que el problema aclare lo contrario)**.
- **Volúmenes NO son aditivos** (salvo que el enunciado lo indique explícitamente): $V_{sc}\neq V_{sto}+V_{sv}$ en general. Ej: $1\ L\ H_2O + 1\ L$ etanol $= 1,93\ L$ de solución (contracción de volumen del 3,5%).
- Densidad: $\delta_{sc}=m_{sc}/V_{sc}$ (y análogamente para soluto/solvente puros).

## 5. Cómo preparar una solución (ejemplo resuelto)

**Preparar 200 mL de solución acuosa de $CuCl_2$ 0,50 M**:
$$n_{sto} = V_{sc}\times M = 0,2\ L \times 0,5\ mol/L = 0,1\ mol$$
$$m_{sto} = n_{sto}\times Mr_{sto} = 0,1\ mol \times 135\ g/mol = 13,5\ g$$

Procedimiento: pesar 13,5 g de $CuCl_2$, colocarlos en un matraz de 200 mL, agregar un poco de agua y disolver, luego **enrasar** con agua hasta el volumen final de 200 mL (el menisco al nivel de la vista).

## 6. Diluciones

Una dilución **disminuye la concentración** de soluto agregando solvente. Los **moles de soluto no cambian**, solo el volumen de la solución:

$$C_0 \cdot V_0 = C_F \cdot V_F$$

**Factor de dilución**: cuántas veces se diluyó la solución original (ej. dilución 1:25 significa que 1 L de solución original se lleva a 25 L totales, quedando la concentración dividida por 25).

**Ejemplo**: partiendo de 1000 mL de $NaOH$ 0,1 M:
| Dilución | Cálculo | $M_2$ |
|---|---|---|
| 1:2 | $0,1\times1/2$ | $0,05$ |
| 1:10 | $0,1\times1/10$ | $0,01$ |
| 1:25 | $0,1\times1/25$ | $0,004$ |

## 7. Solubilidad

**Solubilidad**: máxima concentración de un soluto que puede disolverse en cierto solvente, a una temperatura determinada (estado de **equilibrio**: la velocidad de disolución = velocidad de precipitación).

$$NaCl(s) \underset{}{\overset{H_2O}{\rightleftharpoons}} Na^+(ac) + Cl^-(ac)$$

- **Solución saturada**: contiene la cantidad máxima de soluto disuelta a esa T (está en equilibrio con soluto sin disolver, o justo en el límite).
- **Solución insaturada (no saturada)**: contiene menos soluto que el máximo posible a esa T.
- **Solución sobresaturada**: contiene más soluto que el de una saturada a esa T (estado inestable, no está en equilibrio real).

**Curvas de solubilidad**: gráfico de solubilidad (g soluto/100 g agua) vs. temperatura.
- En general, la solubilidad de **sólidos iónicos aumenta con la T** (hay excepciones, ej. $Ce_2(SO_4)_3$, $NaCl$ casi no cambia).
- La solubilidad de **gases disminuye al aumentar la T** (por eso una gaseosa conserva mejor el gas disuelto fría que a temperatura ambiente).

**Ejemplo de cálculo con curva de solubilidad** (regla de tres): si a 60°C el $NaNO_3$ tiene solubilidad $\approx126\ g/100\ g\ H_2O$, ¿cuánto se disuelve en 278 g de agua?
$$100\ g\ agua \to 126\ g\ NaNO_3 \qquad 278\ g\ agua \to X$$
$$X = \frac{278\times126}{100} \approx 350\ g$$

**Ejemplo con exceso de soluto** (solubilidad de $AgNO_3$ a 18°C = 211,6 g/100 g agua): si se agregan 823,2 g de $AgNO_3$ a 300 mL de agua ($\delta_{H_2O}=0,999\ g/mL \Rightarrow 299,6\ g$ de agua), la máxima cantidad que se disuelve es:
$$\frac{211,6}{100}\times299,6 \approx 633,96\ g$$
Quedan **189,24 g sin disolver** (solución saturada + exceso de sólido).

## 8. Ejemplos integradores típicos de la Serie 4

- **% m/m a partir de masas**: 2 sobres de 6,25 g de azúcar en 200 cm³ de agua $\Rightarrow \%m/m = \dfrac{12,5}{212,5}\times100 \approx 5,9\%$.
- **De % m/m a molaridad, usando densidad**: solución de $FeCl_3$ al 25% m/m con 61,7 g de sal en 200 cm³ de solución $\Rightarrow$ masa de solución $=61,7/0,25=246,8\ g \Rightarrow \delta=246,8/200=1,234\ g/cm^3$; luego $n_{FeCl_3}=61,7/162,2=0,38\ mol \Rightarrow M=0,38/0,2=1,90\ M$.
- **Concentración resultante al mezclar dos soluciones del mismo soluto** (volúmenes aproximadamente aditivos): 100 cm³ de $HNO_3$ 0,25 M + 500 cm³ de $HNO_3$ 1,25 M:
$$M_f = \frac{n_{total}}{V_{total}} = \frac{0,1\times0,25 + 0,5\times1,25}{0,6} = 1,08\ M$$
- **ppm en agua potable/mineral**: límites de metales pesados (As, Cd, Pb, Hg) se expresan en ppm y se convierten a % m/m o M usando $\delta_{sc}\approx1\ g/mL$ para soluciones muy diluidas.

*Ejercicios: ver [SERIE 4_1C_2022.pdf](practicas/SERIE%204_1C_2022.pdf) (no hay serie 2C_2026 propia; los contenidos y el tipo de ejercicio son los mismos).*

---

## Cómo se conectan las 4 series (mapa mental para el parcial)

$$\text{CEE del átomo (S1)} \to \text{enlaces y Lewis (S2)} \to \text{geometría TREPEV y polaridad (S2)} \to \text{fuerzas intermoleculares (S3)} \to \text{Pf/Pe, estado de agregación y solubilidad (S3–S4)} \to \text{cómo cuantificar una solución (S4)}$$

Un ejercicio de parcial típico integra varias series a la vez: por ejemplo, a partir de una fórmula molecular te piden la CEE de sus átomos (S1), la estructura de Lewis y CF (S2), la geometría y polaridad por TREPEV (S2), qué fuerzas intermoleculares presenta y por qué (S3), y finalmente si es soluble en agua o cómo preparar una solución de esa sustancia (S4).
