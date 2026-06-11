import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Ensamble_Computadoras", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes ensamblar media computadora)
x1 = pulp.LpVariable("Escritorio", cat='Integer')
x2 = pulp.LpVariable("Laptop", cat='Integer')

# 3. Función Objetivo
model += 2000 * x1 + 4000 * x2, "Ganancia_Total"

# 4. Restricciones
model += 1 * x1 + 1 * x2 <= 60, "Microprocesadores"
model += 1 * x1 + 3 * x2 <= 100, "Horas_Trabajo"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Computadoras de Escritorio: {int(x1.varValue)}")
print(f"Laptops: {int(x2.varValue)}")
print(f"Ganancia Máxima: ${pulp.value(model.objective):,.0f} MXN")