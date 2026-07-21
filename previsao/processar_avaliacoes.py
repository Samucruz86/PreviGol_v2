"""
Processamento automático de avaliações
PreviGol v2
"""


from database.repositorio import (
    obter_previsoes_pendentes,
    guardar_avaliacao,
    previsao_ja_avaliada
)

from previsao.avaliar_resultados import criar_avaliacao



def avaliar_jogo(previsao_id, resultado_real):

    if previsao_ja_avaliada(previsao_id):

        return {
            "mensagem": "Previsão j+á avaliada"
        }

    previsoes = obter_previsoes_pendentes()


    for previsao in previsoes:

        if previsao["id"] == previsao_id:

            avaliacao = criar_avaliacao(
                previsao,
                resultado_real
            )

            guardar_avaliacao(
                avaliacao
            )

            return avaliacao


    return None



if __name__ == "__main__":

    resultado = avaliar_jogo(
        2,
        "2-1"
    )

    print(resultado)