# Resumen Química General – Segundo Parcial (teoría + verdadero/falso)

> **Alcance**: Serie 5 (Gases) → Serie 6 (Estequiometría) → Serie 7a (Primer principio / Termoquímica) → Serie 7b (Segundo principio, entropía y Gibbs).
> **Fuentes**: `teoria/` Clases 6 a 10 + Ley de Dulong-Petit (2C 2026), y los segundos parciales 2021 1C, 2022 1C, 2022 2C, 2023 2C, 2024 2C y 2025 1C.
> Para qué ejercicios practicar, ver [guia-2do-parcial.md](guia-2do-parcial.md). Para Series 1 a 4, ver [Resumen-Parcial-1.md](Resumen-Parcial-1.md).

**Cómo aparece la teoría en el parcial.** Casi nunca como pregunta suelta: viene pegada a un problema con la forma "justifique", "prediga el signo sin hacer cuentas", "¿mayor, menor o igual?", "explique sin calcular". El único verdadero/falso literal de los parciales del repo es el de gases reales (2021). Por eso este resumen tiene tres partes:

1. Teoría mínima por tema.
2. Las preguntas conceptuales que ya cayeron, con su respuesta.
3. Un banco de verdadero/falso armado a partir de esa teoría y de esas preguntas (las afirmaciones las redacté yo; no son de un parcial salvo donde se indica).

---

# PARTE 1 – Teoría por tema

## 1. Gases (Clase 6)

### Presión y unidades

- La presión de un gas se debe a los **choques de las partículas contra las paredes** del recipiente: $P = F/A$. Más choques (más partículas, o más energía cinética) $\Rightarrow$ más presión.
- $1\ atm = 760\ mmHg = 760\ Torr = 1{,}013\times10^5\ Pa = 1013\ hPa = 1{,}013\ bar$
- $T(K) = T(°C) + 273{,}15$. **En toda fórmula de gases y de termodinámica la T va en Kelvin.**
- **CNPT**: $1\ atm$ y $273\ K$. **Condiciones ambientales**: $1\ atm$ y $298\ K$.

### Leyes de los gases (cantidad de gas fija)

| Ley | Qué se mantiene constante | Relación | Fórmula |
|---|---|---|---|
| Boyle-Mariotte | $T$ y $n$ | $P$ inversamente proporcional a $V$ | $P_1V_1 = P_2V_2$ |
| Charles | $P$ y $n$ | $V$ directamente proporcional a $T$ | $V_1/T_1 = V_2/T_2$ |
| Gay-Lussac | $V$ y $n$ | $P$ directamente proporcional a $T$ | $P_1/T_1 = P_2/T_2$ |
| Avogadro | $P$ y $T$ | $V$ directamente proporcional a $n$ | $V_1/n_1 = V_2/n_2$ |
| Combinada | $n$ | — | $P_1V_1/T_1 = P_2V_2/T_2$ |

- La proporcionalidad con $T$ vale **solo en Kelvin**: pasar de 20 °C a 40 °C **no** duplica la presión.
- Avogadro: a igual $P$ y $T$, volúmenes iguales de gases distintos tienen el **mismo número de partículas** (no la misma masa).

### Ecuación del gas ideal

$$PV = nRT \qquad R = 0{,}082\ \frac{L\cdot atm}{K\cdot mol} = 8{,}314\ \frac{J}{K\cdot mol}$$

**Modelo de gas ideal** (los 4 supuestos de la clase):
- Las partículas ocupan todo el volumen del recipiente (su volumen propio es despreciable).
- Se mueven en forma aleatoria.
- **No hay interacción** entre las partículas.
- El gas se puede comprimir.

**Gases reales**: se parecen al ideal cuando esos supuestos se cumplen, es decir a **presión baja** (partículas lejos, volumen propio despreciable) y **temperatura alta** (la energía cinética le gana a las atracciones). Se alejan del ideal a presión alta y temperatura baja.

**Volumen molar**: $V_m = RT/P$. En CNPT da $22{,}4\ L/mol$ para **cualquier** gas ideal. Fuera de CNPT ese número no vale: hay que usar $PV=nRT$.

### Densidad y masa molar

$$\rho = \frac{P\cdot Mr}{R\cdot T} \qquad\qquad Mr = \frac{mRT}{PV} = \frac{\rho RT}{P}$$

- A igual $P$ y $T$, **el gas de mayor $Mr$ es el más denso**. Un globo asciende si su gas es menos denso que el aire ($Mr_{aire}\approx 29\ g/mol$): He sube, CO₂ no.
- La densidad sube con $P$ y baja con $T$.
- Para una **mezcla**: $\rho = m_{total}/V$, o la misma fórmula con la masa molar promedio $\overline{Mr} = \sum x_i\,Mr_i$.

### Mezcla de gases – Ley de Dalton

$$P_{total} = P_A + P_B + \dots \qquad P_A = x_A\cdot P_{total} \qquad x_A = \frac{n_A}{n_{total}}$$

- La **presión parcial** de un gas es la presión que ejercería **si estuviera solo** en el recipiente: $P_A V = n_A RT$.
- Vale para gases que **no reaccionan** entre sí.
- $\sum x_i = 1$.

**Qué pasa al agregar otro gas a $V$ y $T$ constantes** (cayó en 2022 y 2024):

