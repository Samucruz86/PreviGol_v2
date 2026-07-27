"""
Dashboard Analytics
PreviGol v2.4
"""

from previsao.estatisticas_modelo import obter_estatisticas


def calcular_fiabilidade(dados):
    """
    Calcula a fiabilidade global do modelo.
    """

    return round(

        (

            dados["resultado_exato"]

            +

            dados["over15"]

            +

            dados["over25"]

            +

            dados["ambas_marcam"]

        ) / 4,

        2

    )


def obter_classificacao(fiabilidade):

    if fiabilidade >= 80:
        return "Excelente"

    elif fiabilidade >= 70:
        return "Muito Boa"

    elif fiabilidade >= 60:
        return "Boa"

    elif fiabilidade >= 50:
        return "Razoável"

    else:
        return "Em aprendizagem"



def mostrar_dashboard():

    dados = obter_estatisticas()

    fiabilidade = calcular_fiabilidade(
        dados
    )



    mercados = {

        "Resultado Exato":
            dados["resultado_exato"],

        "Over 1.5":
            dados["over15"],

        "Over 2.5":
            dados["over25"],

        "Ambas Marcam":
            dados["ambas_marcam"]

    }



    melhor = max(
        mercados,
        key=mercados.get
    )



    pior = min(
        mercados,
        key=mercados.get
    )



    print("\n======================================")
    print("        PREVIGOL ANALYTICS")
    print("======================================")

    print(
        f"Jogos avaliados............. {dados['total_avaliacoes']}"
    )

    print(
        f"Resultado exato............ {dados['resultado_exato']}%"
    )

    print(
        f"Over 1.5................... {dados['over15']}%"
    )

    print(
        f"Over 2.5................... {dados['over25']}%"
    )

    print(
        f"Ambas marcam............... {dados['ambas_marcam']}%"
    )

    print("--------------------------------------")

    print(
        f"Fiabilidade global......... {fiabilidade}%"
    )

    print(
        f"Classificação.............. {obter_classificacao(fiabilidade)}"
    )

    print(
        f"Melhor mercado............ {melhor}"
    )

    print(
        f"Mercado a melhorar........ {pior}"
    )

    print("======================================")



if __name__ == "__main__":

    mostrar_dashboard()