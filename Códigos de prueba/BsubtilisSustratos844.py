import cobra
from cobra.io import read_sbml_model
import matplotlib.pyplot as plt

def run_fba():
    # Cargar el modelo de la carpeta 
    model = read_sbml_model("C:/Users/felip/Desktop/python/TESIS/iYO844.xml")

    # límite inferior de todas las reacciones
    for reaction in model.reactions:
        reaction.lower_bound = -0.68
    # Prohibir importación de otros substratos además del que le voy a poner
    for reaction in model.exchanges:
        reaction.lower_bound = 0
    
    # medio mínimo
    model.reactions.get_by_id("EX_o2_LSQBKTe_RSQBKT").lower_bound = -18
    model.reactions.get_by_id("EX_succ_LSQBKTe_RSQBKT").lower_bound = -0
    model.reactions.get_by_id("EX_succ_LSQBKTe_RSQBKT").lower_bound = -8.71


    solution = model.optimize() 

 # para visualizar los flujos metabólicos
    fluxes = solution.fluxes

    #Graficar los flujos metabólicos 
    # plt.figure(figsize=(10, 6))
    # fluxes.plot(kind="barh", color="orange")
    # plt.axvline(0, color='grey', lw=0.8)
    # plt.title("Flujos de Reacción en Bacillus subtilis")
    # plt.xlabel("Flujo")
    # plt.ylabel("Reacciones")
    # plt.grid(axis='x')
    # plt.show()
    # # print(model.summary())
    
    print(f"Valor de la función objetivo (biomasa): {solution.objective_value}")
    # Detectar reacciones bloqueadas
    # blocked_reactions = cobra.flux_analysis.find_blocked_reactions(model)
    # print(f"Reacciones bloqueadas: {blocked_reactions}")

    # # Verificar condiciones actuales del medio
    # print("\nCondiciones actuales del medio:")
    # for reaction in model.exchanges:
    #     if reaction.lower_bound < -1:
    #         print(f"{reaction.id}: {reaction.lower_bound} mmol/gDW/h")

# para evitar el error al usar multiprocessing
if __name__ == "__main__":
    run_fba()