| Magnitud | Cambio | Por qué |
|---|---|---|
| Presión parcial de los gases que ya estaban | **No cambia** | $P_A = n_ART/V$ y nada de eso cambió |
| Presión total | Aumenta | Hay más moles totales |
| Fracción molar de los gases que ya estaban | Disminuye | Mismo $n_A$, mayor $n_{total}$ |
| Densidad de la mezcla | Aumenta | Más masa en el mismo volumen |

**Qué pasa al sacar un tabique entre dos tanques** (2024): cada gas pasa a ocupar el volumen total, así que su presión parcial baja en la proporción $V_{inicial}/V_{total}$ (Boyle). La presión final es la suma de las parciales nuevas.

---

## 2. Estequiometría (Clase 7)

- **Ley de conservación de la masa**: en una ecuación balanceada hay el mismo número de átomos de cada elemento a ambos lados. Se balancea cambiando **coeficientes**, nunca subíndices.
- Lo que se conserva son **átomos y masa**. El número de **moles o de moléculas puede cambiar** ($N_2 + 3H_2 \to 2NH_3$: 4 moles dan 2).
- Los coeficientes son una relación en **moles** (o moléculas), **no en gramos**.
- Métodos de balanceo: a ojo (tabla de átomos) o **algebraico** (un coeficiente incógnita por sustancia, una ecuación por elemento, fijar uno y resolver; si quedan fracciones se multiplica todo).

### Esqueleto de todo problema

$$\text{dato} \to \textbf{moles} \xrightarrow{\ \text{coeficientes}\ } \textbf{moles} \to \text{lo que piden}$$

| Dato de entrada | Cómo pasar a moles |
|---|---|
| Masa | $n = m/Mr$ |
| Volumen de líquido o sólido puro | $m = \rho\cdot V$, luego $n = m/Mr$ |
| Gas | $n = PV/RT$ (o $V/22{,}4$ solo en CNPT) |
| Solución | $n = M\cdot V(L)$ |
| Partículas | $n = N/N_A$ |

### Reactivo limitante y en exceso

- **Limitante**: el que se consume por completo y determina la máxima cantidad de producto. **No es el de menor masa ni el de menor cantidad de moles**: hay que comparar contra los coeficientes.
- Cómo se identifica: pasar todo a moles, elegir un reactivo, calcular cuánto "necesito" del otro; si tengo más de lo que necesito, el otro está en exceso.
- Atajo: dividir los moles de cada reactivo por su coeficiente; el menor cociente es el limitante.
- **Todos los cálculos de producto se hacen desde el limitante.**
- Exceso que sobra $=$ lo que tenía $-$ lo que reaccionó.

### Pureza y rendimiento

$$\text{Pureza \%} = \frac{m_{reactivo\ puro}}{m_{muestra}}\times100 \qquad\qquad \text{Rendimiento \%} = \frac{\text{cantidad real}}{\text{cantidad teórica}}\times100$$

- La **pureza** se aplica al **reactivo**, antes de calcular: solo reacciona la parte pura.
- El **rendimiento** se aplica al **producto**, al final.
- El rendimiento es menor a 100% por reacciones competitivas o incompletas (equilibrio). **Nunca puede superar 100%.**
- Problema inverso ("cuánto reactivo impuro necesito para obtener X de producto"): se **divide** por el rendimiento y por la pureza.

$$m_{impura} = \frac{m_{pura\ necesaria}}{\text{pureza}} \qquad n_{teórico} = \frac{n_{real\ deseado}}{\text{rendimiento}}$$

---

## 3. Primer principio y termoquímica (Clase 8)

### Definiciones

- **Universo = sistema + entorno.**

| Sistema | Intercambia | Ejemplo |
|---|---|---|
| Abierto | Masa y energía | Olla destapada hirviendo |
| Cerrado | Solo energía | Sachet de leche |
| Aislado | Nada | Termo ideal, el universo |

| Pared | Permite | Su contraria |
|---|---|---|
| Permeable | Paso de materia | Impermeable |
| Móvil o flexible | Trabajo | Rígida |
| Diatérmica | Calor | Adiabática |

- **Función de estado**: depende solo del estado del sistema, no del camino. Son funciones de estado $P, V, T, U, H, S, G$. **$Q$ y $W$ no lo son.**
- **Extensiva** (depende de la cantidad): $U, H, S, G$, masa, volumen. **Intensiva**: $T$, $P$, densidad, y cualquier magnitud molar (kJ/mol).

### Convención de signos ("egoísta": todo visto desde el sistema)

| | Positivo | Negativo |
|---|---|---|
| $Q$ | El sistema **recibe** calor (endotérmico) | El sistema **libera** calor (exotérmico) |
| $W$ | El entorno hace trabajo sobre el sistema (**compresión**) | El sistema hace trabajo (**expansión**) |

### Primer principio

$$\Delta U = Q + W \qquad\qquad W = -P_{ext}\,\Delta V$$

- Es la conservación de la energía: **la energía de un sistema aislado es constante**.
- A **volumen constante** $W=0 \Rightarrow \Delta U = Q_V$.
- **Entalpía**: $H = U + PV$. A **presión constante** $\Delta H = Q_P$.
- $\Delta H<0$ exotérmico, $\Delta H>0$ endotérmico.
- Relación entre ambas:

