"""
Modelo Poisson avançado
PreviGol v2.6 compatível
"""

import math



def probabilidade_poisson(
    media,
    golos
):
    """
    Probabilidade de uma equipa marcar
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
    max_golos=5
):
    """
    Cria matriz completa de resultados.
    """

    matriz = []


    for casa in range(max_golos + 1):

        for fora in range(max_golos + 1):


            prob_casa = probabilidade_poisson(
                xg_casa,
                casa
            )


            prob_fora = probabilidade_poisson(
                xg_fora,
                fora
            )


            probabilidade = (
                prob_casa
                *
                prob_fora
                *
                100
            )


            matriz.append(
                {
                    "resultado": f"{casa}-{fora}",

                    "golos_casa": casa,

                    "golos_fora": fora,

                    "probabilidade":
                        round(
                            probabilidade,
                            2
                        )
                }
            )


    return matriz



def analisar_resultados(
    xg_casa,
    xg_fora
):
    """
    Analisa vencedor e resultado provável.
    """

    matriz = calcular_matriz(
        xg_casa,
        xg_fora
    )


    matriz.sort(
        key=lambda x:
        x["probabilidade"],
        reverse=True
    )


    casa = 0
    empate = 0
    fora = 0


    for resultado in matriz:

        prob = resultado["probabilidade"]


        if resultado["golos_casa"] > resultado["golos_fora"]:

            casa += prob


        elif resultado["golos_casa"] == resultado["golos_fora"]:

            empate += prob


        else:

            fora += prob



    return {

        "resultado_provavel":
            matriz[0]["resultado"],


        "probabilidade_resultado":
            matriz[0]["probabilidade"],


        "melhores_resultados":
            matriz[:5],


        "vitoria_casa":
            round(casa, 2),


        "empate":
            round(empate, 2),


        "vitoria_fora":
            round(fora, 2)

    }