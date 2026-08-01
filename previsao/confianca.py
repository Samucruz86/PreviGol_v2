"""
Sistema de confiança das previsões
PreviGol v3.0
"""

from previsao.aprendizagem_pesos import carregar_pesos



def calcular_confianca(
    mercados,
    resultado,
    xg_casa,
    xg_fora,
    forma_casa,
    forma_fora
):
    """
    Calcula nível de confiança adaptativo
    usando os pesos aprendidos.
    """

    pesos = carregar_pesos()


    if not pesos:

        pesos = {

            "resultado": 0.5,
            "over15": 0.5,
            "over25": 0.5,
            "ambas": 0.5

        }


    xg_total = xg_casa + xg_fora


    confianca = (

        resultado["vitoria_casa"]
        *
        0.25
        *
        pesos["resultado"]


        +

        mercados["over15"]
        *
        0.25
        *
        pesos["over15"]


        +

        mercados["over25"]
        *
        0.20
        *
        pesos["over25"]


        +

        mercados["ambas_marcam"]
        *
        0.20
        *
        pesos["ambas"]


        +

        min(
            xg_total * 10,
            100
        )
        *
        0.05


        +

        (
            (forma_casa + forma_fora)
            /
            2
        )
        *
        0.05

    )


    return round(
        min(confianca, 100),
        2
    )



def definir_nivel(confianca):
    """
    Define classificação da confiança.
    """

    if confianca >= 70:

        return "Alta"


    elif confianca >= 50:

        return "Média"


    else:

        return "Baixa"