$$\Delta H = \Delta U + \Delta n_{gas}\,RT \qquad \Delta n_{gas} = n_{gas,\ productos} - n_{gas,\ reactivos}$$

  - Sólidos y líquidos: el trabajo es despreciable $\Rightarrow \Delta H \approx \Delta U$.
  - Con gases solo son iguales si $\Delta n_{gas}=0$. Usar $R = 8{,}314\ J/(K\cdot mol)$.
- **Signo del trabajo en una reacción**: si $\Delta n_{gas}>0$ el sistema se expande y hace trabajo sobre el entorno ($W<0$); si $\Delta n_{gas}<0$ es al revés.

### Capacidad calorífica y calorimetría

$$Q = m\cdot C\cdot\Delta T = n\cdot\overline{C}\cdot\Delta T$$

- $C$ específica en $J/(g\cdot K)$, $\overline{C}$ molar en $J/(mol\cdot K)$. Agua líquida: $4{,}184\ J/(g\cdot K)$.
- Un $\Delta T$ vale lo mismo en °C que en K.
- Mayor capacidad calorífica $\Rightarrow$ **menor** cambio de temperatura para el mismo calor.
- Gases ideales: $\overline{C_p} = \overline{C_v} + R$, por lo tanto $C_p > C_v$.
- **Ley de Dulong y Petit**: para elementos sólidos, $\overline{C_p}\approx 3R \approx 25\ J/(mol\cdot K)$. Se cumple a temperatura alta (para la mayoría ya a temperatura ambiente); a baja temperatura falla y solo lo explica la física cuántica. Excepción: el carbono (diamante), que necesita temperaturas muy altas.
- **Cambio de fase**: la temperatura **no cambia** pero sí hay transferencia de calor, $Q_P = n\cdot\Delta H_{cambio\ de\ fase}$.

**Balance en un recipiente adiabático**: la suma de todos los calores es cero.

$$q_{reacción} + q_{solución} + q_{calorímetro} = 0$$

$$n\,\Delta H_r + m_{sc}\,C_{sc}\,\Delta T + C_k\,\Delta T = 0$$

- Calorímetro **ideal**: $C_k = 0$.
- Calorímetro **real**: absorbe parte del calor $\Rightarrow$ el cambio de temperatura es **menor** que en el ideal (si la reacción es exotérmica, $T_f$ queda más baja).
- Reacción **exotérmica** en recipiente adiabático: la temperatura **sube**. **Endotérmica**: **baja**.
- "Solo se aprovecha el X% del calor": $q_{útil} = \dfrac{X}{100}\cdot q_{liberado}$, así que hay que quemar **más** combustible: $q_{liberado} = q_{útil}\big/\frac{X}{100}$.

### Entalpía de reacción

- $\Delta H_r$ es **extensiva**: si se multiplica la ecuación por un factor, $\Delta H$ se multiplica por ese factor. Expresada por mol de una sustancia se vuelve intensiva.
- Si se **invierte** la ecuación, cambia el signo.
- Depende del **estado de agregación** (por eso hay que escribirlo): la combustión de $CH_4$ da $-890\ kJ$ con $H_2O(l)$ y $-802\ kJ$ con $H_2O(g)$.
- **Estado estándar (°)**: sustancia pura en su forma más estable a $1\ bar$ y a la temperatura indicada; solutos a $1\ M$. **No fija la temperatura** (las tablas suelen estar a 25 °C).
- **Ley de Hess**: como $H$ es función de estado, el $\Delta H$ de una reacción es la suma de los $\Delta H$ de las etapas en que se la descomponga.

**Tres formas de calcular $\Delta H°_r$:**

$$\textbf{1.}\ \ \Delta H°_r = \sum n\,\Delta H°_f(\text{productos}) - \sum n\,\Delta H°_f(\text{reactivos})$$

- $\Delta H°_f$: entalpía de formar **1 mol** de la sustancia a partir de sus **elementos en su forma más estable**.
- $\Delta H°_f = 0$ para los elementos en su forma más estable: $O_2(g)$, $H_2(g)$, $N_2(g)$, $C(grafito)$. **No** vale cero para el diamante ($+1{,}9\ kJ/mol$) ni para $O_3$.

$$\textbf{2.}\ \ \Delta H°_r = \sum D(\text{enlaces rotos, reactivos}) - \sum D(\text{enlaces formados, productos})$$

- $D$ (energía de disociación de enlace) es **siempre positiva**: romper un enlace absorbe energía, formarlo libera.
- Hay que contar **moles de enlaces** por mol de molécula (el $CH_4$ tiene 4 C–H; el $CO_2$ tiene 2 C=O).
- **El orden es al revés que con formación**: reactivos menos productos.
- Da un valor **aproximado**: las $D$ de tabla son **promedios** sobre muchas moléculas y valen para sustancias en **fase gaseosa**. Por eso no coincide exacto con el cálculo por $\Delta H°_f$ (ejemplo de clase: $-668$ contra $-802\ kJ$).

$$\textbf{3.}\ \ \text{Ley de Hess: combinar ecuaciones (invertir, multiplicar, sumar).}$$

---

## 4. Segundo principio: entropía y energía libre (Clases 9 y 10)

### Espontaneidad

