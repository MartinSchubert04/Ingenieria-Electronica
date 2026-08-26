# Formulario de Análisis I

Definiciones, propiedades y fórmulas de las **prácticas 1, 2, 3 y 5** (funciones, función módulo, exponencial-logaritmo y límites). No reemplaza la práctica de ejercicios ni las definiciones dadas en clase.

---

## Práctica 1 — Funciones

**Función, dominio y codominio.** *f : A → B* asigna a cada *a ∈ A* exactamente un *f(a) ∈ B*. *A* es el dominio, *B* el codominio.

> Dom(f) = { x ∈ ℝ : es posible calcular f(x) } — dominio natural de una fórmula

**Imagen y conjuntos de signo**
- Im(f) = { f(a) : a ∈ A }
- C₀(f) = { a : f(a) = 0 } — ceros
- C₊(f) = { a : f(a) > 0 }
- C₋(f) = { a : f(a) < 0 }

**Gráfico y composición**
- Gráfico de f: { (a, f(a)) : a ∈ A }
- (g ∘ f)(a) = g(f(a))
- Dom(g∘f) = { x ∈ Dom(f) : f(x) ∈ Dom(g) }

**Transformaciones del gráfico**

Traslaciones (c > 0):

| Expresión | Efecto |
|---|---|
| f(x) + c | sube c |
| f(x) − c | baja c |
| f(x − c) | corre a la derecha c |
| f(x + c) | corre a la izquierda c |

Escalados y reflexiones (c > 1):

| Expresión | Efecto |
|---|---|
| c·f(x) | estira verticalmente ×c |
| (1/c)·f(x) | comprime verticalmente ×c |
| f(cx) | comprime horizontalmente ×c |
| f(x/c) | estira horizontalmente ×c |
| −f(x) | refleja respecto al eje x |
| f(−x) | refleja respecto al eje y |

**Monotonía**
- Creciente en I: x₁ < x₂ ⇒ f(x₁) < f(x₂)
- Decreciente en I: x₁ < x₂ ⇒ f(x₁) > f(x₂)

**Inyectiva · suryectiva · biyectiva**
- Inyectiva: x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂)
- Suryectiva: Im(f) = B
- Biyectiva: inyectiva y suryectiva

**Función inversa**
> f⁻¹(b) = a ⇔ f(a) = b
> f⁻¹∘f(a) = a para todo a ∈ A · f∘f⁻¹(b) = b para todo b ∈ B

**Raíz de un polinomio**
> p(a) = 0 ⇔ p(x) = (x − a)·q(x), con q polinómica

**Trigonométricas**
- sen, cos: periódicas de período 2π; Im = [−1, 1]
- tan(x) = sen(x)/cos(x); Dom = { x ≠ π/2 + kπ }; Im = ℝ; período π

**Inversas trigonométricas**

| Función | Dominio | Imagen |
|---|---|---|
| arcsen | [−1, 1] | [−π/2, π/2] |
| arccos | [−1, 1] | [0, π] |
| arctan | ℝ | (−π/2, π/2) |

---

## Práctica 2 — Función módulo

**Dos definiciones equivalentes**
> \|x\| = √(x²)
> \|x\| = −x si x < 0 ; \|x\| = x si x ≥ 0

**Dominio, imagen y monotonía**
- Dom(\|x\|) = ℝ · Im(\|x\|) = [0, +∞)
- Creciente en [0, +∞); decreciente en (−∞, 0]

**Módulo como distancia.** \|x\| es la distancia de x al origen.
> d(x₁, x₂) = \|x₂ − x₁\| = \|x₁ − x₂\|

**Composición con el módulo**
- **\|f(x)\|**: la parte del gráfico bajo el eje x se refleja hacia arriba; el resto queda igual.
- **f(\|x\|)**: se conserva la parte del gráfico a la derecha del eje y y se refleja sobre la izquierda (se descarta lo que había a la izquierda).

**Álgebra del módulo**
- \|x\| = \|−x\|
- \|x₁·x₂\| = \|x₁\|·\|x₂\|
- \|x₁/x₂\| = \|x₁\|/\|x₂\| (x₂ ≠ 0)
- \|xⁿ\| = \|x\|ⁿ

**Ecuaciones e inecuaciones con módulo**

| Caso | M > 0 | M = 0 | M < 0 |
|---|---|---|---|
| \|x\| = M | x = ±M | x = 0 | sin solución |
| \|x\| < M | (−M, M) | sin solución | sin solución |
| \|x\| > M | (−∞,−M) ∪ (M,+∞) | ℝ ∖ {0} | ℝ (todo) |

