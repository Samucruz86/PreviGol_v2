"""
Modelo de Poisson
PreviGol v2
"""

import math



def poisson(media, golos):

    """
    Calcula a probabilidade de uma equipa marcar
    determinado número de golos.
    """

    return (
        math.exp(-media)
        *
        (media ** golos)
        /
        math.factorial(golos)
    )



def calcular_matriz(
    xg_casa,
    xg_fora,
    max_golos=6
):

    """
    Cria todas as combinações possíveis
    de resultados.
    """

    resultados = []


    for golos_casa in range(max_golos + 1):

        for golos_fora in range(max_golos + 1):

            probabilidade = (
                poisson(
                    xg_casa,
                    golos_casa
                )
                *
                poisson(
                    xg_fora,
                    golos_fora
                )
            )


            resultados.append(
                {
                    "resultado":
                        f"{golos_casa}-{golos_fora}",

                    "golos_casa":
                        golos_casa,

                    "golos_fora":
                        golos_fora,

                    "probabilidade":
                        round(
                            probabilidade * 100,
                            4
                        )
                }
            )


    return sorted(
        resultados,
        key=lambda x: x["probabilidade"],
        reverse=True
    )



def analisar_resultados(
    xg_casa,
    xg_fora
):

    matriz = calcular_matriz(
        xg_casa,
        xg_fora
    )


    vitoria_casa = 0
    empate = 0
    vitoria_fora = 0


    for resultado in matriz:

        if resultado["golos_casa"] > resultado["golos_fora"]:

            vitoria_casa += resultado["probabilidade"]


        elif resultado["golos_casa"] == resultado["golos_fora"]:

            empate += resultado["probabilidade"]


        else:

            vitoria_fora += resultado["probabilidade"]



    return {

        "resultado_provavel":
            matriz[0]["resultado"],

        "vitoria_casa":
            round(vitoria_casa, 2),

        "empate":
            round(empate, 2),

        "vitoria_fora":
            round(vitoria_fora, 2),

        "top_resultados":
            matriz[:10]

    }
