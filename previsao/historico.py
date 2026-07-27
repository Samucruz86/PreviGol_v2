"""
Histórico de previsões
PreviGol v2.4
"""

from database.repositorio import obter_historico_previsoes



def mostrar_historico():

    historico = obter_historico_previsoes()


    print("\n==============================================================")
    print("                    HISTÓRICO PREVIGOL")
    print("==============================================================")


    if not historico:

        print("Não existem previsões registadas.")
        print("==============================================================")
        return



    print(
        f'{"ID":>3}  '
        f'{"Jogo":<45} '
        f'{"Prev.":<6} '
        f'{"Real":<6} '
        f'Estado'
    )

    print(
        "--------------------------------------------------------------"
    )


    avaliadas = 0
    pendentes = 0



    for previsao in historico:


        if previsao["resultado_real"] is None:

            estado = "⏳"
            resultado_real = "-"

            pendentes += 1



        elif previsao["acertou"] == 1:

            estado = "✅"
            resultado_real = previsao["resultado_real"]

            avaliadas += 1



        else:

            estado = "❌"
            resultado_real = previsao["resultado_real"]

            avaliadas += 1



        jogo = (

            f'{previsao["equipa_casa"]} vs '

            f'{previsao["equipa_fora"]}'

        )



        print(

            f'{previsao["id"]:>3}  '

            f'{jogo:<45.45} '

            f'{previsao["resultado_previsto"]:<6} '

            f'{resultado_real:<6} '

            f'{estado}'

        )



    print(
        "--------------------------------------------------------------"
    )


    print(
        f"Total de previsões : {len(historico)}"
    )

    print(
        f"Avaliadas          : {avaliadas}"
    )

    print(
        f"Pendentes          : {pendentes}"
    )


    print(
        "=============================================================="
    )



if __name__ == "__main__":

    mostrar_historico()