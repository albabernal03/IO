import sympy as sym
from sympy import symbols
from sympy.plotting import plot

f1 = "10-x"  # <=
f2 = "x-1"   # >=
f3 = "4"     # <=
Z1 = "(16-x)"
Z2 = "(14-x)"
Z3 = "(13-x)"
x = symbols('x')

# Crear el gráfico con las restricciones y la función objetivo
p = plot(f1, f2, f3, Z1, Z2, Z3, (x, 0, 15), show=False)

# Agregar una línea para la solución óptima
p.extend(sym.plot(10 - x, (x, 1, 10), line_color='black', show=False)) # Aqui se muestra la solucion optima porque 

# Etiquetar la solución óptima
p[6].line_label = 'Solución Óptima' 

# Mostrar el gráfico con las líneas adicionales
p.show()



