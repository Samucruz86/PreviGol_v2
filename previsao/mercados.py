"""
Cálculo dos mercados de golos
PreviGol v2
"""

from .modelo_poisson import calcular_matriz



def calcular_mercados(
    xg_casa,
    xg_fora
):

    matriz = calcular_matriz(
        xg_casa,
        xg_fora
    )


    over15 = 0
    over25 = 0
    over35 = 0
    ambas_marcam = 0


    for resultado in matriz:

        total_golos = (
            resultado["golos_casa"]
            +
            resultado["golos_fora"]
        )


        probabilidade = resultado["probabilidade"]


        if total_golos >= 2:
            over15 += probabilidade


        if total_golos >= 3:
            over25 += probabilidade


        if total_golos >= 4:
            over35 += probabilidade


        if (
            resultado["golos_casa"] > 0
            and
            resultado["golos_fora"] > 0
        ):
            ambas_marcam += probabilidade



    return {

        "over15":
            round(over15, 2),

        "over25":
            round(over25, 2),

        "over35":
            round(over35, 2),

        "ambas_marcam":
            round(ambas_marcam, 2)

    }
