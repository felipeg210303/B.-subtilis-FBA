import cobra
from cobra.io import read_sbml_model
import matplotlib.pyplot as plt

def run_fba():
    # Cargar el modelo de la carpeta 
    model = read_sbml_model("C:/Users/felip/Desktop/python/TESIS/ibsu1147_bigg.xml")

    # # límite inferior de todas las reacciones
    # for reaction in model.reactions:
    #     reaction.lower_bound = -10
    # # Prohibir importación de otros substratos además del que le voy a poner
    # for reaction in model.exchanges:
    #     reaction.lower_bound = -0.0
    
    # # medio mínimo
    # model.reactions.get_by_id("EX_cpd00007_e").lower_bound = -18 # oxígeno
 
    # model.reactions.get_by_id("EX_cpd00029_e").lower_bound = -8.71 # acetato
    # model.reactions.get_by_id("R_EX_etoh_e").lower_bound = -8.71 # etanol
    # model.reactions.get_by_id("EX_cpd00082_e").lower_bound = -8.71 # fructosa
    # model.reactions.get_by_id("EX_cpd00106_e").lower_bound = -8.71 # fumarato
    # model.reactions.get_by_id("EX_cpd00053_e").lower_bound = -8.71 # glutamina
    # model.reactions.get_by_id("EX_cpd00023_e").lower_bound = -8.71 # glutamato
    # model.reactions.get_by_id("EX_cpd00159_e").lower_bound = -8.71 # lactato
    # model.reactions.get_by_id("EX_cpd00386_e").lower_bound = -8.71 # malato
    # model.reactions.get_by_id("EX_cpd00020_e").lower_bound = -8.71 # piruvato
    # model.reactions.get_by_id("EX_cpd00036_e").lower_bound = -8.71 # succinato

    # model.reactions.get_by_id("EX_cpd00027_e").lower_bound = -20 # glucosa
    # model.reactions.get_by_id("EX_cpd00009_e").lower_bound = -3 # fosfato
    # model.reactions.get_by_id("EX_cpd00013_e").lower_bound = -5 # amonio
    # model.reactions.get_by_id("EX_cpd00048_e").lower_bound = -3 # sulfato
    # model.reactions.get_by_id("EX_cpd00205_e").lower_bound = -2 #potasio
    # model.reactions.get_by_id("EX_cpd00254_e").lower_bound = -1 # magnesio
    # model.reactions.get_by_id("EX_cpd00063_e").lower_bound = -1 # calcio
    # model.reactions.get_by_id("EX_cpd00971_e").lower_bound = -2 # sodio

    solution = model.optimize() 

 # para visualizar los flujos metabólicos
    # fluxes = solution.fluxes

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