- **Proceso espontáneo**: ocurre por sí mismo, sin acción externa continua. El **inverso** de un proceso espontáneo **no** es espontáneo.
- Los procesos no espontáneos **son posibles**, pero necesitan un agente externo.
- **Espontáneo no significa rápido**: la termodinámica no dice nada de la velocidad.
- **$\Delta H$ no sirve como criterio de espontaneidad**: el hielo se funde solo a 25 °C y es endotérmico.

### Entropía

- **Entropía ($S$)**: mide cómo se reparte la energía entre los niveles microscópicos disponibles. Es **función de estado** y **extensiva**.
- **Boltzmann**: $S = k\ln\Omega$, con $\Omega$ = número de microestados y $k = 1{,}38\times10^{-23}\ J/K$. Más microestados $\Rightarrow$ más entropía. $\Delta S = k\ln(\Omega_f/\Omega_i)$.
- **Segundo principio**: en todo proceso espontáneo **aumenta la entropía del universo**.

$$\Delta S_{universo} = \Delta S_{sistema} + \Delta S_{entorno}$$

| $\Delta S_{universo}$ | Proceso |
|---|---|
| $>0$ | Espontáneo |
| $=0$ | Reversible (equilibrio) |
| $<0$ | Imposible tal como está escrito |

- **La entropía del sistema puede disminuir** en un proceso espontáneo, siempre que la del entorno aumente más.
- **Entropía del entorno** (a $T$ y $P$ constantes): $\Delta S_{entorno} = -\dfrac{\Delta H_{sistema}}{T}$. Un proceso exotérmico aumenta la entropía del entorno; uno endotérmico la disminuye.
- **Cambio de fase en el equilibrio**: $\Delta S = \dfrac{\Delta H_{cambio\ de\ fase}}{T_{cambio}}$.
- **Tercer principio**: la entropía de un cristal puro y perfecto a $0\ K$ es cero (un solo microestado, $\ln 1 = 0$). Por eso existen **entropías absolutas** $S°$, y **$S°$ de un elemento no es cero** (a diferencia de $\Delta H°_f$ y $\Delta G°_f$).

$$\Delta S°_r = \sum n\,S°(\text{productos}) - \sum n\,S°(\text{reactivos})$$

### Cómo predecir el signo de $\Delta S$ sin cuentas

En este orden:

1. **Moles de gas**: si $\Delta n_{gas}>0 \Rightarrow \Delta S>0$; si $\Delta n_{gas}<0 \Rightarrow \Delta S<0$. Es el criterio que domina.
2. **Cambio de fase**: $S_{gas} \gg S_{líquido} > S_{sólido}$. Fusión, vaporización y sublimación: $\Delta S>0$. Los inversos: $\Delta S<0$.
3. **Disolución** de un sólido o líquido: $\Delta S>0$ en general.
4. **Temperatura**: al subir $T$, $S$ aumenta.
5. Más volumen disponible para un gas, o más partículas: $\Delta S>0$.

La justificación que piden es siempre con **microestados**: "aumenta el número de moles de gas, por lo tanto aumentan las posiciones y formas de repartir la energía (microestados accesibles), y la entropía aumenta".

### Energía libre de Gibbs

$$\Delta G = \Delta H - T\Delta S \qquad (T\text{ y }P\text{ constantes})$$

- Sale de $\Delta S_{universo}$: $\Delta G = -T\,\Delta S_{universo}$. Permite decidir la espontaneidad usando **solo propiedades del sistema**.
- $G$ es función de estado.

| $\Delta G$ | Significado |
|---|---|
| $<0$ | Espontánea tal como está escrita |
| $>0$ | No espontánea; es espontánea la inversa |
| $=0$ | Equilibrio |

**Los cuatro casos** (hay que saberlos de memoria):

| $\Delta H$ | $\Delta S$ | Espontaneidad | Ejemplo |
|---|---|---|---|
| $-$ | $+$ | Espontánea a **cualquier** temperatura | Combustiones que generan gas |
| $-$ | $-$ | Espontánea a temperaturas **bajas** | $H_2O(l)\to H_2O(s)$, síntesis de $NH_3$ |
| $+$ | $+$ | Espontánea a temperaturas **altas** | $CaCO_3 \to CaO + CO_2$, fusión |
| $+$ | $-$ | **No** espontánea a ninguna temperatura | $3O_2 \to 2O_3$ |

**Temperatura de inversión** (cae siempre, y la práctica no la ejercita):

$$\Delta G° = 0 \Rightarrow T_{inv} = \frac{\Delta H°}{\Delta S°}$$

- **Existe solo si $\Delta H$ y $\Delta S$ tienen el mismo signo.** Si tienen signos opuestos, $T$ daría negativa: no hay inversión.
- **Unidades**: $\Delta H°$ viene en kJ y $\Delta S°$ en J/K. Pasar uno de los dos antes de dividir.
- Supone que $\Delta H°$ y $\Delta S°$ no cambian con la temperatura.
- **Gráfico $\Delta G°$ vs $T$**: es una recta de ordenada al origen $\Delta H°$ y pendiente $-\Delta S°$. Corta el eje $T$ en $T_{inv}$.

**Dos formas de calcular $\Delta G°_r$** (preguntado textual en 2021: "¿existe otra manera?"):

