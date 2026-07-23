from manim import *

class DerivadaVisual(Scene):
    def construct(self):
        # Ejes
        axes = Axes(x_range=[-3, 3], y_range=[-2, 10])
        
        # Función y su derivada
        funcion = axes.plot(lambda x: x**2, color=BLUE)
        derivada = axes.plot(lambda x: 2*x, color=RED)
        
        label_f = MathTex("f(x) = x^2").set_color(BLUE).to_corner(UL)
        label_d = MathTex("f'(x) = 2x").set_color(RED).to_corner(UL).shift(DOWN)
        
        self.play(Create(axes))
        self.play(Create(funcion), Write(label_f))
        self.wait(1)
        self.play(Create(derivada), Write(label_d))
        self.wait(2)