**Raíces de índice par y monomios**
> ⁿ√(xⁿ) = \|x\| si n es par

| Ecuación / inecuación | n impar | n par (k ≥ 0) |
|---|---|---|
| xⁿ = k | x = ⁿ√k | x = ±ⁿ√k |
| xⁿ > k | x > ⁿ√k | \|x\| > ⁿ√k |

> **Ejemplo.** Resolver \|x² + x\| < 6. Por la propiedad de \|x\| < M equivale a −6 < x²+x < 6 simultáneamente. Resolviendo ambas desigualdades e intersecando, la solución es (−3, 2).

---

## Práctica 3 — Exponencial y logaritmo

**Función exponencial aˣ.** Para a > 0, a ≠ 1: f(x) = aˣ es biyectiva, Dom = ℝ, Im = (0, +∞).
- a > 1 → creciente
- 0 < a < 1 → decreciente

**Leyes de la exponenciación**

| | |
|---|---|
| a^(z+w) | = aᶻ·aʷ |
| a^(z−w) | = aᶻ/aʷ |
| (aᶻ)ʷ | = a^(zw) |
| (ab)ᶻ | = aᶻ·bᶻ |

**Equivalencias (exponencial)**
- aᶻ = aʷ ⇔ z = w
- a > 1: aᶻ < aʷ ⇔ z < w
- 0 < a < 1: aᶻ < aʷ ⇔ z > w (se invierte)

**Logaritmo, como inversa de aˣ**
> log_a(w) = z ⇔ aᶻ = w

**Función log_a(x).** Biyectiva, Dom = (0, +∞), Im = ℝ. Creciente si a > 1; decreciente si 0 < a < 1.
> log_a(aˣ) = x · a^(log_a x) = x

**Álgebra del logaritmo**
- log_a(xy) = log_a(x) + log_a(y)
- log_a(x/y) = log_a(x) − log_a(y)
- log_a(xʳ) = r·log_a(x)
- log_b(x) = log_a(x) / log_a(b) — cambio de base

**Equivalencias (logaritmo)**
- a > 1: log_a(z) < log_a(w) ⇔ z < w
- 0 < a < 1: log_a(z) < log_a(w) ⇔ z > w

**Exponencial por dos puntos.** Dados (x₁,y₁), (x₂,y₂) con x₁≠x₂ e y₁,y₂ > 0, existen únicos a,k > 0 tales que
> f(x) = k·aˣ

> **Ejemplo.** Resolver (2/3)^(5x−3) < 9/4. Se escribe 9/4 = (2/3)⁻². Como 0 < 2/3 < 1, la desigualdad se invierte al comparar exponentes: 5x−3 > −2, de donde x > −1/5.

---

## Práctica 5 — Límites

**Límite puntual finito.** "Cerca de a" = en un entorno reducido de a.
> lim (x→a) f(x) = L

**Límites laterales.** El límite existe y vale L ⇔ ambos laterales (x→a⁻ y x→a⁺) existen y valen L.

**Álgebra de límites finitos.** Si lim(x→a) f y lim(x→a) g existen y c es constante:
- lim(f+g) = lim f + lim g
- lim(cf) = c·lim f
- lim(fg) = lim f · lim g
- lim(f/g) = lim f / lim g, si lim g ≠ 0

**Límite de potencia fᵍ.** Si f > 0 cerca de a, lim f = L > 0, lim g = K:
> lim (x→a) f(x)^g(x) = Lᴷ

**Continuidad en un punto**
> lim (x→a) f(x) = f(a)

Exige: a ∈ Dom(f), que el límite exista, y que coincida con f(a). Continuidad lateral: idem con el límite lateral correspondiente.

**Funciones continuas "de fábrica".** Son continuas en todo su dominio: polinomiales, racionales, raíz ⁿ√x, trigonométricas y sus inversas, exponenciales, logarítmicas, y toda suma, resta, producto o cociente de éstas. Si a ∈ Dom(f): lim(x→a) f(x) = f(a) (sustitución directa).

**Continuidad y composición.** Si g es continua en b y lim(x→a) f(x) = b:
> lim (x→a) g(f(x)) = g( lim f(x) )

**Técnica para 0/0 — sustitución.** Si f(x) = g(x) para todo x cerca de a (salvo quizá en a), entonces lim f existe ⇔ lim g existe, y son iguales. Se usa factorizando y simplificando el factor que anula numerador y denominador.

