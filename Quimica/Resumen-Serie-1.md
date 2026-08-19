# Serie 1 – Átomos, iones y configuración electrónica

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
- Energía **por mol de fotones/átomos**: multiplicar por $N_A$

$$E_{mol} = E_{foton} \times N_A$$

Cuidado con las unidades: $\lambda$ en metros $\to$ $E$ en Joule $\to$ pasar a kJ/mol dividiendo por 1000.

A menor $\lambda$ (o mayor frecuencia) $\Rightarrow$ mayor energía del fotón.

## 2. Espectro de emisión/absorción del hidrógeno

- **Emisión**: el electrón cae de un nivel superior a uno inferior, libera un fotón (línea de emisión).
- **Absorción**: el electrón sube de nivel absorbiendo un fotón de energía exacta.
- Ecuación de Rydberg para las transiciones del H:

$$\frac{1}{\lambda} = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right), \quad n_1 < n_2$$

- La serie de Balmer (líneas visibles: 410, 434, 486, 656 nm) corresponde a transiciones que terminan en $n_1=2$.
- Cuanto mayor es la diferencia de energía entre niveles, mayor energía y menor longitud de onda tiene el fotón emitido/absorbido.
- Un experimento de este tipo (lámpara + prisma) revela que la energía del átomo está **cuantizada**: solo existen ciertos niveles de energía permitidos.

## 3. Números cuánticos

| Número | Símbolo | Qué describe | Valores posibles |
|---|---|---|---|
| Principal | $n$ | Nivel de energía / tamaño del orbital | $1, 2, 3, \dots$ |
| Secundario (azimutal) | $l$ | Forma del orbital (subnivel) | $0$ a $n-1$ ($s=0, p=1, d=2, f=3$) |
| Magnético | $m_l$ | Orientación espacial del orbital | $-l$ a $+l$ |
| Espín | $m_s$ | Sentido de giro del electrón | $+\tfrac12$ o $-\tfrac12$ |

## 4. Formas de los orbitales

- **s**: esférico, 1 orientación.
- **p**: forma de dos lóbulos (figura de "8"), 3 orientaciones ($p_x, p_y, p_z$), cada uno con un plano nodal.
- **d**: 5 orientaciones ($d_{xy}, d_{xz}, d_{yz}, d_{x^2-y^2}, d_{z^2}$).
- **f**: 7 orientaciones (formas más complejas).
- El tamaño del orbital aumenta con $n$ (ej. $1s < 2s < 3s < 4s$).

## 5. Reglas para armar la configuración electrónica

- **Principio de Aufbau** (regla de las diagonales / Madelung): orden de llenado
$$1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p,\ 5s,\ 4d,\ 5p,\ 6s,\ 4f,\ 5d,\ 6p,\dots$$
- **Principio de exclusión de Pauli**: cada orbital admite máximo **2 electrones**, con espines opuestos.
- **Regla de Hund**: en subniveles degenerados (ej. los 3 orbitales $p$), los electrones ocupan primero orbitales distintos con espín paralelo antes de aparearse.
- Un orbital **no es** una trayectoria fija; describe una región de probabilidad. La mecánica cuántica **sí** es la herramienta apropiada para describir la materia a nivel atómico, y los electrones **sí** se consideran partículas (con comportamiento también ondulatorio).

## 6. Configuración electrónica (CE) y externa (CEE)

- **CE**: se listan todos los subniveles ocupados siguiendo el orden de Aufbau. Ej: $Na\ (Z=11) = 1s^2\,2s^2\,2p^6\,3s^1$
- **CEE**: subniveles del **último nivel** ($n$ más alto, incluyendo $d$ del penúltimo nivel si corresponde) — determina las propiedades químicas y la ubicación en la tabla.
- Notación abreviada con gas noble: se reemplaza el "core" interno por el símbolo del gas noble anterior entre corchetes. Ej: $Na = [Ne]\,3s^1$

## 7. Grupo y período a partir de la CEE

- **Período** = valor de $n$ del nivel más externo.
- **Grupo**:
  - Elementos representativos (bloque s/p): según electrones en la CEE
    - $ns^1 \to$ grupo 1, $ns^2 \to$ grupo 2
    - $ns^2np^1 \to$ grupo 13, ..., $ns^2np^6 \to$ grupo 18
  - Elementos de transición (bloque d): grupo = suma de electrones en $(n-1)d + ns$

## 8. Formación de iones estables

- **Cationes**: se forman perdiendo electrones. Se pierden primero los del subnivel de **mayor $n$** (en metales de transición esto significa que se pierden primero los $s$, aunque en la CE el $d$ se haya llenado después).
- **Aniones**: se forman ganando electrones hasta completar el octeto del subnivel $p$ más externo.
- **Regla general de estabilidad**: los iones más estables son **isoelectrónicos** con el gas noble más cercano (mismo número de electrones que el gas noble).
- **Metales de transición**: su estabilidad iónica no siempre sigue la regla de isoelectronicidad con gases nobles; depende de la estabilidad extra de subniveles $d$ llenos o semillenos (ej. $Fe^{3+}$ con $3d^5$ semilleno es más estable de lo esperado).

## 9. Isoelectronicidad

Dos especies son **isoelectrónicas** si tienen la misma cantidad de electrones (y por lo tanto, en general, la misma CE), aunque tengan distinto número atómico/protónico. Se usa para deducir la CE de iones o comparar iones entre sí y con gases nobles.

---

*Ejercicios: ver [SERIE 1_2C_2026.pdf](practicas/SERIE%201_2C_2026.pdf) y respuestas desarrolladas en [Practica-1.md](Practica-1.md).*
