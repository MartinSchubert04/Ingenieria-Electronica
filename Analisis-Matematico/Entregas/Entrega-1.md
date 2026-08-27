1.

Voy a utilizar las siguientes variables

a = longitud vertiacal del rectangulo
b = longitud horizontal del rectangulo
d = diametro de la circunferencia
r = radio de la circunferencia
P = perimetro
C = circunferencia

Ahora sabiendo que la relacion del perimetro y el diametro es $\pi$, para hallar el perimetro de un circulo y un cuadrado planteo lo siguiente

Circulo:  
$C = d*\pi = 2{\pi}r$

Rectangulo:  
$P = 2a + 2b$

Al ser un semicirculo para que coincida con los laterales verticales del rectangulo entonces requiere que

$b = d = 2r$

Perimetro de la ventana:

$P = P_{rectangulo} - b + \frac{C_{circulo}}{2}$  
$P = 2a + 2b - b + \frac{b\pi}{2}$  
$P = 2a + b + \frac{b\pi}{2}$

Se le resta a porque solo se suman los cuatros lados rectos y para el lado que seria una semiesfera se calcula con la formula de C y se divide por dos ya que es la mitad del circulo

2.

Las condiciones que exige son las siguientes:

$b > 0$
$a > 0$

3.

La altura total de nuestra ventana la llamare h y se describe asi

$h = a + r$

Y queremo que nuestra ventana este dentro por encima de 100cm y por debajo 250cm, entonces la ventana debe entrar en 150cm de altura

$h \le 150cm$

4.

Sabiendo que el perimetro final de la ventana es  
$P = 350cm$

Planteo la formula del perimetro y despejo a en funcion de b, lo que me permite saber el $a$ para cualquier $b$

$P = 2a + b + \frac{b\pi}{2}$  
$350cm = 2a + b + \frac{b\pi}{2}$  
$a = \frac{350cm - b - \frac{b\pi}{2}}{2}$

5.

Planteo lo mismo que en el 4 pero despejo $b$ esta vez en funcion de $a$

$P = 2a + b + \frac{b\pi}{2}$  
$b = P - 2a - \frac{b\pi}{2}$  
$b + \frac{b\pi}{2}= P - 2a$  
$b(2+\pi) = 2P - 4a$  
$b = \frac{2P - 4a}{2+\pi}$  
$b = \frac{2*350cm - 4a}{2+\pi}$

6.

Reemplazo las condiciones previas por la formula en funcion de b

$a > 0$  
$\frac{P - b - \frac{b\pi}{2}}{2} > 0$  
$P - b - \frac{b\pi}{2} > 0$  
$- \frac{2b + b\pi}{2} > -P$  
$- \frac{b(2 + \pi)}{2} > -P$  
$b(2 + \pi) < P*2$  
$b < \frac{2P}{2 + \pi}$

Ahora lo mismo para la restriccion de altura

$h \le 150cm$  
$a + r \le 150cm$  
$a + \frac{b}{2} \le 150cm$  
$\frac{P - b - \frac{b\pi}{2}}{2} + \frac{b}{2} \le 150cm$  
$\frac{P - b - \frac{b\pi}{2}  + b}{2} \le 150cm$  
$P - \frac{b\pi}{2} \le 2*150cm$  
$\frac{2P - b\pi}{2} \le 300cm$  
$2P - b\pi \le 300cm * 2$  
$b \ge \frac{2P -600cm}{\pi}$