**Límite infinito y asíntotas verticales.** lim f(x) = +∞ / −∞ / ∞ (sin signo determinado). x = a es asíntota vertical si algún límite lateral (o el bilátero) en a es ±∞.
> Si f ≠ 0 cerca de a: lim(x→a) f(x) = 0 ⇔ lim(x→a) 1/f(x) = ∞

**Álgebra de límites infinitos.** Con lim f = +∞, lim g = +∞, lim h = L (cerca de a):

| | | | |
|---|---|---|---|
| lim(f+g) | +∞ | lim(h·f), L = 0 | indeterminado |
| lim(f+h) | +∞ | lim h/f | 0 |
| lim(f−g) | indeterminado | lim g/f | indeterminado |
| lim(fg) | +∞ | lim(h·f), L ≠ 0 | sg(L)·∞ |

**Comparación, sandwich y cero por acotada**
- **Comparación:** f ≤ g cerca de a, ambos límites existen ⇒ lim f ≤ lim g
- **Sandwich:** f ≤ g ≤ h, lim f = lim h = L ⇒ lim g = L
- **Divergencia:** f ≤ g, lim f = +∞ ⇒ lim g = +∞
- **Cero por acotada:** f acotada cerca de a, lim g = 0 ⇒ lim(fg) = 0

**Límite en el infinito**
> lim (x→+∞) f(x) = L

y = L es asíntota horizontal si vale para x→+∞ o x→−∞.

**Monomios y polinomios en ∞**
- lim(x→+∞) xⁿ = +∞
- lim(x→−∞) xⁿ = (−1)ⁿ·∞
- lim p(x) = signo(coef. ppal.) · (±1)^gr(p) · ∞

**Racionales p(x)/q(x) en ∞ (según grados)**

| Comparación de grados | lim (x→+∞) |
|---|---|
| gr(p) = gr(q) | coef. ppal. p / coef. ppal. q |
| gr(p) < gr(q) | 0 |
| gr(p) > gr(q) | [sg(coef p)/sg(coef q)] · ∞ |

Para x→−∞ los dos primeros casos no cambian; en el tercero se multiplica cada signo por (−1)^grado correspondiente antes de comparar.

**Raíces, exponenciales y logaritmos en ∞**
- lim(x→+∞) ⁿ√x = +∞; lim(x→−∞) ⁿ√x = −∞ (n impar)
- a > 1: aˣ → 0 (x→−∞), → +∞ (x→+∞)
- 0 < a < 1: aˣ → +∞ (x→−∞), → 0 (x→+∞)
- a > 1: log_a(x) → +∞ (x→+∞); 0 < a < 1: log_a(x) → −∞ (x→+∞)

**Composición de límites**
- lim(x→a) f = L, f ≠ L cerca de a, lim(y→L) g = K ⇒ lim(x→a) g∘f = K
- lim(x→a) f = +∞, lim(y→+∞) g = L ⇒ lim(x→a) g∘f = L

**Límites especiales**

> Número e: lim(x→+∞) (1 + 1/x)ˣ = e = lim(x→0) (1+x)^(1/x)
> Generaliza: si f(x)→±∞, lim (1+1/f(x))^f(x) = e. Si f(x)→0 (f≠0), lim (1+f(x))^(1/f(x)) = e.

> Seno sobre x: lim(x→0) sen(x)/x = 1
> Generaliza: si f(x)→0 (f≠0) cerca de a: lim(x→a) sen(f(x))/f(x) = 1.

**Tabla de referencia — límite generalizado de potencias f(x)^g(x)**

Vale para x→□ (por izquierda, derecha, ambos lados, o a ±∞). Se pide f(x) > 0.

| lim f | lim g | lim fᵍ |
|---|---|---|
| L > 0 | K | Lᴷ |
| 0 | K > 0 | 0 |
| 0 | K < 0 | +∞ |
| 0 | 0 | indeterminado |
| L > 1 | +∞ | +∞ |
| L > 1 | −∞ | 0 |
| 0 < L < 1 | +∞ | 0 |
| 0 < L < 1 | −∞ | +∞ |
| 1 | +∞ | indeterminado |
| 1 | −∞ | indeterminado |
| 0 | +∞ | 0 |
| 0 | −∞ | +∞ |
| +∞ | K > 0 | +∞ |
| +∞ | K < 0 | 0 |
| +∞ | 0 | indeterminado |
| +∞ | +∞ | +∞ |
| +∞ | −∞ | 0 |

**Discontinuidades.** a es discontinuidad de f si f no es continua en a (incluye bordes de Dom(f) que no pertenecen a él).
- **Evitable:** lim(x→a) f(x) es un número real.
- **No evitable:** en cualquier otro caso.
