# Importar el módulo SymPy
import sympy as sym 
from sympy import symbols 
from sympy.plotting import plot

f1 = "5+0*x"
f2 = "8-2*x"
f3 ='(10-4*x)/5'
x = symbols('x') 
plot(f1, f2,f3, (x, 0, 5))