import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Backend",cat='Integer')
x2 = pulp.LpVariable("Dataworker",cat='Integer')

# 3. Función Objetivo
model += 300 * x1 + 250 * x2, "Costo_Total"

# 4. Restricciones
model += 2 * x1 + 1 * x2 <= 16, "RAM"
model += 1 * x1 + 2 * x2 <= 17, "SSD"
model += x1 <= 6, "Red"
model += x2 <= 7, "Licencias"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"contenedor backend: {x1.varValue}")
print(f"contenedor data worker: {x2.varValue}")
print(f"Valor de Rendimiento Máximo: ${pulp.value(model.objective):.0f} USD/hora")  


#source .venv/bin/activate