"""
Conversor de dados API-Football
PreviGol v0.7.3
"""


def converter_jogo(jogo):

    return {

        "equipa_casa":
            jogo["teams"]["home"]["name"],


        "equipa_fora":
            jogo["teams"]["away"]["name"],


        "golos_casa":
            jogo["goals"]["home"],


        "golos_fora":
            jogo["goals"]["away"],


        "data":
            jogo["fixture"]["date"],


        "estado":
            jogo["fixture"]["status"]["short"]

    }



def converter_lista_jogos(resposta):

    jogos = []

    for jogo in resposta["response"]:

        jogos.append(
            converter_jogo(jogo)
        )


    return jogos