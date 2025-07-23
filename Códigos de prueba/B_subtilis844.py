import cobra
import matplotlib.pyplot as plt

# Cargar el modelo metabólico (iYO844)
model = cobra.io.read_sbml_model("C:/Users/felip/Desktop/python/TESIS/iYO844.xml")

# Optimizar el modelo usando FBA
solution = model.optimize()
print(f"Objective value: {solution.objective_value}")

# Obtener y filtrar los flujos significativos
fluxes = solution.fluxes
fluxes_filtered = fluxes[abs(fluxes) > 1e-6]  # Filtrar flujos cercanos a 0

# Graficar los flujos metabólicos principales
plt.figure(figsize=(10, 6))
fluxes.plot(kind="barh", color="orange")
plt.axvline(0, color='grey', lw=0.8)
plt.xlim(-40, 100)  # Establece los límites del eje x
plt.title("Flujos de Reacción en Bacillus subtilis")
plt.xlabel("Flujo")
plt.ylabel("Reacciones")
plt.grid(axis='x')
plt.show()