$$\Delta G°_r = \Delta H°_r - T\Delta S°_r \qquad\qquad \Delta G°_r = \sum n\,\Delta G°_f(\text{productos}) - \sum n\,\Delta G°_f(\text{reactivos})$$

- $\Delta G°_f = 0$ para elementos en su forma más estable.
- La segunda forma con datos de tabla **solo vale a 25 °C**; para otra temperatura se usa la primera.
- Cuanto más negativo es $\Delta G°$, mayor tendencia a ocurrir. No dice nada de la velocidad.

---

# PARTE 2 – Preguntas conceptuales que ya cayeron

| Parcial | Pregunta | Respuesta |
|---|---|---|
| 2021 P1c | V o F: "Los gases reales se acercan a la idealidad a presiones altas y temperaturas altas" | **Falso.** Se acercan a **presiones bajas** y temperaturas altas. A presión alta las moléculas están cerca: pesan su volumen propio y las interacciones. |
| 2021 P1b | Globo con He y globo con CO₂, ¿cuál asciende? | El de **He**. $\rho = P\,Mr/RT$: a igual $P$ y $T$ la densidad depende de $Mr$. He (4) es menor que aire (29); CO₂ (44) es mayor. |
| 2022 2C P2 | Se agregan 2 mol de N₂ a $V$ y $T$ constantes | $P_{total}$ sube, densidad sube, fracciones molares de los otros gases bajan, **presiones parciales no cambian**. |
| 2024 P2 | Se retira el tabique entre dos tanques iguales | Cada gas ocupa el doble de volumen: su presión parcial cae a la mitad. $P_{final}$ = suma de las nuevas parciales. |
| 2022 1C P1 | ¿Qué volumen para duplicar $P$ a $T$ cte? ¿Y para la mitad de $T$ a $P$ cte? | La mitad del volumen (Boyle). La mitad del volumen (Charles, con $T$ en Kelvin). |
| 2022 1C P2d | ¿Cambia el limitante si se usa aire ($x_{O_2}=0{,}2$) en vez de O₂ puro? | Hay 5 veces menos moles de O₂ en el mismo volumen: hay que recalcular, y puede pasar a ser el limitante. |
| 2023 P3b | Calorímetro real en vez de ideal, ¿$T_f$ mayor, menor o igual? | **Menor** (reacción exotérmica): parte del calor lo absorbe el calorímetro. |
| 2022 1C P3b | $\Delta H_{disolución}>0$ en recipiente adiabático, ¿$T_f$ mayor o menor? | **Menor**: el proceso endotérmico toma calor de la propia solución. |
| 2025 P4e | Descomposición de CaCO₃ en recipiente adiabático | Es endotérmica ($\Delta H = +178\ kJ/mol$): la temperatura final es **menor**. |
| 2025 P4b | ¿El sistema hace trabajo sobre el entorno o al revés? | Se forma 1 mol de gas ($\Delta n_{gas}=+1$): el sistema se **expande y hace trabajo** sobre el entorno, $W<0$. |
| 2022 1C P3c | Calcular $\Delta U$ a partir de $\Delta H$, indicando suposiciones | $\Delta U = \Delta H - \Delta n_{gas}RT$. Suposiciones: gases ideales, $P$ y $T$ constantes, volumen de sólidos y líquidos despreciable. |
| 2024 P3a | $\Delta U$ de una neutralización en solución | No hay gases: $\Delta n_{gas}=0$, $\Delta U \approx \Delta H$. |
| 2021 P3c | Con $\Delta H>0$, ¿se puede afirmar que no es espontánea? | **No.** El criterio es $\Delta G$, no $\Delta H$. Hace falta conocer $\Delta S$ y $T$. |
| 2022 1C P4a | Signo de $\Delta S$: agua líquida → vapor; $2H(g)\to H_2(g)$ | Positivo (pasa a gas, más microestados). Negativo (2 moles de gas dan 1). |
| 2022 1C P4b | Haber-Bosch: signo de $\Delta S$, y qué se concluye si $\Delta H<0$ | $\Delta S<0$ (4 moles de gas dan 2). Con $\Delta H<0$ y $\Delta S<0$: espontánea solo a **baja** temperatura; deja de serlo por encima de $T=\Delta H/\Delta S$. |
| 2024 P4 | Combustión de acetona: signo de $\Delta S$ y gráfico $\Delta G$ vs $T$ | Con agua gaseosa pasan 4 moles de gas a 6: $\Delta S>0$. Con $\Delta H<0$: espontánea a toda temperatura, **no hay temperatura de inversión**. Recta con ordenada $\Delta H$ y pendiente negativa. |
| 2022 2C P4g | ¿Hay un intervalo de $T$ donde no sea espontánea? ($\Delta H<0$, $\Delta S>0$) | **No**: $\Delta G<0$ para toda $T$. |
| 2023 P4b | ¿A qué $T$ están en equilibrio CO, O₂ y CO₂? | $\Delta G=0 \Rightarrow T = \Delta H/\Delta S = (-283{,}0\ kJ)/(-0{,}0866\ kJ/K) \approx 3270\ K$. |
| 2023 P4c | ¿Cómo puede congelarse el agua si $S_{hielo}<S_{líquido}$? | El segundo principio habla del **universo**. Congelar es exotérmico: el calor liberado aumenta la entropía del entorno ($-\Delta H/T$), y por debajo de 0 °C ese aumento supera la disminución del sistema. |
| 2025 P4f | ¿La reacción invierte su sentido a alguna $T$? | Sí: $\Delta H>0$ y $\Delta S>0$. $T = 178{,}3/0{,}1589 \approx 1122\ K$; por encima es espontánea. |

