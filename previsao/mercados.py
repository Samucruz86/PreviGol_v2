"""
Cálculo de mercados baseado na matriz Poisson
PreviGol v2.7
"""

from previsao.modelo_poisson import calcular_matriz



def calcular_mercados(
    xg_casa,
    xg_fora
):
    """
    Calcula mercados através
    da matriz Poisson.
    """

    matriz = calcular_matriz(
        xg_casa,
        xg_fora
    )


    over15 = 0
    over25 = 0
    over35 = 0
    ambas_marcam = 0


    for resultado in matriz:


        golos_total = (
            resultado["golos_casa"]
            +
            resultado["golos_fora"]
        )


        prob = resultado[
            "probabilidade"
        ]



        # Over 1.5 golos

        if golos_total >= 2:

            over15 += prob



        # Over 2.5 golos

        if golos_total >= 3:

            over25 += prob



        # Over 3.5 golos

        if golos_total >= 4:

            over35 += prob



        # Ambas marcam

        if (
            resultado["golos_casa"] >= 1
            and
            resultado["golos_fora"] >= 1
        ):

            ambas_marcam += prob



    return {


        "over15":
            round(
                over15,
                2
            ),


        "over25":
            round(
                over25,
                2
            ),


        "over35":
            round(
                over35,
                2
            ),


        "ambas_marcam":
            round(
                ambas_marcam,
                2
            )

    }