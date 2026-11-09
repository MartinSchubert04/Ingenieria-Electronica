# Resumen corto — Tercer Parcial de Química General

> **Alcance:** Serie 8 (Equilibrio químico), Serie 9 (Ácido-base) y Serie 10 (Cinética).
> **Fuentes:** el programa 2C 2026, las hojas de fórmulas de los parciales 2024 y 2025, y
> las resoluciones corregidas de `Parciales/3ª Parcial/Resueltos/`. Las clases de estas
> series todavía no están en `practicas/teoria/`: cuando las suban, conviene chequear la
> notación contra ellas.
> Para qué parciales hacer, ver [guia-3er-parcial.md](guia-3er-parcial.md).

**Qué te dan en la hoja de fórmulas:** ΔG = ΔH − TΔS, ΔG = ΔG° + RT ln Q, Kp = Kc·(RT)^Δn,
Van't Hoff, las leyes integradas con su t½, Arrhenius, Ka·Kb = 10⁻¹⁴ y R. **No te dan**
los conceptos de abajo: eso es lo que se justifica en palabras.

---

## 1. Equilibrio químico (Serie 8)

### La idea

- Una reacción reversible llega al **equilibrio dinámico**: la reacción directa y la
  inversa siguen ocurriendo, pero **a la misma velocidad**, así que las concentraciones
  ya no cambian.
- La **constante de equilibrio K** depende **solo de la temperatura**.
  - K ≫ 1: en el equilibrio hay mayoría de productos.
  - K ≪ 1: en el equilibrio casi todo son reactivos.

### Fórmulas

Para $a\,\mathrm{A} + b\,\mathrm{B} \rightleftharpoons c\,\mathrm{C} + d\,\mathrm{D}$ (**ley de acción de masas**):

$$K_c = \frac{[\mathrm{C}]^c[\mathrm{D}]^d}{[\mathrm{A}]^a[\mathrm{B}]^b} \qquad K_p = \frac{P_\mathrm{C}^c\,P_\mathrm{D}^d}{P_\mathrm{A}^a\,P_\mathrm{B}^b} \qquad K_p = K_c\,(RT)^{\Delta n}$$

- **Sólidos y líquidos puros no entran en K**: su concentración es constante.
- Δn = moles de gas en productos − moles de gas en reactivos (solo gases).
- Para pasar de concentración a presión: $P_i = [i]\,RT$, con R = 0,082 y T en K.

**Q contra K** (Q es la misma expresión que K, pero con los valores de *ese momento*):

| Comparación | Qué hace el sistema |
| --- | --- |
| Q < K | avanza hacia **productos** |
| Q > K | avanza hacia **reactivos** |
| Q = K | está en equilibrio |

**Relación con la termodinámica:**

$$\Delta G^\circ = -RT\ln K \qquad \Delta G = \Delta G^\circ + RT\ln Q$$

- En el equilibrio, **ΔG = 0** y Q = K.
- ΔG° < 0 equivale a K > 1.

**Van't Hoff** (cómo cambia K con T):

$$\ln\frac{K(T_1)}{K(T_2)} = -\frac{\Delta H^\circ}{R}\left(\frac{1}{T_1}-\frac{1}{T_2}\right) \qquad \ln K = -\frac{\Delta H^\circ}{R}\cdot\frac{1}{T} + \frac{\Delta S^\circ}{R}$$

- Si te dan el **gráfico de ln K contra 1/T**, la recta es la segunda fórmula:
  - pendiente = −ΔH°/R
  - ordenada = ΔS°/R
- Pendiente negativa → ΔH° > 0 (endotérmica).
- En estas fórmulas R = 8,314 J/(mol·K).

### Cómo se resuelve (método de la cátedra)

1. Escribir la expresión de K, sin sólidos.
2. Calcular Q inicial para saber hacia dónde va.
3. Armar la tabla **inicial / cambio / equilibrio**, con el cambio en x según los
   coeficientes. El sólido va como "exceso".
4. Reemplazar en K y despejar x. Si es cuadrática, **descartar la raíz que da una
   concentración negativa** y decirlo.
5. Verificar: los valores de equilibrio, reemplazados en K, tienen que dar K.

### Le Chatelier: si se perturba el equilibrio, el sistema se corre para contrarrestarlo