### Ejemplo completo: P4 de 2025, $CaCO_3(s)\to CaO(s)+CO_2(g)$

Datos: $\Delta H°_f$: $-1206{,}9$; $-635{,}1$; $-393{,}5$ kJ/mol. $\Delta G°_f$: $-1128{,}8$; $-604{,}0$; $-394{,}4$ kJ/mol. $S°$: $92{,}9$; $38{,}1$; $213{,}7$ J/(mol·K).

- $\Delta H°_r = (-635{,}1-393{,}5)-(-1206{,}9) = +178{,}3\ kJ/mol$ (endotérmica).
- Calor para 2 kg: $n = 2000/100{,}09 = 19{,}98\ mol \Rightarrow q_P = 19{,}98\times178{,}3 = 3563\ kJ$ absorbidos.
- Trabajo: $\Delta n_{gas}=+1$, el sistema hace trabajo sobre el entorno.
- Signo de $\Delta S$: positivo, se genera un gas a partir de un sólido.
- $\Delta S°_r = (38{,}1+213{,}7)-92{,}9 = +158{,}9\ J/(mol\cdot K)$.
- $\Delta G°_r = (-604{,}0-394{,}4)-(-1128{,}8) = +130{,}4\ kJ/mol$: **no espontánea a 25 °C**.
- Recipiente adiabático: endotérmica, la temperatura baja.
- Inversión: $T = \dfrac{178\,300\ J}{158{,}9\ J/K} = 1122\ K \approx 849\ °C$. Por encima, $\Delta G<0$.

---

# PARTE 3 – Banco de verdadero/falso

Tapar las dos columnas de la derecha y contestar justificando en una línea.

## Gases

| # | Afirmación | Rta | Por qué |
|---|---|---|---|
| 1 | Los gases reales se acercan al comportamiento ideal a presiones altas y temperaturas altas. | F | A presiones **bajas** y temperaturas altas. |
| 2 | En un gas ideal las partículas no interactúan entre sí. | V | Es uno de los supuestos del modelo. |
| 3 | A $T$ constante, si el volumen se reduce a la mitad la presión se duplica. | V | Boyle: $PV$ = cte. |
| 4 | A $V$ constante, calentar un gas de 20 °C a 40 °C duplica su presión. | F | La proporcionalidad es con $T$ en Kelvin: $313/293 = 1{,}07$. |
| 5 | Un mol de cualquier gas ideal ocupa 22,4 L. | F | Solo en CNPT (1 atm y 273 K). |
| 6 | A igual $P$ y $T$, volúmenes iguales de H₂ y de CO₂ contienen el mismo número de moléculas. | V | Ley de Avogadro. |
| 7 | A igual $P$ y $T$, volúmenes iguales de H₂ y de CO₂ tienen la misma masa. | F | Mismo $n$, distinto $Mr$. |
| 8 | A igual $P$ y $T$, el gas de mayor masa molar es el más denso. | V | $\rho = P\,Mr/RT$. |
| 9 | La densidad de un gas aumenta al calentarlo a presión constante. | F | $\rho$ es inversamente proporcional a $T$. |
| 10 | La presión parcial de un gas es la que ejercería si estuviera solo en el recipiente. | V | Definición (Dalton). |
| 11 | Al agregar He a una mezcla a $V$ y $T$ constantes, las presiones parciales de los otros gases disminuyen. | F | No cambian; baja su fracción molar y sube la $P$ total. |
| 12 | Al agregar un gas a una mezcla a $V$ y $T$ constantes, la fracción molar de los demás disminuye. | V | Mismo $n_A$, mayor $n_{total}$. |
| 13 | En una mezcla, el gas con mayor fracción molar tiene la mayor presión parcial. | V | $P_A = x_A P_{total}$. |
| 14 | La presión de un gas se debe a los choques de las partículas contra las paredes. | V | $P=F/A$. |
| 15 | Si se duplican los moles de gas a $P$ y $T$ constantes, el volumen se duplica. | V | Avogadro. |

## Estequiometría

| # | Afirmación | Rta | Por qué |
|---|---|---|---|
| 16 | En una reacción se conserva el número de moles. | F | Se conservan átomos y masa. |
| 17 | En una reacción se conserva la masa total. | V | Ley de conservación de la masa. |
| 18 | El reactivo limitante es el que está en menor masa. | F | Depende de los moles y de los coeficientes. |
| 19 | El reactivo limitante es el que tiene menos moles. | F | Hay que comparar moles dividido coeficiente. |
| 20 | Al terminar la reacción queda reactivo en exceso junto con los productos. | V | Solo el limitante se consume del todo. |
| 21 | Los coeficientes estequiométricos indican la relación en gramos. | F | Relación en moles o moléculas. |
| 22 | Para balancear se pueden modificar los subíndices de las fórmulas. | F | Cambiaría la sustancia; solo coeficientes. |
| 23 | El rendimiento de una reacción puede ser mayor al 100%. | F | La cantidad real no supera la teórica. |
| 24 | Si un reactivo tiene 80% de pureza, hace falta más masa de muestra que si fuera puro. | V | $m_{muestra} = m_{pura}/0{,}80$. |
| 25 | Con rendimiento menor al 100% se necesita más reactivo para obtener la misma cantidad de producto. | V | $n_{teórico} = n_{real}/\text{rendimiento}$. |
| 26 | La cantidad de producto se calcula a partir del reactivo en exceso. | F | Siempre desde el limitante. |

