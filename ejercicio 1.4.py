import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Edge_Computing_Node", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes instalar medio servidor)
x1 = pulp.LpVariable("Blade_Estandar", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Rack_Pro", lowBound=0, cat='Integer')

# 3. Función Objetivo (Maximizar eventos por segundo)
model += 10000 * x1 + 25000 * x2, "EPS_Total"

# 4. Restricciones
model += 1500 * x1 + 4000 * x2 <= 30000, "Presupuesto_USD"
model += 1 * x1 +    3 * x2 <= 24,     "Espacio_Rack_Bahias"
model += 2 * x1 +    5 * x2 <= 45,     "Suministro_Electrico_kW"
model += x2 >= 2,                        "SLA_Redundancia_RackPro"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Servidores Blade Estándar: {int(x1.varValue)}")
print(f"Servidores Rack Pro:       {int(x2.varValue)}")
print(f"Capacidad Máxima: {pulp.value(model.objective):,.0f} EPS")