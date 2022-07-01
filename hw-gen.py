from manim import *
from sympy.solvers import solve
from sympy import Symbol, latex, sympify
import random
from math import sqrt

class Equation:
    def __init__(self, equation: tuple, solutions: tuple):
        self.equation = equation
        self.solutions = solutions

def generate_random_equation():
    x = Symbol('x')
    a = random.randrange(-100, 100)
    b = random.randrange(-100, 100)
    c = random.randrange(-100, 100)

    equation = (a*x*x + b*x + c, 0)

    equation = Equation(equation, solve(equation))
    return equation


class EqScene(Scene):
    def construct(self):
        equation = generate_random_equation()
        #Ecuacion: (40*x**2 + 41*x + 48, 0)
        #Solucion: \[\{x: -41/80 - sqrt(5999)*I/80\}, \{x: -41/80 + sqrt(5999)*I/80\}\]
        # Sustituir a/b por \frac{a}{b}


        eq_py   = str(equation.equation)
        sol_py  = str(equation.solutions)
        x = Symbol('x')
        print(sol_py)
        eq_text = latex(sympify(eq_py))
        sol_text = latex(sympify(sol_py))
        eq_tex  = MathTex(r'{}'.format(eq_text))
        sol_tex = MathTex(r'{}'.format(sol_text))

        eq_tex.shift(UP)
        sol_tex.shift(DOWN)
        self.add(eq_tex, sol_tex)