## Primer principio y termoquímica

| # | Afirmación | Rta | Por qué |
|---|---|---|---|
| 27 | El calor y el trabajo son funciones de estado. | F | Dependen del camino. $U$ y $H$ sí lo son. |
| 28 | Un sistema cerrado no intercambia energía con el entorno. | F | No intercambia **materia**; el que no intercambia nada es el aislado. |
| 29 | Una pared adiabática impide el intercambio de calor. | V | Definición. |
| 30 | Cuando un gas se expande contra una presión externa, $W$ es negativo. | V | El sistema hace trabajo: $W=-P_{ext}\Delta V$ con $\Delta V>0$. |
| 31 | En un proceso exotérmico $Q>0$. | F | El sistema libera calor: $Q<0$. |
| 32 | A volumen constante el calor intercambiado es igual a $\Delta H$. | F | Es igual a $\Delta U$. $\Delta H = Q_P$. |
| 33 | La energía de un sistema aislado es constante. | V | Primer principio. |
| 34 | Para reacciones entre sólidos y líquidos, $\Delta H\approx\Delta U$. | V | El trabajo de volumen es despreciable. |
| 35 | En una reacción con gases siempre $\Delta H \neq \Delta U$. | F | Son iguales si $\Delta n_{gas}=0$. |
| 36 | Durante un cambio de fase el sistema no intercambia calor porque $T$ no cambia. | F | Hay calor latente: $Q=n\Delta H$. |
| 37 | $\Delta H_r$ es una magnitud extensiva. | V | Se duplica al duplicar la ecuación. |
| 38 | Al invertir una reacción, $\Delta H$ cambia de signo. | V | $H$ es función de estado. |
| 39 | El $\Delta H$ de combustión del metano es igual si el agua queda líquida o gaseosa. | F | Depende del estado de agregación ($-890$ y $-802\ kJ$). |
| 40 | La entalpía estándar de formación de $O_2(g)$ es cero. | V | Elemento en su forma más estable. |
| 41 | La entalpía estándar de formación del diamante es cero. | F | La forma estable del carbono es el grafito. |
| 42 | El estado estándar implica una temperatura de 25 °C. | F | Fija la presión (1 bar) y la pureza, no la temperatura. |
| 43 | Las energías de disociación de enlace son siempre positivas. | V | Romper un enlace requiere energía. |
| 44 | Formar un enlace absorbe energía. | F | La libera. |
| 45 | El $\Delta H$ calculado con energías de enlace coincide exactamente con el calculado con $\Delta H°_f$. | F | Las energías de enlace son promedios y valen en fase gaseosa. |
| 46 | Con energías de enlace, $\Delta H_r = \sum D_{productos} - \sum D_{reactivos}$. | F | Es reactivos menos productos. |
| 47 | La ley de Hess es consecuencia de que $H$ es función de estado. | V | El $\Delta H$ no depende del camino. |
| 48 | Para un gas ideal, $C_p$ es mayor que $C_v$. | V | $C_p = C_v + R$. |
| 49 | La capacidad calorífica molar de los elementos sólidos es cercana a $3R$. | V | Dulong y Petit, a temperatura alta. |
| 50 | La ley de Dulong y Petit se cumple mejor a bajas temperaturas. | F | A altas; a bajas falla (efecto cuántico). |
| 51 | Una reacción exotérmica en un recipiente adiabático aumenta la temperatura. | V | El calor queda en el sistema. |
| 52 | Con un calorímetro real, el aumento de temperatura de una reacción exotérmica es mayor que con uno ideal. | F | Menor: el calorímetro absorbe parte del calor. |
| 53 | Para el mismo calor, la sustancia de mayor capacidad calorífica cambia menos su temperatura. | V | $\Delta T = Q/(mC)$. |

## Segundo principio, entropía y Gibbs

