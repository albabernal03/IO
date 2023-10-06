import sympy as sym
from sympy import symbols
from sympy.plotting import plot

#restricciones

f1='(800-x)' #color 
f2='(x-450)'
f3='(1200-2*x)'
f4='(2400-3*x)/4'

#Lo mostramos graficamente
x = symbols('x')
plot(f1, f2,f3,f4, (x, 0, 1200))
