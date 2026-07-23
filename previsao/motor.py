"""
Motor principal de previsão
PreviGol v2.1
"""

from previsao.calculo_xg import calcular_xg
from previsao.modelo_poisson import analisar_resultados
from previsao.mercados import calcular_mercados
from previsao.avaliacao import avaliar_previsao
from previsao.analise import analisar_previsao

from database.repositorio import (
    obter_estatisticas_equipa,
    guardar_previsao,
    previsao_existente,
    obter_previsao_existente
)



def calcular_confianca(
    mercados,
    xg_casa,
    xg_fora,
    forma_casa,
    forma_fora
):
    """
    Calcula nível de confiança da previsão.
    """

    xg_total = xg_casa + xg_fora

    confianca = (

        mercados["over25"] * 0.40

        +

        mercados["ambas_marcam"] * 0.30

        +

        min(xg_total * 10, 100) * 0.20

        +

        ((forma_casa + forma_fora) / 2) * 0.10

    )

    return round(
        min(confianca, 100),
        2
    )



def definir_nivel(confianca):

    if confianca >= 70:
        return "Alta"

    elif confianca >= 50:
        return "Média"

    else:
        return "Baixa"





def gerar_previsao(
    equipa_casa,
    equipa_fora
):
    """
    Gera previsão automática.
    """



    # Verifica se já existe previsão

    if previsao_existente(
        equipa_casa,
        equipa_fora
    ):

        print(
            f"Previsão já existente: {equipa_casa} vs {equipa_fora}"
        )


        previsao_antiga = obter_previsao_existente(
            equipa_casa,
            equipa_fora
        )


        return previsao_antiga



    print(
        f"A analisar {equipa_casa} vs {equipa_fora}"
    )



    dados_casa = obter_estatisticas_equipa(
        equipa_casa
    )


    dados_fora = obter_estatisticas_equipa(
        equipa_fora
    )

    print("DEBUG DADOS CASA")
    print(dados_casa)

    print("DEBUG DADOS FORA")
    print(dados_fora)

    xg = calcular_xg(

        dados_casa["media_marcados_casa"],

        dados_casa["media_sofridos_casa"],

        dados_fora["media_marcados_fora"],

        dados_fora["media_sofridos_fora"],

        dados_casa["forma"],

        dados_fora["forma"]

    )



    xg_casa = round(
        xg["xg_casa"],
        2
    )


    xg_fora = round(
        xg["xg_fora"],
        2
    )


    print("DEBUG XG ANTES POISSON:")
    print(xg_casa)
    print(xg_fora)

    resultado = analisar_resultados(

        xg_casa,

        xg_fora

    )



    mercados = calcular_mercados(

        xg_casa,

        xg_fora

    )



    confianca = calcular_confianca(

        mercados,

        xg_casa,

        xg_fora,

        dados_casa["forma"],

        dados_fora["forma"]

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
            confianca,


        "nivel":
            definir_nivel(
                confianca
            )

    }



    # Avaliação automática

    previsao.update(

        avaliar_previsao(
            previsao
        )

    )



    # Análise do mercado recomendado

    previsao["analise"] = analisar_previsao(

        previsao

    )



    # Guardar previsão na BD

    guardar_previsao(

        previsao

    )



    return previsao






if __name__ == "__main__":


    resultado = gerar_previsao(

        "Sporting",

        "Porto"

    )


    print("\nRESULTADO FINAL")

    print(resultado)