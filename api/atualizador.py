"""
Atualizador de jogos PreviGol
v0.7.3
"""

from api.football_api import obter_jogos
from api.mapper import converter_lista_jogos

from database.db import ligar_bd



def guardar_jogos(jogos):

    conn = ligar_bd()
    cursor = conn.cursor()


    for jogo in jogos:

        cursor.execute(
            """
            INSERT INTO jogos
            (
                equipa_casa,
                equipa_fora,
                golos_casa,
                golos_fora,
                data,
                estado
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                jogo["equipa_casa"],
                jogo["equipa_fora"],
                jogo["golos_casa"],
                jogo["golos_fora"],
                jogo["data"],
                jogo["estado"]
            )
        )


    conn.commit()
    conn.close()



def atualizar_jogos(data):

    resposta = obter_jogos(data)

    jogos = converter_lista_jogos(
        resposta
    )

    guardar_jogos(
        jogos
    )

    print(
        f"{len(jogos)} jogos adicionados."
    )



if __name__ == "__main__":

    atualizar_jogos(
        "2026-07-21"
    )