| # | Afirmación | Rta | Por qué |
|---|---|---|---|
| 54 | Toda reacción exotérmica es espontánea. | F | Depende de $\Delta G$. Si $\Delta S<0$, deja de serlo a $T$ alta. |
| 55 | Una reacción endotérmica nunca es espontánea. | F | Lo es a $T$ alta si $\Delta S>0$ (fusión del hielo a 25 °C). |
| 56 | Espontáneo significa que ocurre rápido. | F | La termodinámica no informa la velocidad. |
| 57 | Un proceso no espontáneo es imposible. | F | Puede ocurrir con acción externa continua. |
| 58 | Si un proceso es espontáneo, el inverso no lo es en las mismas condiciones. | V | $\Delta G$ cambia de signo. |
| 59 | En todo proceso espontáneo aumenta la entropía del sistema. | F | Aumenta la del **universo**. |
| 60 | La entropía del universo aumenta en todo proceso espontáneo. | V | Segundo principio. |
| 61 | La entropía de un sistema nunca puede disminuir. | F | Puede, si la del entorno aumenta más (congelación). |
| 62 | A la misma temperatura, $S_{gas}>S_{líquido}>S_{sólido}$. | V | Más microestados accesibles. |
| 63 | La entropía de una sustancia aumenta con la temperatura. | V | Más energía para repartir. |
| 64 | A mayor número de microestados, mayor entropía. | V | $S=k\ln\Omega$. |
| 65 | Un aumento de los moles de gas en una reacción implica $\Delta S>0$. | V | Los gases dominan la entropía. |
| 66 | Para $N_2(g)+3H_2(g)\to2NH_3(g)$, $\Delta S>0$. | F | 4 moles de gas dan 2: $\Delta S<0$. |
| 67 | La entropía estándar de un elemento en su forma estable es cero. | F | Solo es cero a 0 K para un cristal perfecto; lo que vale cero es $\Delta H°_f$ y $\Delta G°_f$. |
| 68 | La entropía de un cristal puro y perfecto a 0 K es cero. | V | Tercer principio. |
| 69 | Un proceso exotérmico aumenta la entropía del entorno. | V | $\Delta S_{ent} = -\Delta H_{sis}/T$. |
| 70 | La entropía es una función de estado. | V | $\Delta S = S_f - S_i$. |
| 71 | Si $\Delta G<0$ la reacción es espontánea tal como está escrita. | V | A $T$ y $P$ constantes. |
| 72 | Si $\Delta G=0$ el sistema está en equilibrio. | V | No hay cambio neto. |
| 73 | Si $\Delta H<0$ y $\Delta S>0$, la reacción es espontánea a cualquier temperatura. | V | $\Delta G$ siempre negativo. |
| 74 | Si $\Delta H>0$ y $\Delta S<0$, la reacción es espontánea a temperaturas altas. | F | No es espontánea a ninguna temperatura. |
| 75 | Si $\Delta H<0$ y $\Delta S<0$, la reacción es espontánea a temperaturas altas. | F | A temperaturas bajas. |
| 76 | Si $\Delta H>0$ y $\Delta S>0$, existe una temperatura por encima de la cual la reacción es espontánea. | V | $T>\Delta H/\Delta S$. |
| 77 | Toda reacción tiene una temperatura de inversión de la espontaneidad. | F | Solo si $\Delta H$ y $\Delta S$ tienen el mismo signo. |
| 78 | En el gráfico $\Delta G°$ vs $T$, la pendiente es $\Delta S°$. | F | Es $-\Delta S°$; la ordenada al origen es $\Delta H°$. |
| 79 | $\Delta G°_f$ de $O_2(g)$ es cero. | V | Elemento en su forma estable. |
| 80 | $\Delta G°$ se puede calcular tanto con $\Delta G°_f$ como con $\Delta H°-T\Delta S°$. | V | Son las dos formas vistas en clase. |
| 81 | El $\Delta G°$ calculado con $\Delta G°_f$ de tabla sirve para cualquier temperatura. | F | Solo para 25 °C; para otra $T$ se usa $\Delta H°-T\Delta S°$. |
| 82 | Cuanto más negativo es $\Delta G°$, más rápida es la reacción. | F | Indica tendencia, no velocidad. |
| 83 | El agua puede congelarse espontáneamente aunque su entropía disminuya. | V | Por debajo de 0 °C el aumento de entropía del entorno es mayor. |
| 84 | El signo de $\Delta H$ alcanza para saber si una reacción es espontánea. | F | Hace falta $\Delta S$ y $T$. |

---

# Machete de fórmulas

$$PV=nRT \qquad P_A = x_AP_T \qquad \rho=\frac{P\,Mr}{RT} \qquad \frac{P_1V_1}{T_1}=\frac{P_2V_2}{T_2}$$

$$\text{Rend. \%}=\frac{\text{real}}{\text{teórico}}\times100 \qquad \text{Pureza \%}=\frac{m_{pura}}{m_{muestra}}\times100$$

$$\Delta U=Q+W \qquad W=-P_{ext}\Delta V \qquad \Delta H=\Delta U+\Delta n_{gas}RT \qquad Q=mC\Delta T$$

$$\Delta H°_r=\sum n\Delta H°_f(prod)-\sum n\Delta H°_f(react) \qquad \Delta H°_r=\sum D(react)-\sum D(prod)$$

$$\Delta S°_r=\sum nS°(prod)-\sum nS°(react) \qquad \Delta S_{ent}=-\frac{\Delta H_{sis}}{T} \qquad \Delta S_{fase}=\frac{\Delta H_{fase}}{T}$$

$$\Delta G=\Delta H-T\Delta S \qquad \Delta G°_r=\sum n\Delta G°_f(prod)-\sum n\Delta G°_f(react) \qquad T_{inv}=\frac{\Delta H°}{\Delta S°}$$

**Los errores de unidades que más puntos cuestan:**

- $T$ en °C dentro de $PV=nRT$ o de $\Delta G=\Delta H-T\Delta S$.
- $\Delta H$ en kJ y $\Delta S$ en J/K sin convertir.
- $R=0{,}082$ para energía: en $\Delta n_{gas}RT$ va $8{,}314\ J/(K\cdot mol)$.
- Usar 22,4 L/mol fuera de CNPT.
- Presión en Torr o mmHg sin pasar a atm.
