"""
Avaliação das previsões realizadas
PreviGol v2
"""


def classificar_confianca(valor):

    """
    Classifica o nível de confiança.
    """

    if valor >= 70:
        return "Alta"

    elif valor >= 50:
        return "Média"

    else:
        return "Baixa"



def avaliar_previsao(previsao):

    """
    Recebe uma previsão e devolve
    uma avaliação de confiança.
    """


    confianca = previsao.get(
        "confianca",
        0
    )


    return {

        "confianca":
            round(
                confianca,
                2
            ),

        "nivel":
            classificar_confianca(
                confianca
            )

    }



def comparar_resultado(
    previsao,
    golos_casa_real,
    golos_fora_real
):

    """
    Compara previsão com resultado real.
    """


    resultado_previsto = (
        previsao.get(
            "resultado_previsto"
        )
    )


    resultado_real = (
        f"{golos_casa_real}-{golos_fora_real}"
    )


    acertou = (
        resultado_previsto ==
        resultado_real
    )


    return {

        "resultado_previsto":
            resultado_previsto,

        "resultado_real":
            resultado_real,

        "acertou":
            acertou

    }
