## 1. Función área

Dom = (0,2)

$Dom = (0,\pi/2]$

Llamo al "techo" o lado superior del trapezio $S$ y a la base $B$, y como los otros dos lados tienen mismo angulo y misma longitudo podemos decir que es un trapecio isosceles, llamo a cada lado $L_0$ (izquierdo) y $L_1$ (derecho) aunque realmente se podria decir que son igual y tratar de la misma forma, solo varia la orientacion

$L_1 = 10$  
$L_0 = 10$

Para cada lado no paralelo puedo hallar el cateto que conforma una parte de $S$ (lo llamo cateto $a$) siendo que estos forman una hipotenusa con el mismo y un cateto $b$ en el punto que cualquier de los $L$ toca $B$

Los llamo L ya que son iguales

Por pitagoras se sabe que:

$\operatorname{sen}\alpha = \frac
{b}{L}$

con L = 10  
$b= 10 \operatorname{sen}\alpha$

el otro cateto

$\cos\alpha = \frac{a}{L}$

$a= 10\cos\alpha$

$A(\alpha) = B \cdot b + a \cdot b = 10 \cdot 10\operatorname{sen}\alpha + 10\cos\alpha \cdot 10\operatorname{sen}\alpha$

$A(\alpha) = 100(\operatorname{sen}\alpha + \cos\alpha \cdot \operatorname{sen}\alpha)$

## 2. Máximo

### Derivada

$$A(\alpha) = 100(\operatorname{sen}\alpha + \operatorname{sen}\alpha\cos\alpha)$$

Usando la regla del producto en $\operatorname{sen}\alpha\cos\alpha$:

$$A'(\alpha) = 100\left(\cos\alpha + \cos\alpha \cdot \cos\alpha + \operatorname{sen}\alpha \cdot (-\operatorname{sen}\alpha)\right)$$

$$A'(\alpha) = 100\left(\cos\alpha + \cos^2\alpha - \operatorname{sen}^2\alpha\right)$$

Reemplazo $\operatorname{sen}^2\alpha = 1 - \cos^2\alpha$:

$$A'(\alpha) = 100\left(\cos\alpha + \cos^2\alpha - 1 + \cos^2\alpha\right) = 100\left(2\cos^2\alpha + \cos\alpha - 1\right)$$

Hallo los ceros de la derivada

$$2\cos^2\alpha + \cos\alpha - 1 = 0$$

Con $u = \cos\alpha$ queda $2u^2 + u - 1 = 0$:

$$u = \frac{-1 \pm \sqrt{1 + 8}}{4} = \frac{-1 \pm 3}{4}$$

- $u = \frac{1}{2} \Rightarrow \cos\alpha = \frac{1}{2} \Rightarrow \alpha = \frac{\pi}{3}$ ✔ (está en el dominio)
- $u = -1 \Rightarrow \cos\alpha = -1 \Rightarrow \alpha = \pi$ ✘ (fuera del dominio)

Único punto crítico: $\alpha = \dfrac{\pi}{3}$

Verificación del máximo

Factorizando:

$$A'(\alpha) = 100\,(2\cos\alpha - 1)(\cos\alpha + 1)$$

En el dominio, $\cos\alpha + 1 > 0$ siempre, así que el signo de $A'$ depende solo de $2\cos\alpha - 1$:

| Intervalo        | $\cos\alpha$ | $2\cos\alpha - 1$ | $A'$ | $A$     |
| ---------------- | ------------ | ----------------- | ---- | ------- |
| $(0, \pi/3)$     | $> 1/2$      | $> 0$             | $+$  | crece   |
| $(\pi/3, \pi/2]$ | $< 1/2$      | $< 0$             | $-$  | decrece |

$A$ crece hasta $\pi/3$ y después decrece, por lo tanto en $\alpha = \pi/3$ hay un **máximo**.

### Área máxima

$$A\left(\tfrac{\pi}{3}\right) = 100 \cdot \operatorname{sen}\tfrac{\pi}{3}\left(1 + \cos\tfrac{\pi}{3}\right) = 100 \cdot \frac{\sqrt{3}}{2} \cdot \frac{3}{2} = 75\sqrt{3} \approx 129{,}9 \text{ cm}^2$$

Comparando con el extremo $\alpha = \pi/2$ (rectángulo): $A(\pi/2) = 100 \cdot 1 \cdot 1 = 100 \text{ cm}^2 < 75\sqrt{3}$ ✔

### Conclusión

El área de la sección es máxima cuando $\alpha = \dfrac{\pi}{3}$ (60°, $\approx 1{,}047$ rad), y vale $75\sqrt{3} \approx 129{,}9$ cm².
