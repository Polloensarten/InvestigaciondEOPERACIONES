import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Firewall_Seguridad", pulp.LpMaximize)

# 2. Definir Variables (GB procesados por cada tipo de inspección)
x1 = pulp.LpVariable("Inspeccion_Basica", cat='Integer')
x2 = pulp.LpVariable("Inspeccion_Profunda", cat='Integer')

# 3. Función Objetivo (Maximizar puntos de mitigación de riesgo)
model += 2 * x1 + 5 * x2, "Puntos_Seguridad_Total"

# 4. Restricciones
model += 1 * x1 + 3 * x2 <= 18, "CPU_Firewall"
model += 1 * x1 + 1 * x2 <= 8,  "RAM_Buffer"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"GB con Inspección Básica:   {int(x1.varValue)}")
print(f"GB con Inspección Profunda: {int(x2.varValue)}")
print(f"Puntos de Seguridad Máximos: {pulp.value(model.objective):.0f} puntos")