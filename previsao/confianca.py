"""
Sistema de confiança das previsões
PreviGol v3.1
"""

from previsao.aprendizagem_pesos import carregar_pesos



def limitar(valor, minimo=0, maximo=100):
    """
    Garante que um valor fica entre 0 e 100.
    """

    return max(
        minimo,
        min(valor, maximo)
    )



def calcular_confianca(
    mercados,
    resultado,
    xg_casa,
    xg_fora,
    forma_casa,
    forma_fora
):
    """
    Calcula nível de confiança adaptativo.

    Mantém aprendizagem dos pesos,
    mas com escala equilibrada.
    """

    pesos = carregar_pesos()


    if not pesos:

        pesos = {

            "resultado": 1.0,
            "over15": 1.0,
            "over25": 1.0,
            "ambas": 1.0

        }



    peso_resultado = pesos.get(
        "resultado",
        1.0
    )

    peso_over15 = pesos.get(
        "over15",
        1.0
    )

    peso_over25 = pesos.get(
        "over25",
        1.0
    )

    peso_ambas = pesos.get(
        "ambas",
        1.0
    )



    resultado_score = (
        resultado["vitoria_casa"]
        *
        peso_resultado
    )


    mercado_score = (

        mercados["over15"]
        *
        0.50
        *
        peso_over15

        +

        mercados["over25"]
        *
        0.50
        *
        peso_over25

    )



    ambas_score = (

        mercados["ambas_marcam"]
        *
        peso_ambas

    )



    xg_total = xg_casa + xg_fora


    xg_score = limitar(
        xg_total * 25
    )



    forma_media = (

        forma_casa
        +
        forma_fora

    ) / 2



    forma_score = limitar(
        forma_media * 20
    )



    confianca = (

        resultado_score * 0.30

        +

        mercado_score * 0.30

        +

        ambas_score * 0.15

        +

        xg_score * 0.15

        +

        forma_score * 0.10

    )



    return round(
        limitar(confianca),
        2
    )




def definir_nivel(confianca):
    """
    Define classificação da confiança.
    """

    if confianca >= 85:

        return "Muito Alta"


    elif confianca >= 70:

        return "Alta"


    elif confianca >= 50:

        return "Média"


    elif confianca >= 35:

        return "Baixa"


    else:

        return "Muito Baixa"