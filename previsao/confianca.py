"""
Sistema de confiança das previsões
PreviGol v3.2
"""

from previsao.aprendizagem_pesos import carregar_pesos



def limitar(valor, minimo=0, maximo=100):

    return max(
        minimo,
        min(valor, maximo)
    )



def calcular_consistencia(
    mercados,
    resultado,
    xg_casa,
    xg_fora
):
    """
    Mede o acordo entre os indicadores.
    Resultado entre 0 e 100.
    """

    pontos = 0


    # Resultado forte + xG favorável

    xg_total = xg_casa + xg_fora


    if resultado["vitoria_casa"] >= 65 and xg_casa >= xg_fora:

        pontos += 30


    elif resultado["vitoria_fora"] >= 65 and xg_fora >= xg_casa:

        pontos += 30


    elif resultado["empate"] >= 45:

        pontos += 20



    # Mercados de golos coerentes com xG

    if xg_total >= 2.8 and mercados["over15"] >= 70:

        pontos += 25


    elif xg_total >= 2.2 and mercados["over15"] >= 60:

        pontos += 20


    else:

        pontos += 10



    # Over 2.5 confirma tendência

    if mercados["over25"] >= 60:

        pontos += 20


    elif mercados["over25"] >= 45:

        pontos += 10



    # Ambas marcam como indicador complementar

    if mercados["ambas_marcam"] >= 55:

        pontos += 15


    elif mercados["ambas_marcam"] >= 35:

        pontos += 10



    return limitar(pontos)




def calcular_confianca(
    mercados,
    resultado,
    xg_casa,
    xg_fora,
    forma_casa,
    forma_fora
):

    pesos = carregar_pesos()


    if not pesos:

        pesos = {

            "resultado": 1.0,
            "over15": 1.0,
            "over25": 1.0,
            "ambas": 1.0

        }



    resultado_score = (
        resultado["vitoria_casa"]
        *
        pesos.get("resultado", 1.0)
    )



    mercado_score = (

        mercados["over15"]
        *
        0.50
        *
        pesos.get("over15", 1.0)

        +

        mercados["over25"]
        *
        0.50
        *
        pesos.get("over25", 1.0)

    )



    ambas_score = (

        mercados["ambas_marcam"]
        *
        pesos.get("ambas", 1.0)

    )



    xg_score = limitar(
        (xg_casa + xg_fora) * 25
    )



    forma_score = limitar(

        (
            forma_casa
            +
            forma_fora
        )
        /
        2
        *
        20

    )



    consistencia = calcular_consistencia(

        mercados,
        resultado,
        xg_casa,
        xg_fora

    )



    confianca = (

        resultado_score * 0.30

        +

        mercado_score * 0.25

        +

        ambas_score * 0.05

        +

        xg_score * 0.15

        +

        forma_score * 0.10

        +

        consistencia * 0.20

    )



    return round(
        limitar(confianca),
        2
    )




def definir_nivel(confianca):

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