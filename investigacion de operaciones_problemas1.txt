import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Escritorio", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Laptops", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 2000 * x1 + 4000 * x2, "Costo_Total"

# 4. Restricciones
model += 1 * x1 + 1 * x2 <= 60, "Microproceesadores"
model += 1 * x1 + 3 * x2 <= 100, "Horas de Trabajo"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Contratar Tipo A: {x1.varValue}")
print(f"Contratar Tipo B: {x2.varValue}")
print(f"Costo Mínimo Diario: ${pulp.value(model.objective)}")

#source .venv/bin/activate