| Perturbación | Efecto |
| --- | --- |
| Agregar reactivo o sacar producto | Q < K → hacia **productos** |
| Agregar producto o sacar reactivo | Q > K → hacia **reactivos** |
| Bajar V (subir P) a T constante | hacia el lado con **menos moles de gas** |
| Subir T | hacia el lado **endotérmico**; es lo **único que cambia K** |
| Agregar sólido | **nada**: no está en Q |
| Gas inerte a V constante | **nada**: las presiones parciales no cambian |
| Gas inerte a P constante | aumenta V → hacia el lado con más moles de gas |
| Catalizador | **nada**: llega antes al equilibrio, K igual |

### Equilibrio heterogéneo (sólido que se descompone en gas)

Ejemplo: CaCO₃(s) ⇌ CaO(s) + CO₂(g).

- **K depende solo del gas:** $K_p = P_{\mathrm{CO_2}}$.
- Mientras quede algo de sólido, **la presión de equilibrio no depende de cuánto sólido
  pusiste**.
- Los moles de sólido que reaccionaron salen de los moles de gas formados, por
  estequiometría.

---

## 2. Ácido-base (Serie 9)

### Definiciones

- **Arrhenius:** ácido = libera H⁺ en agua; base = libera OH⁻.
- **Brønsted-Lowry:** ácido = **dona** H⁺; base = **acepta** H⁺.
  - Al donar, el ácido queda como su **base conjugada** (HA / A⁻).
- **Lewis:** ácido = acepta un par de electrones; base = lo dona. Por ejemplo, el NH₃ y
  las aminas tienen un par libre en el N.

### Agua y pH

$$K_w = [\mathrm{H_3O^+}][\mathrm{OH^-}] = 1\times10^{-14}\ (25\,°\mathrm{C}) \qquad \mathrm{pH} = -\log[\mathrm{H_3O^+}] \qquad \mathrm{pH} + \mathrm{pOH} = 14$$

- **Neutro** quiere decir [H₃O⁺] = [OH⁻]. Eso da pH = 7 **solo a 25 °C**, porque Kw
  cambia con la temperatura.

### Fuertes y débiles

**Fuerte:** se disocia **totalmente**.
- [H₃O⁺] = C (o [OH⁻] = C).
- Ojo con Ca(OH)₂ o Mg(OH)₂: dan 2 OH⁻ por fórmula, así que [OH⁻] = 2C.

**Débil:** se disocia **parcialmente**, y hay un equilibrio con Ka (o Kb):

$$K_a = \frac{[\mathrm{A^-}][\mathrm{H_3O^+}]}{[\mathrm{HA}]} = \frac{x^2}{C - x} \qquad \alpha = \frac{x}{C} \qquad \mathrm{p}K_a = -\log K_a$$

- Aproximación C − x ≈ C: vale si x da menos del 5 % de C. Hay que **verificarla y
  decirlo**.
- **Mayor Ka** (menor pKa) = ácido más fuerte.
- **Grado de disociación α:**
  - **aumenta al diluir** (Le Chatelier: el equilibrio se corre hacia el lado con más
    partículas disueltas);
  - **disminuye si agregás el ion común**: por ejemplo, la sal A⁻ corre el equilibrio
    hacia HA.
- **Par conjugado:** $K_a \cdot K_b = K_w$.
  - Cuanto más débil el ácido, más fuerte su base conjugada.
  - La conjugada de un ácido fuerte (Cl⁻, NO₃⁻) no tiene fuerza ácido-base.

### Hidrólisis de sales: pensar de qué ácido y de qué base viene cada ion

| La sal viene de... | Ejemplo | La solución es |
| --- | --- | --- |
| ácido fuerte + base fuerte | NaCl, KNO₃, Na₂SO₄ | **neutra** |
| ácido débil + base fuerte | NaF, KNO₂, HCOOK | **básica**: A⁻ + H₂O ⇌ HA + OH⁻ |
| ácido fuerte + base débil | NH₄Cl, cloruro de piridinio | **ácida**: BH⁺ + H₂O ⇌ B + H₃O⁺ |
| ácido débil + base débil | NH₄NO₂, NH₄F | depende: comparar Ka del catión con Kb del anión |

Para calcular el pH de la sal, usar la constante del ion que hidroliza: $K_b = K_w / K_a$.

**Ordenar por pH sin cuentas** (a igual concentración), de menor a mayor:
1. ácidos fuertes (el diprótico H₂SO₄ es más ácido que el HI);
2. ácidos débiles (de mayor a menor Ka);
3. sales ácidas;
4. sales neutras;
5. sales básicas;
6. bases débiles;
7. bases fuertes (Mg(OH)₂ da el doble de OH⁻).

### Titulación (neutralización)

- **Punto de equivalencia (PE):** se agregaron los moles justos para neutralizar.
  Para monopróticos:

   $$n_{\text{ácido}} = n_{\text{base}} \;\Rightarrow\; C_a V_a = C_b V_b$$

