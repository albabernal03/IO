# Import OR-Tools wrapper for linear programming
from ortools.linear_solver import pywraplp
# Create a solver using the GLOP backend
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)


#creamos las variables 
estudiar=solver.NumVar(0,solver.infinity(),'estudiar')
divertirse=solver.NumVar(0,solver.infinity(),'divertirse')

#creamos las restricciones
solver.Add(estudiar+divertirse<=10)
solver.Add(divertirse<=4)
solver.Add(estudiar-divertirse<=1)

#creamos la funcion objetivo
solver.Maximize(estudiar+divertirse)

#resolvemos el problema
status = solver.Solve()

#imprimimos la solucion
if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    print('estudiar =', estudiar.solution_value())
    print('divertirse =', divertirse.solution_value())
else:
    print('The problem does not have an optimal solution.')

