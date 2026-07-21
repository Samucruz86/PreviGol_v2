def analisar_previsao(previsao):
    """
    Analisa uma previsão e devolve recomendações.
    """

    analise = {}

    xg_total = previsao["xg_casa"] + previsao["xg_fora"]

    over15 = previsao["over15"]
    over25 = previsao["over25"]
    ambas = previsao["ambas_marcam"]
    confianca = previsao["confianca"]


    # Mercado recomendado
    mercados = []


    if over15 >= 75 and xg_total >= 2.3:
        mercados.append(
            ("Over 1.5", over15)
        )


    if over25 >= 60 and xg_total >= 2.8:
        mercados.append(
            ("Over 2.5", over25)
        )


    if ambas >= 60 and previsao["xg_casa"] >= 1.2 and previsao["xg_fora"] >= 1.0:
        mercados.append(
            ("Ambas marcam", ambas)
        )


    if mercados:
        melhor = max(
            mercados,
            key=lambda x: x[1]
        )

        analise["mercado"] = melhor[0]
        analise["probabilidade"] = melhor[1]

    else:
        analise["mercado"] = "Sem aposta recomendada"
        analise["probabilidade"] = 0

   


    # Comentário automático

    if xg_total >= 3:
        comentario = "Jogo com forte tendência de golos"

    elif xg_total >= 2:
        comentario = "Jogo com tendência moderada de golos"

    else:
        comentario = "Jogo de baixa expectativa de golos"


    analise["comentario"] = comentario


    return analise