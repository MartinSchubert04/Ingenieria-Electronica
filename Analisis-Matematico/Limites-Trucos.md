# Trucos para resolver límites (Práctica 5)

## 1. Indeterminación 0/0 (x → a finito)

**Factorizar y cancelar** — numerador y denominador se anulan en $x=a$, ambos tienen $(x-a)$ como factor. Factorizar y simplificar.

**Multiplicar por el conjugado** — cuando hay raíces que generan 0/0 (o ∞−∞). Multiplicar numerador y denominador por el conjugado para convertir la resta de raíces en diferencia de cuadrados y cancelar.

**Armar el límite notable $\lim \frac{\text{sen}(u)}{u}=1$** — multiplicar y dividir por la constante que falta para que el argumento del seno coincida con lo que divide:
$$\frac{\text{sen}(3x)}{2x} = \frac{3}{2}\cdot\frac{\text{sen}(3x)}{3x} \to \frac{3}{2}\cdot 1$$

**Derivados del límite notable de seno:**
- $\frac{\tan x}{x}\to 1$
- $\frac{1-\cos x}{x}\to 0$ (y $\frac{1-\cos x}{x^2}\to \frac12$)

## 2. Indeterminación ∞/∞ (x → ±∞, cociente de polinomios)

**Dividir todo por la mayor potencia de x** (arriba y abajo) — los términos de menor grado tienden a 0 y queda la relación entre coeficientes líderes.

**Sacar como factor común la potencia dominante** — útil cuando hay raíces con distintos grados adentro (ej. $\sqrt{4x^2+1} = x\sqrt{4+1/x^2}$).

## 3. Indeterminación ∞ − ∞

**Multiplicar y dividir por el conjugado** — convierte la resta de raíces en una fracción, después se divide por la potencia dominante.

## 4. Indeterminación $1^{\infty}$

**Usar el límite notable $\left(1+\frac1y\right)^y \to e$**, reescribiendo la base como $1+(\text{algo}\to 0)$ y ajustando el exponente para que coincida:
$$\left(1+\frac{a}{x}\right)^x = \left[\left(1+\frac{a}{x}\right)^{x/a}\right]^a \to e^a$$

## 5. Teorema del sandwich / compresión

Acotar la función entre dos que tienden al mismo límite — útil cuando aparece sen o cos de algo que no tiene límite (oscila) pero está multiplicado por algo que sí tiende a 0.
Ej: $x\cos(1/x)\to 0$ porque $-1\le\cos(1/x)\le1$.

## 6. Límites laterales por separado

Con valor absoluto, raíces con dominio restringido, o exponenciales tipo $e^{1/x}$, el comportamiento cambia según el lado — partir en $x\to a^-$ y $x\to a^+$.

## 7. Cambio de variable / sustitución

Sustituir $u=x-a$ (o $u=1/x$) para reconducir un límite a la forma de un límite notable conocido. Se combina seguido con el truco de sen(x)/x cuando el punto no es 0.

## 8. Álgebra de límites (base de todo)

Si existen los límites de las partes, el límite de suma/resta/producto/cociente/potencia/raíz es la operación entre esos límites (cuidado si el denominador o la base de una potencia da 0).

---

**Orden lógico para encarar un ejercicio:**
1. Probar sustitución directa.
2. Si da 0/0: ¿raíces? → conjugado. ¿polinomio? → factorizar. ¿sen/cos? → armar límite notable.
3. Si da ∞/∞ o ∞−∞: dividir por potencia dominante o conjugado.
4. Si da $1^\infty$: armar la forma de $e$.
5. Si hay algo acotado (sen, cos) multiplicando algo que tiende a 0 o ∞: sandwich.
6. Si hay valor absoluto o exponencial rara en un punto: laterales.
