"""
Sistema de aprendizagem PreviGol v1.0
Analisa desempenho histórico do modelo
"""

from previsao.estatisticas_modelo import obter_estatisticas



def analisar_desempenho():

    estatisticas = obter_estatisticas()


    print("\n==========================")
    print(" APRENDIZAGEM PREVIGOL")
    print("==========================\n")


    print(
        f"Jogos avaliados: {estatisticas['total_avaliacoes']}"
    )

    print(
        f"Resultado exato: {estatisticas['resultado_exato']}%"
    )

    print(
        f"Over 1.5: {estatisticas['over15']}%"
    )

    print(
        f"Over 2.5: {estatisticas['over25']}%"
    )

    print(
        f"Ambas marcam: {estatisticas['ambas_marcam']}%"
    )


    print("\nANÁLISE:")


    if estatisticas["total_avaliacoes"] == 0:

        print(
            "Ainda não existem avaliações suficientes."
        )

        return



    if estatisticas["over15"] >= 70:

        print(
            "✓ Modelo forte no mercado Over 1.5"
        )

    else:

        print(
            "⚠ Melhorar previsão de golos"
        )



    if estatisticas["over25"] < 50:

        print(
            "⚠ Over 2.5 com baixo desempenho"
        )


    if estatisticas["resultado_exato"] < 30:

        print(
            "⚠ Resultado exato necessita calibração"
        )


    print(
        "\nFim da análise."
    )



if __name__ == "__main__":

    analisar_desempenho()