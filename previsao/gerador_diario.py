"""
Gerador automático de previsões
PreviGol v2
"""

from database.db import ligar_bd
from previsao.motor import gerar_previsao



def obter_jogos_para_prever():

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            equipa_casa,
            equipa_fora
        FROM jogos
        WHERE golos_casa IS NULL
        OR golos_fora IS NULL
        """
    )


    jogos = cursor.fetchall()

    conn.close()


    return jogos



def gerar_previsoes_diarias():

    jogos = obter_jogos_para_prever()


    if not jogos:

        print(
            "Não existem jogos pendentes."
        )

        return



    contador = 0


    for jogo in jogos:

        equipa_casa = jogo[0]
        equipa_fora = jogo[1]


        print(
            f"A analisar {equipa_casa} vs {equipa_fora}"
        )


        try:

            previsao = gerar_previsao(
                equipa_casa,
                equipa_fora
            )


            print(
                "Previsão criada:",
                previsao["resultado_previsto"]
            )


            contador += 1


        except Exception as erro:

            print(
                "Erro:",
                erro
            )



    print(
        f"{contador} previsões geradas."
    )



if __name__ == "__main__":

    gerar_previsoes_diarias()