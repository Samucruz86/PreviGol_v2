"""
Motor principal de previsão
PreviGol v2
"""

from previsao.calculo_xg import calcular_xg
from previsao.modelo_poisson import analisar_resultados
from previsao.mercados import calcular_mercados
from previsao.avaliacao import avaliar_previsao
from previsao.analise import analisar_previsao
from database.repositorio import obter_estatisticas_equipa, guardar_previsao



def gerar_previsao(
    equipa_casa,
    equipa_fora
):
    """
    Gera uma previsão automática
    usando dados da base de dados.
    """


    dados_casa = obter_estatisticas_equipa(
        equipa_casa
    )


    dados_fora = obter_estatisticas_equipa(
        equipa_fora
    )



    xg = calcular_xg(

    dados_casa["media_casa"],
    dados_casa["golos_sofridos"],
    dados_fora["media_fora"],
    dados_fora["golos_sofridos"]
    )


    xg_casa = xg["xg_casa"]

    xg_fora = xg["xg_fora"]



    resultado = analisar_resultados(
        xg_casa,
        xg_fora
    )


    mercados = calcular_mercados(
        xg_casa,
        xg_fora
    )



    confianca = max(

        resultado["vitoria_casa"],

        resultado["empate"],

        resultado["vitoria_fora"]

    )



    previsao = {

        "equipa_casa":
            equipa_casa,

        "equipa_fora":
            equipa_fora,

        "xg_casa":
            xg_casa,

        "xg_fora":
            xg_fora,

        "resultado_previsto":
            resultado["resultado_provavel"],

        "vitoria_casa":
            resultado["vitoria_casa"],

        "empate":
            resultado["empate"],

        "vitoria_fora":
            resultado["vitoria_fora"],

        "over15":
            mercados["over15"],

        "over25":
            mercados["over25"],

        "over35":
            mercados["over35"],

        "ambas_marcam":
            mercados["ambas_marcam"],

        "confianca":
            round(confianca,2)

    }


    previsao.update(
        avaliar_previsao(
            previsao
        )
    )

    previsao["analise"] = analisar_previsao(
        previsao
    )


    guardar_previsao(
        previsao
    )


    return previsao



if __name__ == "__main__":


    resultado = gerar_previsao(
        "Benfica",
        "Braga"
    )


    print(resultado)
