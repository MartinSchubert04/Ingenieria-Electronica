# Teoría para el 2º Parcial — Continuidad, derivadas y aplicaciones

Resumen de las prácticas 6, 7 y 8, ordenado según los **6 ejercicios del parcial M1**
(ver `guia-2do-parcial.md`). Cada tema tiene: qué dice la teoría, cómo se aplica y un
ejemplo resuelto. **Los ejemplos no son los del parcial**: son del mismo tipo, para que
practiques la técnica y después hagas el parcial vos.

Basado en `teoria/Material de lectura/definiciones y propiedades practica 6.pdf` y
`... practica 7.pdf` (las de la cátedra). Las diapositivas 12 a 20 de
`teoria/Pases de diapositivas M1/` cubren lo mismo con más detalle.

---

## Índice

0. [Continuidad (base de todo)](#0-continuidad-base-de-todo)
1. [Ejercicio 1 — Bolzano y derivada por definición](#ejercicio-1--bolzano-y-derivada-por-definición)
2. [Ejercicio 2 — Recta tangente / normal con parámetro](#ejercicio-2--recta-tangente--normal-con-parámetro)
3. [Ejercicio 3 — Derivación implícita (y logarítmica)](#ejercicio-3--derivación-implícita-y-logarítmica)
4. [Ejercicio 4 — Asíntotas y L'Hôpital](#ejercicio-4--asíntotas-y-lhôpital)
5. [Ejercicio 5 — Estudio de función con $f'$ y $f''$ dadas](#ejercicio-5--estudio-de-función-con-f-y-f-dadas)
6. [Ejercicio 6 — Optimización en intervalo cerrado](#ejercicio-6--optimización-en-intervalo-cerrado)
7. [Errores que cuestan puntos](#errores-que-cuestan-puntos)

---

## 0. Continuidad (base de todo)

**Definición.** $f$ es continua en $a$ si se cumplen las tres cosas:

1. $a \in \operatorname{Dom}(f)$ (existe $f(a)$),
2. existe $\displaystyle\lim_{x \to a} f(x)$ (los laterales existen y son iguales),
3. $\displaystyle\lim_{x \to a} f(x) = f(a)$.

**Qué es continuo sin hacer cuentas:** polinomios, $\operatorname{sen}$, $\cos$, $e^x$,
$\ln x$ (en $x > 0$), raíces (en su dominio), y sumas, productos, cocientes (donde el
denominador no se anula) y composiciones de continuas. En el parcial alcanza con decir
*"$f$ es continua en $[a, b]$ por ser suma/producto/composición de funciones continuas
y $0 \notin [a, b]$"* (o lo que corresponda).

**Tipos de discontinuidad**

| Tipo | Qué pasa |
| --- | --- |
| Evitable | El límite existe pero $f(a)$ no existe o es distinto |
| De salto | Los dos laterales existen (finitos) y son distintos |
| Esencial / infinita | Algún lateral no existe o es $\pm\infty$ |

### Ejemplo — continuidad con un parámetro

$$
f(x) = \begin{cases} ax + 1 & x < 2 \\ x^2 & x \ge 2 \end{cases}
\qquad \text{¿Para qué } a \text{ es continua en } \mathbb{R}\text{?}
$$

Fuera de $x = 2$ es continua (cada tramo es polinomio). En $x = 2$ hay que pedir:

$$\lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = f(2)$$

$$2a + 1 = 4 = 4 \quad\Longrightarrow\quad a = \tfrac{3}{2}$$

---

## Ejercicio 1 — Bolzano y derivada por definición

### 1.1 Teorema de Bolzano

> Si $f$ es **continua en $[a, b]$** y $f(a)$, $f(b)$ tienen **signos opuestos**,
> entonces existe $c \in (a, b)$ con $f(c) = 0$.

### 1.2 Teorema de los valores intermedios (TVI)

> Si $f$ es **continua en $[a, b]$** y $k$ está entre $f(a)$ y $f(b)$,
> entonces existe $c \in (a, b)$ con $f(c) = k$.

Son lo mismo: para probar $f(c) = k$ con Bolzano, se lo aplicás a $g(x) = f(x) - k$.

**Receta para "probá que existe $c$ con $f(c) = k$":**

1. Definí $g(x) = f(x) - k$ (o usá TVI directo).
2. Elegí $a$ y $b$ fáciles de evaluar (donde se anulen $\operatorname{sen}$, $\ln$, etc.:
   $x = 0,\ \pi,\ 1,\ e, \dots$) con signos opuestos de $g$.
3. **Justificá la continuidad en $[a, b]$** — es lo que más se olvida.
   Si el dominio tiene un agujero, el intervalo **no puede contenerlo**.
4. Concluí: "por Bolzano existe $c \in (a, b)$ tal que $g(c) = 0$, es decir $f(c) = k$".

#### Ejemplo — TVI

Probar que existe $c$ con $e^c + c = 3$.

$g(x) = e^x + x$ es continua en $\mathbb{R}$ (suma de continuas). Busco dónde queda
por debajo y por encima de $3$:

$$g(0) = e^0 + 0 = 1 < 3 \qquad g(1) = e + 1 \approx 3{,}72 > 3$$

Como $g$ es continua en $[0, 1]$ y $3$ está entre $g(0)$ y $g(1)$, por TVI existe
$c \in (0, 1)$ con $g(c) = 3$. $\blacksquare$

#### Contraejemplo — por qué importa la continuidad

$f(x) = \dfrac{1}{x}$: $f(-1) = -1 < 0$ y $f(1) = 1 > 0$, pero **no** existe $c$ con
$f(c) = 0$. Bolzano no aplica porque $f$ no es continua en $[-1, 1]$ ($0 \notin \operatorname{Dom}(f)$).

#### Extra — unicidad de la raíz (práctica 8, ej. 4)

Bolzano dice que **hay** una raíz; para decir que es **única** se usa el corolario de
Rolle/Lagrange: si $f'(x) \neq 0$ en todo el intervalo, $f$ es estrictamente monótona y
corta al cero una sola vez.

Ej: $f(x) = x^3 + x - 1$. $f(0) = -1 < 0$, $f(1) = 1 > 0$ ⇒ hay raíz en $(0, 1)$.
$f'(x) = 3x^2 + 1 > 0$ para todo $x$ ⇒ $f$ es creciente ⇒ la raíz es única.

### 1.3 Derivada por definición

> $f$ es **derivable en $a$** si existe y es un número real el límite
> $$f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$

- Si el límite da $\pm\infty$ o no existe ⇒ **no es derivable** en $a$.
- **Derivable ⇒ continua.** Al revés no: $|x|$ es continua en $0$ pero no derivable.
  Por eso: si $f$ **no** es continua en $a$, ya sabés que no es derivable.

**Cuándo hay que usar la definición (y no las reglas):**

- Funciones partidas en el punto de corte.
- Cuando $f(a)$ está definida "aparte" (ej: "definimos $f(0) = 2$").
- Cuando la fórmula de $f'$ no está definida en $a$ (aparece $\ln 0$, $1/0$, $\sqrt{0}$ en un denominador…).

**Receta:**

1. Escribí el cociente con $f(a + h)$ y el valor **dado** de $f(a)$.
2. Simplificá (separar en fracciones, sacar factor común $h$).
3. Calculá el límite. Herramientas típicas:
   - $\displaystyle\lim_{h \to 0} \frac{\operatorname{sen} h}{h} = 1$, $\displaystyle\lim_{h \to 0} \frac{e^h - 1}{h} = 1$, $\displaystyle\lim_{h \to 0} \frac{\ln(1 + h)}{h} = 1$
   - acotada × (algo $\to 0$) $\to 0$ (sandwich),
   - $\ln$ de algo que tiende a $0$ va a $-\infty$; $0 \cdot \infty$ se resuelve con L'Hôpital.
4. Si en partidas los laterales dan distinto ⇒ no derivable.

#### Ejemplo — derivable (sandwich)

$$f(x) = \begin{cases} x^2 \operatorname{sen}\!\left(\frac{1}{x}\right) & x \neq 0 \\ 0 & x = 0 \end{cases}$$

$$f'(0) = \lim_{h \to 0} \frac{f(h) - f(0)}{h} = \lim_{h \to 0} \frac{h^2 \operatorname{sen}(1/h) - 0}{h} = \lim_{h \to 0} h \operatorname{sen}(1/h)$$

$h \to 0$ y $\operatorname{sen}(1/h)$ está acotado entre $-1$ y $1$ ⇒ el límite es $0$.
**Derivable, $f'(0) = 0$.**

#### Ejemplo — no derivable

$$f(x) = \begin{cases} x \operatorname{sen}\!\left(\frac{1}{x}\right) & x \neq 0 \\ 0 & x = 0 \end{cases}
\qquad \frac{f(h) - f(0)}{h} = \operatorname{sen}(1/h)$$

$\operatorname{sen}(1/h)$ oscila entre $-1$ y $1$ cuando $h \to 0$: el límite **no existe**.
**No es derivable** en $0$ (aunque sí es continua).

#### Ejemplo — partida, laterales

$$f(x) = \begin{cases} x^2 & x \le 1 \\ 2x - 1 & x > 1 \end{cases}$$

Primero continuidad: $\lim_{x \to 1^-} = 1 = \lim_{x \to 1^+} = f(1)$ ✓. Ahora:

$$\lim_{h \to 0^-} \frac{(1 + h)^2 - 1}{h} = \lim_{h \to 0^-} \frac{2h + h^2}{h} = \lim_{h \to 0^-} (2 + h) = 2$$

$$\lim_{h \to 0^+} \frac{2(1 + h) - 1 - 1}{h} = \lim_{h \to 0^+} \frac{2h}{h} = 2$$

Laterales iguales ⇒ **derivable, $f'(1) = 2$**.

#### Ejemplo — hallar $a$ y $b$ para que sea derivable (práctica 7, ej. 11)

$$f(x) = \begin{cases} x^2 & x \le 1 \\ ax + b & x > 1 \end{cases}$$

Se imponen **dos condiciones** (derivable ⇒ continua):

$$\text{continuidad: } 1 = a + b \qquad \text{derivadas laterales: } 2 \cdot 1 = a$$

$$\Longrightarrow\quad a = 2,\quad b = -1$$

> Comparar las derivadas de cada tramo vale **solo si ya impusiste continuidad**.
> Si $f$ no es continua en el punto, no es derivable, aunque las "pendientes" coincidan.

---

## Ejercicio 2 — Recta tangente / normal con parámetro

**Recta tangente** al gráfico de $f$ en $(a, f(a))$:

$$y = f(a) + f'(a)\,(x - a)$$

**Recta normal** (perpendicular a la tangente), si $f'(a) \neq 0$:

$$y = f(a) - \frac{1}{f'(a)}\,(x - a)$$

(si $f'(a) = 0$, la normal es vertical: $x = a$).

**Rectas paralelas** tienen la misma pendiente; **perpendiculares**: $m_1 \cdot m_2 = -1$.

### Receta "la tangente en $x = a$ es $y = mx + n$; hallá $k$"

Que esa recta sea la tangente significa **dos cosas a la vez**:

1. **Pasa por el punto:** $f(a) = m \cdot a + n$.
2. **Tiene la pendiente:** $f'(a) = m$.

Resolvés cada ecuación en $k$ y te quedás con los $k$ que **cumplen las dos**.
Después verificá que para ese $k$ el punto $a$ esté en el dominio (ojo con $\ln$ y raíces).

#### Ejemplo

$f(x) = k^2 x + k$. Hallar $k$ para que la tangente en $x = 0$ sea $y = 4x + 2$.

- Punto: $f(0) = k$ y la recta en $x = 0$ vale $2$ ⇒ $k = 2$.
- Pendiente: $f'(x) = k^2$ ⇒ $f'(0) = k^2 = 4$ ⇒ $k = 2$ o $k = -2$.

Las dos condiciones a la vez: **solo $k = 2$**. ($k = -2$ da la pendiente correcta pero la
recta no pasa por el punto.)

#### Ejemplo — tangente de una composición sin conocer $f$ (práctica 7, ej. 25–27)

La recta tangente a $f$ en $x = 4$ es $y = 3x - 5$. Hallar la tangente a $g(x) = f(x^2)$ en $x = 2$.

De la tangente de $f$ se leen **dos datos**: $f'(4) = 3$ (pendiente) y $f(4) = 3 \cdot 4 - 5 = 7$.

Regla de la cadena:
$$g'(x) = f'(x^2) \cdot 2x$$

En $x = 2$:
$$g(2) = f(4) = 7 \qquad g'(2) = f'(4) \cdot 4 = 12$$

$$y = 7 + 12\,(x - 2)$$

### Reglas de derivación (tienen que salir sin pensar)

| $f(x)$ | $f'(x)$ |
| --- | --- |
| $x^r$ | $r\,x^{r-1}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $1/x$ |
| $\operatorname{sen} x$ | $\cos x$ |
| $\cos x$ | $-\operatorname{sen} x$ |
| $\tan x$ | $1/\cos^2 x$ |
| $\arctan x$ | $1/(1 + x^2)$ |
| $\operatorname{arcsen} x$ | $1/\sqrt{1 - x^2}$ |

- Producto: $(fg)' = f'g + fg'$
- Cociente: $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$
- Cadena: $(g \circ f)'(x) = g'(f(x)) \cdot f'(x)$ — ej: $\left(\ln(u)\right)' = \dfrac{u'}{u}$, $\left(e^{u}\right)' = e^{u}\,u'$

---

## Ejercicio 3 — Derivación implícita (y logarítmica)

### Implícita

Cuando $f$ viene dada por una **ecuación** y no por una fórmula:

1. Escribí la ecuación con $f(x)$ en lugar de $y$.
2. **Derivá los dos miembros respecto de $x$.** Cada vez que derivás algo con $f(x)$
   adentro, aparece un $f'(x)$ por la regla de la cadena:
   $\left((f(x))^n\right)' = n\,(f(x))^{n-1} f'(x)$, $\ \left(\ln f(x)\right)' = \dfrac{f'(x)}{f(x)}$.
3. Despejá $f'(x)$ en general.
4. Recién ahí reemplazá $x = x_0$ y $f(x_0)$ (dato).

#### Ejemplo

$f$ derivable cerca de $x = 1$, cumple $(f(x))^3 + x\,f(x) = 10$ y $f(1) = 2$.
(Verificación: $2^3 + 1 \cdot 2 = 10$ ✓.)

Derivo los dos miembros (el segundo término es un producto):

$$3\,(f(x))^2 f'(x) + \big(f(x) + x\,f'(x)\big) = 0$$

Despejo $f'(x)$:

$$f'(x)\,\big(3\,(f(x))^2 + x\big) = -f(x) \quad\Longrightarrow\quad f'(x) = \frac{-f(x)}{3\,(f(x))^2 + x}$$

Reemplazo $x = 1$, $f(1) = 2$:

$$f'(1) = \frac{-2}{3 \cdot 4 + 1} = -\frac{2}{13}$$

### Derivada logarítmica — para $f(x)^{g(x)}$

Si $h(x) = f(x)^{g(x)}$ con $f(x) > 0$:

$$\ln h(x) = g(x) \ln f(x) \quad\Longrightarrow\quad \frac{h'(x)}{h(x)} = \big(g(x) \ln f(x)\big)'$$

$$h'(x) = h(x) \cdot \big(g(x) \ln f(x)\big)'$$

#### Ejemplo

$h(x) = x^x$, $x > 0$: $\ln h = x \ln x$ ⇒ $\dfrac{h'}{h} = \ln x + x \cdot \dfrac{1}{x} = \ln x + 1$

$$h'(x) = x^x\,(\ln x + 1)$$

---

## Ejercicio 4 — Asíntotas y L'Hôpital

### Definiciones

| Asíntota | Condición |
| --- | --- |
| Vertical $x = a$ | $\displaystyle\lim_{x \to a^{\pm}} f(x) = \pm\infty$ (alguno de los laterales alcanza) |
| Horizontal $y = L$ | $\displaystyle\lim_{x \to +\infty} f(x) = L$ o $\displaystyle\lim_{x \to -\infty} f(x) = L$ |
| Oblicua $y = mx + b$ | $\displaystyle\lim_{x \to \pm\infty} \big(f(x) - (mx + b)\big) = 0$ |

**Dónde buscar verticales:** puntos fuera del dominio y bordes (ceros de denominadores,
donde el argumento de un $\ln$ se hace $0$).

**Procedimiento para la oblicua** (en $+\infty$; igual en $-\infty$):

$$m = \lim_{x \to +\infty} \frac{f(x)}{x} \qquad\qquad b = \lim_{x \to +\infty} \big(f(x) - mx\big)$$

Si alguno no existe o es infinito ⇒ no hay oblicua de ese lado. Si $m = 0$ es una horizontal.

#### Ejemplo — horizontal con L'Hôpital

$f(x) = x^2 e^x$ cuando $x \to -\infty$: es "$\infty \cdot 0$". Lo paso a cociente:

$$\lim_{x \to -\infty} \frac{x^2}{e^{-x}} \overset{\frac{\infty}{\infty}}{=} \lim_{x \to -\infty} \frac{2x}{-e^{-x}} \overset{\frac{\infty}{\infty}}{=} \lim_{x \to -\infty} \frac{2}{e^{-x}} = 0$$

⇒ $y = 0$ es asíntota horizontal en $-\infty$.

#### Ejemplo — oblicua de un cociente

$f(x) = \dfrac{x^2 + 1}{x - 1}$:

$$m = \lim_{x \to +\infty} \frac{x^2 + 1}{x^2 - x} = 1 \qquad
b = \lim_{x \to +\infty} \left(\frac{x^2 + 1}{x - 1} - x\right) = \lim_{x \to +\infty} \frac{x + 1}{x - 1} = 1$$

⇒ $y = x + 1$ es asíntota oblicua en $+\infty$ (y por la misma cuenta en $-\infty$).

#### Ejemplo — oblicua con cambio de variable $u = 1/x$

$f(x) = x^2 \operatorname{sen}\!\left(\frac{1}{x}\right)$ en $+\infty$. Con $u = \frac{1}{x}$ ($u \to 0^+$):

$$m = \lim_{x \to +\infty} x \operatorname{sen}\!\left(\tfrac{1}{x}\right) = \lim_{u \to 0^+} \frac{\operatorname{sen} u}{u} = 1$$

$$b = \lim_{x \to +\infty} \left(x^2 \operatorname{sen}\!\left(\tfrac{1}{x}\right) - x\right) = \lim_{u \to 0^+} \frac{\operatorname{sen} u - u}{u^2} \overset{\frac{0}{0}}{=} \lim_{u \to 0^+} \frac{\cos u - 1}{2u} = 0$$

⇒ $y = x$ es asíntota oblicua en $+\infty$.

> Truco: con $\operatorname{sen}$ o $\cos$ de algo que va a $0$ cuando $x \to \infty$, el
> cambio $u = 1/x$ casi siempre lleva a un límite notable. Repasá también las identidades
> de suma de ángulos ($\operatorname{sen}(\alpha + \beta)$) por si el argumento viene "corrido".

### Regla de L'Hôpital

> Si $\displaystyle\lim \frac{f(x)}{g(x)}$ es $\frac{0}{0}$ o $\frac{\infty}{\infty}$, y existe
> (o es $\pm\infty$) $\displaystyle\lim \frac{f'(x)}{g'(x)}$, entonces los dos límites coinciden.
> Vale para $x \to a$, $a^{\pm}$ y $\pm\infty$.

Se deriva **numerador y denominador por separado** (no es la regla del cociente).

**Otras indeterminaciones — se llevan a $\frac{0}{0}$ o $\frac{\infty}{\infty}$:**

| Forma | Qué hacer |
| --- | --- |
| $0 \cdot \infty$ | $f \cdot g = \dfrac{f}{1/g}$ (bajar al denominador el que sea más fácil de derivar; en general **no** el $\ln$) |
| $\infty - \infty$ | Sacar común denominador o factor común |
| $0^0$, $1^\infty$, $\infty^0$ | $f^g = e^{\,g \ln f}$ ⇒ calcular $\lim g \ln f$ y después exponenciar |

#### Ejemplos

$$\lim_{x \to 0^+} x \ln x = \lim_{x \to 0^+} \frac{\ln x}{1/x} \overset{\frac{\infty}{\infty}}{=} \lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$$

$$\lim_{x \to 0^+} x^x = \lim_{x \to 0^+} e^{x \ln x} = e^0 = 1 \qquad (0^0)$$

$$\lim_{x \to +\infty} \left(1 + \frac{2}{x}\right)^x : \quad
\lim_{x \to +\infty} x \ln\!\left(1 + \frac{2}{x}\right) = \lim_{x \to +\infty} \frac{\ln(1 + 2/x)}{1/x} \overset{\frac{0}{0}}{=} \lim_{x \to +\infty} \frac{2}{1 + 2/x} = 2
\ \Longrightarrow\ \text{el límite es } e^2$$

#### Cuándo NO sirve (práctica 8, ej. 7–8)

$\displaystyle\lim_{x \to +\infty} \frac{x + \operatorname{sen} x}{x}$: L'Hôpital da $\displaystyle\lim (1 + \cos x)$, que **no existe**.
Pero eso no prueba nada: dividiendo, $1 + \frac{\operatorname{sen} x}{x} \to 1$.
**Si el límite de las derivadas no existe, L'Hôpital no concluye nada** — hay que hacerlo de otra forma.
Y siempre chequeá que sea $\frac{0}{0}$ o $\frac{\infty}{\infty}$ antes de aplicarlo.

---

## Ejercicio 5 — Estudio de función con $f'$ y $f''$ dadas

### Teoría

| Si en un intervalo… | entonces $f$ es… |
| --- | --- |
| $f' > 0$ | creciente |
| $f' < 0$ | decreciente |
| $f'' > 0$ | cóncava hacia arriba ($\cup$) |
| $f'' < 0$ | cóncava hacia abajo ($\cap$) |

- **Extremo local en $a$:** $f$ continua en $a$ y $f'$ **cambia de signo** en $a$
  ($+ \to -$: máximo; $- \to +$: mínimo). Que $f'(a) = 0$ **no alcanza** (ej: $x^3$ en $0$).
- **Punto de inflexión en $a$:** $f$ continua en $a$ y $f''$ **cambia de signo** en $a$.
- **Candidatos:** ceros de $f'$ (o $f''$), puntos donde no existe la derivada, y
  puntos donde $f$ no es continua (estos se ponen en la tabla pero no son extremos/inflexión).

### Receta

1. Factorizá $f'$ y $f''$. **Mirá qué factores son siempre positivos** (ej: $(x^2 + 9)^{3/2}$, $e^x$)
   y descartalos: el signo lo deciden los demás.
2. Ceros de los factores que quedan ⇒ marcan los intervalos.
3. Tabla de signos (un valor de prueba por intervalo).
4. Concluí con palabras: "crece en …, decrece en …, máximo local en $x = …$ de valor $f(…)$".
5. Gráfico: puntos dados, extremos, inflexiones, asíntotas, y que respete crecimiento + concavidad.
6. **Imagen:** juntá los valores de los extremos y los límites en $\pm\infty$ (o en los
   bordes). Si $f$ es continua en $\mathbb{R}$, por TVI toma todos los valores intermedios.
   Ojo: un valor de una asíntota horizontal **puede no alcanzarse** (paréntesis, no corchete).

### Ejemplo completo

$$f'(x) = \frac{1 - x^2}{(x^2 + 1)^2} \qquad f''(x) = \frac{2x\,(x^2 - 3)}{(x^2 + 1)^3}$$

con $\lim_{x \to \pm\infty} f(x) = 0$, $f(-1) = -\tfrac{1}{2}$, $f(1) = \tfrac{1}{2}$, $f(0) = 0$.
(Es $f(x) = \frac{x}{x^2 + 1}$.)

**Crecimiento.** El denominador es siempre $> 0$ ⇒ el signo es el de $1 - x^2$, que se anula en $x = \pm 1$.

| Intervalo | $(-\infty, -1)$ | $(-1, 1)$ | $(1, +\infty)$ |
| --- | --- | --- | --- |
| signo de $f'$ | $-$ | $+$ | $-$ |
| $f$ | decrece | crece | decrece |

Mínimo local en $x = -1$ (valor $-\frac{1}{2}$), máximo local en $x = 1$ (valor $\frac{1}{2}$).

**Concavidad.** El denominador es $> 0$ ⇒ el signo es el de $2x(x^2 - 3)$, ceros en $x = -\sqrt{3},\ 0,\ \sqrt{3}$.

| Intervalo | $(-\infty, -\sqrt{3})$ | $(-\sqrt{3}, 0)$ | $(0, \sqrt{3})$ | $(\sqrt{3}, +\infty)$ |
| --- | --- | --- | --- | --- |
| signo de $x$ | $-$ | $-$ | $+$ | $+$ |
| signo de $x^2 - 3$ | $+$ | $-$ | $-$ | $+$ |
| signo de $f''$ | $-$ | $+$ | $-$ | $+$ |
| $f$ | $\cap$ | $\cup$ | $\cap$ | $\cup$ |

Puntos de inflexión en $x = -\sqrt{3},\ 0,\ \sqrt{3}$.

**Imagen.** $f$ es continua en $\mathbb{R}$, tiende a $0$ en $\pm\infty$, y sus extremos
locales valen $-\frac{1}{2}$ y $\frac{1}{2}$. Como $0$ está entre esos valores, el
máximo y el mínimo locales son **globales**, y por TVI $f$ toma todo lo del medio:

$$\operatorname{Im}(f) = \left[-\tfrac{1}{2},\ \tfrac{1}{2}\right]$$

---

## Ejercicio 6 — Optimización en intervalo cerrado

### Teoría

> **Weierstrass:** si $f$ es continua en $[a, b]$, alcanza un máximo y un mínimo absolutos en $[a, b]$.

Los candidatos son:
1. los puntos críticos **dentro** de $(a, b)$ ($f' = 0$ o $f'$ no existe),
2. **los extremos $a$ y $b$** — el paso que más se olvida.

Se evalúa $f$ en todos y se comparan los valores.

### Receta

1. Dibujo y nombre de variables.
2. Escribí la **función a optimizar** (costo, área, distancia…) con todas las variables.
3. Usá la **restricción** del enunciado para dejarla en **una sola variable**.
4. **Dominio:** de dónde a dónde puede moverse esa variable (por la geometría o por el enunciado) ⇒ $[a, b]$.
5. Derivá, buscá puntos críticos, **descartá los que caen fuera de $[a, b]$**.
6. Tabla: $f(a)$, $f(\text{críticos})$, $f(b)$. Elegí.
7. Respondé **lo que pide el enunciado** (el punto, las dimensiones, el costo…), con unidades.

**Distancias:** si un tramo es la diagonal de un rectángulo de lados $d$ y $x$, su largo
es $\sqrt{d^2 + x^2}$ (Pitágoras). Derivada útil:
$\left(\sqrt{d^2 + x^2}\right)' = \dfrac{x}{\sqrt{d^2 + x^2}}$.

### Ejemplo — el extremo del intervalo gana

Se quiere cercar un terreno rectangular de $800\ \text{m}^2$ junto a un río (el lado del
río no se cerca). Por un reglamento, el lado perpendicular al río debe medir entre $25$ y $40$ m.
¿Qué dimensiones minimizan el alambre?

- Variables: $x$ = lado perpendicular al río, $y$ = lado paralelo.
- A minimizar: $L = 2x + y$.
- Restricción: $x\,y = 800$ ⇒ $y = \dfrac{800}{x}$ ⇒ $L(x) = 2x + \dfrac{800}{x}$.
- Dominio: $x \in [25, 40]$.
- Derivada: $L'(x) = 2 - \dfrac{800}{x^2} = 0 \iff x^2 = 400 \iff x = 20$.

$x = 20 \notin [25, 40]$ ⇒ **se descarta**. En $[25, 40]$, $L'(x) > 0$ (porque $x^2 > 400$), así que $L$ crece:

| $x$ | $25$ | $40$ |
| --- | --- | --- |
| $L(x)$ | $50 + 32 = 82$ | $80 + 20 = 100$ |

Mínimo en $x = 25$ m, $y = 800/25 = 32$ m, con $82$ m de alambre.
(Sin la restricción habría dado $x = 20$: por eso hay que mirar el intervalo.)

---

## Errores que cuestan puntos

- **Bolzano sin decir "continua en $[a, b]$"**, o con un intervalo que contiene un punto fuera del dominio.
- **Derivar con reglas en el punto de corte** de una partida o donde $f(a)$ está definida aparte. Va por definición.
- Concluir "es derivable" solo porque las pendientes de los tramos coinciden, **sin chequear continuidad**.
- Tangente con parámetro: usar **solo la pendiente** (o solo el punto). Son dos condiciones.
- Implícita: olvidar el $f'(x)$ de la regla de la cadena, o reemplazar los números antes de derivar.
- L'Hôpital sobre algo que **no** es $\frac{0}{0}$ ni $\frac{\infty}{\infty}$; o aplicar la regla del cociente.
- Decir "máximo en $a$" porque $f'(a) = 0$, sin mostrar el **cambio de signo**.
- Imagen: poner corchete en el valor de una asíntota que no se alcanza.
- Optimización: no evaluar los bordes del intervalo, o no responder lo que se preguntó.
- **"JUSTIFICÁ TODAS LAS RESPUESTAS"**: cada conclusión necesita el teorema o la cuenta que la respalda, dicho con palabras.
