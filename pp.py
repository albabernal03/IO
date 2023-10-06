# Importar OR-Tools y crear el solver
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Crear las variables
estudiar = solver.NumVar(0, solver.infinity(), 'estudiar')
divertirse = solver.NumVar(0, solver.infinity(), 'divertirse')

# Crear las restricciones
solver.Add(estudiar + divertirse <= 10)
solver.Add(divertirse <= 4)
solver.Add(estudiar - divertirse <= 1)

# Crear la función objetivo
solver.Maximize(estudiar + divertirse)

# Resolver el problema
status = solver.Solve()

# Imprimir la solución
if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    print('estudiar =', estudiar.solution_value())
    print('divertirse =', divertirse.solution_value())
else:
    print('The problem does not have an optimal solution.')
