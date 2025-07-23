
import cobra
from cobra.io import read_sbml_model


def run_fba():
# Cargar el modelo de la carpeta 
    model = read_sbml_model("C:/Users/felip/Desktop/python/TESIS/iYO844.xml")

    for reaction in model.exchanges:
        reaction.lower_bound = -1.95  # Prohibir importación por defecto

    # minimal_medium = { # establecer medio 
    #     "EX_glc__D_LSQBKTe_RSQBKT": -10,   # Fuente de carbono: glucosa
    #     "EX_nh4_LSQBKTe_RSQBKT": -5,    # Fuente de nitrógeno: amonio
    #     "EX_pi_LSQBKTe_RSQBKT": -3,     # Fuente de fósforo: fosfato
    #     "EX_so4_LSQBKTe_RSQBKT": -3,    # Fuente de azufre: sulfato
    #     "EX_o2_LSQBKTe_RSQBKT": -20,    # Fuente de oxígeno: condiciones aerobias
    #     "EX_k_LSQBKTe_RSQBKT": -2,      # Potasio
    #     "EX_na1_LSQBKTe_RSQBKT": -2,    # Sodio
    #     "EX_mg2_LSQBKTe_RSQBKT": -1,    # Magnesio
    #     "EX_ca2_LSQBKTe_RSQBKT": -1     # Calcio
    # }

    # model.reactions.get_by_id("EX_pyr_e").lower_bound = -8.71  # metabolito que se consume
    # model.reactions.get_by_id("EX_glu__D_LSQBKTe_RSQBKT").lower_bound = 0  # consume glucosa, por defecto está en -10, es decir si no se pone sustrato será la glucosa
    # model.reactions.get_by_id("EX_glu__D_LSQBKTe_RSQBKT").upper_bound = 0

    # # acetato > EX_ac_LSQBKTe_RSQBKT ; Valor de la función objetivo: 
    # etanol > EX_etoh_LSQBKTe_RSQBKT ; Valor de la función objetivo: 0.69
    # D-fructosa > EX_fru_LSQBKTe_RSQBKT ; Valor de la función objetivo: 1.79
    # fumarato > EX_fum_LSQBKTe_RSQBKT; Valor de la función objetivo: 0.78
    # D-glucosa > EX_glc__D_LSQBKTe_RSQBKT ; Valor de la función objetivo: 1.79
    # L-glutamina > EX_gln__L_LSQBKTe_RSQBKT; Valor de la función objetivo: 1.16
    # L-glutamato > EX_glu__L_LSQBKTe_RSQBKT; Valor de la función objetivo: 1.24
    # l-lactato > EX_lac__L_LSQBKTe_RSQBKT; Valor de la función objetivo: 0.74
    # L-malato > EX_mal__L_LSQBKTe_RSQBKT; Valor de la función objetivo: 0.78
    # piruvato > EX_pyr_LSQBKTe_RSQBKT; Valor de la función objetivo: 0.62
    # succinato > EX_succ_LSQBKTe_RSQBKT; Valor de la función objetivo: 0.84

    # model.medium = minimal_medium  # establecer el medio inicial

    # Permitir captación ilimitada de oxígeno
    model.reactions.get_by_id("EX_o2_LSQBKTe_RSQBKT").lower_bound = -1000  # Consumo de O2
    model.reactions.get_by_id("EX_fum_LSQBKTe_RSQBKT").lower_bound = -10  # Consumo de O2
    model.reactions.get_by_id("EX_pi_LSQBKTe_RSQBKT").lower_bound = -3  # Consumo de O2
    model.reactions.get_by_id("EX_nh4_LSQBKTe_RSQBKT").lower_bound = -5  # Consumo de O2
    model.reactions.get_by_id("EX_so4_LSQBKTe_RSQBKT").lower_bound = -3  # Consumo de O2
    model.reactions.get_by_id("EX_k_LSQBKTe_RSQBKT").lower_bound = -2  # Consumo de O2
    model.reactions.get_by_id("EX_mg2_LSQBKTe_RSQBKT").lower_bound = -1  # Consumo de O2
    model.reactions.get_by_id("EX_ca2_LSQBKTe_RSQBKT").lower_bound = -1  # Consumo de O2
    model.reactions.get_by_id("EX_na1_LSQBKTe_RSQBKT").lower_bound = -2  # Consumo de O2

    # Ejecutar la optimización FBA, la biomasa es la función objetivo por defecto
    solution = model.optimize()

    # Imprimir resultados
    print(f"Valor de la función objetivo (biomasa): {solution.objective_value}")

    # print("\nCondiciones actuales del medio:")
    # for reaction in model.exchanges:
    #     if reaction.lower_bound < 0:
    #         print(f"{reaction.id}: {reaction.lower_bound} mmol/gDW/h")


# # Verificar reacciones bloqueadas
# blocked_reactions = cobra.flux_analysis.find_blocked_reactions(model)
# print(f"Reacciones bloqueadas: {blocked_reactions}")
if __name__ == "__main__":
    run_fba()