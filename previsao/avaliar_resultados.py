"""
Avaliação automática das previsões
PreviGol v2
"""


def calcular_golos(resultado):
    """
    Extrai golos de um resultado X-X
    """

    casa, fora = resultado.split("-")

    return int(casa), int(fora)



def avaliar_resultado(
    resultado_previsto,
    resultado_real
):

    if resultado_previsto == resultado_real:
        return 1

    return 0



def avaliar_over15(resultado_real):

    casa, fora = calcular_golos(resultado_real)

    total = casa + fora

    if total >= 2:
        return 1

    return 0



def avaliar_over25(resultado_real):

    casa, fora = calcular_golos(resultado_real)

    total = casa + fora

    if total >= 3:
        return 1

    return 0



def avaliar_ambas(resultado_real):

    casa, fora = calcular_golos(resultado_real)

    if casa > 0 and fora > 0:
        return 1

    return 0



def criar_avaliacao(previsao, resultado_real):

    return {

        "previsao_id":
            previsao["id"],

        "resultado_real":
            resultado_real,

        "acertou":
            avaliar_resultado(
                previsao["resultado_previsto"],
                resultado_real
            ),

        "acertou_over15":
            avaliar_over15(
                resultado_real
            ),

        "acertou_over25":
            avaliar_over25(
                resultado_real
            ),

        "acertou_ambas":
            avaliar_ambas(
                resultado_real
            )
    }