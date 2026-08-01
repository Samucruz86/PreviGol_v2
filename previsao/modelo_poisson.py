"""
Modelo Poisson inteligente
PreviGol v2.8
"""

import math



def probabilidade_poisson(
    media,
    golos
):
    """
    Calcula a probabilidade de uma equipa
    marcar determinado número de golos.
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
    max_golos=7
):
    """
    Cria matriz de resultados usando Poisson.
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
                            4
                        )
                }
            )


    return matriz



def calcular_score_resultado(
    resultado,
    xg_casa,
    xg_fora
):
    """
    Score inteligente para selecionar
    o resultado mais coerente.
    """

    probabilidade = resultado["probabilidade"]


    golos_casa = resultado["golos_casa"]

    golos_fora = resultado["golos_fora"]


    score = probabilidade



    diferenca_xg = xg_casa - xg_fora


    diferenca_golos = (
        golos_casa
        -
        golos_fora
    )


    if diferenca_xg > 1:

        if diferenca_golos > 1:
            score += 2


        if diferenca_golos < 0:
            score -= 3



    elif diferenca_xg < -1:

        if diferenca_golos < -1:
            score += 2


        if diferenca_golos > 0:
            score -= 3



    if (
        golos_casa == 0
        and
        golos_fora == 0
    ):

        score -= 2



    if (
        golos_casa == golos_fora
        and
        abs(diferenca_xg) > 1
    ):

        score -= 3



    return score



def analisar_resultados(
    xg_casa,
    xg_fora
):
    """
    Analisa resultado provável,
    vencedor e probabilidades.
    """

    matriz = calcular_matriz(
        xg_casa,
        xg_fora
    )


    for resultado in matriz:

        resultado["score"] = calcular_score_resultado(
            resultado,
            xg_casa,
            xg_fora
        )


    matriz.sort(
        key=lambda x:
        x["score"],
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
            round(
                matriz[0]["probabilidade"],
                2
            ),


        "melhores_resultados":
            matriz[:5],


        "vitoria_casa":
            round(
                casa,
                2
            ),


        "empate":
            round(
                empate,
                2
            ),


        "vitoria_fora":
            round(
                fora,
                2
            )

    }