- **El pH en el PE lo decide la sal que se formó:**
  - fuerte + fuerte → 7;
  - **ácido débil + base fuerte → mayor que 7** (A⁻ hidroliza);
  - base débil + ácido fuerte → menor que 7.
- **Cálculo del pH en el PE:**
  1. Concentración de la sal = moles / **volumen total** (V ácido + V base).
  2. Plantear la hidrólisis con $K_b = K_w/K_a$ (o $K_a = K_w/K_b$).
  3. Sacar pOH (o pH).
- **Mezcla de un ácido fuerte con una base fuerte:** el que esté en exceso decide el pH,
  con su concentración calculada sobre el volumen total.
- **Indicador:** elegir uno cuyo **rango de viraje contenga el pH del PE**.
- **Punto final:** cuando el indicador cambia de color. Idealmente coincide con el PE.

---

## 3. Cinética (Serie 10)

### La idea

- La **velocidad** es cuánto cambia una concentración por unidad de tiempo. Con el
  coeficiente *a* del reactivo:

   $$v = -\frac{1}{a}\frac{d[\mathrm{A}]}{dt} \qquad v = k[\mathrm{A}]^m$$

- El **orden m se determina experimentalmente**: no tiene por qué coincidir con el
  coeficiente estequiométrico.
- **k depende de T** (y del catalizador), no de las concentraciones.

### Leyes integradas (notación de la hoja de fórmulas, con *a* = coeficiente de A)

| Orden | Ley integrada | Gráfico que da recta | t½ | Unidades de k |
| --- | --- | --- | --- | --- |
| 0 | [A] = [A]₀ − a·k·t | [A] contra t | [A]₀ / (2ak) | M/s |
| 1 | ln[A] = ln[A]₀ − a·k·t | ln[A] contra t | ln 2 / (ak) | 1/s |
| 2 | 1/[A] = 1/[A]₀ + a·k·t | 1/[A] contra t | 1 / ([A]₀·a·k) | 1/(M·s) |

- **Orden a partir de gráficos:** el que es recta (R² más cerca de 1) da el orden.
  - La pendiente es −ak (orden 0 y 1) o +ak (orden 2).
  - La ordenada da [A]₀, ln[A]₀ o 1/[A]₀.
- **Orden a partir de datos:** "si triplico [A], la velocidad aumenta 9 veces":

   $$\frac{v_2}{v_1} = \left(\frac{[\mathrm{A}]_2}{[\mathrm{A}]_1}\right)^m \;\Rightarrow\; 9 = 3^m \;\Rightarrow\; m = 2$$

- **Orden a partir de las unidades de k:** ver la última columna de la tabla.
- **"Se consumió un p %"** quiere decir que queda $[\mathrm{A}] = (1 - p)\,[\mathrm{A}]_0$. Por ejemplo, consumir el 80 % deja $0{,}20\,[\mathrm{A}]_0$.
- **Solo en orden 1** la vida media no depende de [A]₀: es constante.

### Temperatura: Arrhenius

$$k = A\,e^{-E_a/RT} \qquad \ln\frac{k(T_1)}{k(T_2)} = -\frac{E_a}{R}\left(\frac{1}{T_1}-\frac{1}{T_2}\right)$$

- Gráfico de ln k contra 1/T: **pendiente = −Ea/R**.
- **Ea (energía de activación):** la barrera de energía mínima que tienen que superar
  los choques para que se forme producto (pasando por el complejo activado).
- Ea **no cambia con T**: al subir T, más moléculas superan la barrera, y por eso k
  aumenta.
- **Catalizador:** ofrece un camino con **menor Ea**. Acelera tanto la reacción directa
  como la inversa, **no cambia ΔH ni K** y no se consume.
- **Diagrama de energía:** ΔH = Ea(directa) − Ea(inversa).

---

## Errores típicos que bajan puntos

- Meter el sólido en K, o usar los moles del sólido para calcular el equilibrio.
- Olvidarse de multiplicar x (mol/L) por V para pasar a moles o a gramos.
- Usar R = 0,082 en Van't Hoff o Arrhenius (va 8,314), o T en °C.
- Mezclar kJ y J: ΔH° suele venir en kJ/mol y ΔS° en J/(mol·K).
- En titulaciones, calcular concentraciones con el volumen inicial en vez del total.
- No escribir las reacciones: varios parciales piden "Escriba TODAS las reacciones".
- Decir que un catalizador desplaza el equilibrio o cambia K.
