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

        equation_py  = str(equation.equation)
        solution_py  = str(equation.solutions)

        x = Symbol('x')
        equation_text = latex(sympify(equation_py))
        solution_text = latex(sympify(solution_py))
        equation_tex  = MathTex(r'{}'.format(equation_text))
        solution_tex = MathTex(r'{}'.format(solution_text))

        equation_tex.shift(UP)
        solution_tex.shift(DOWN)
        self.add(equation_tex, solution_tex)
