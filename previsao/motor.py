"""
Motor principal de previsão
PreviGol v2.4
"""

from previsao.calculo_xg import calcular_xg
from previsao.modelo_poisson import analisar_resultados
from previsao.mercados import calcular_mercados
from previsao.avaliacao import avaliar_previsao
from previsao.analise import analisar_previsao
from previsao.aprendizagem_pesos import carregar_pesos


from database.repositorio import (
    obter_estatisticas_equipa,
    guardar_previsao,
    previsao_existente,
    obter_previsao_existente
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


    if previsao_existente(
        equipa_casa,
        equipa_fora
    ):


        print(
            f"Previsão já existente: {equipa_casa} vs {equipa_fora}"
        )


        return obter_previsao_existente(
            equipa_casa,
            equipa_fora
        )



    print(
        f"A analisar {equipa_casa} vs {equipa_fora}"
    )



    dados_casa = obter_estatisticas_equipa(
        equipa_casa
    )


    dados_fora = obter_estatisticas_equipa(
        equipa_fora
    )


    if not dados_casa["dados_validos"]:

        return {

        "estado": "sem_dados",

        "equipa": equipa_casa,

        "mensagem":
            "Não existem estatísticas suficientes para gerar previsão"

       }



    if not dados_fora["dados_validos"]:

        return {

        "estado": "sem_dados",

        "equipa": equipa_fora,

        "mensagem":
            "Não existem estatísticas suficientes para gerar previsão"

        }



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

        resultado,

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

        "Moreirense",

        "Famalicão"

    )


    print("\nRESULTADO FINAL")

    print(resultado)