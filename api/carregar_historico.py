"""
Carregador histórico API-Football
PreviGol v2.2

Carrega jogos históricos para a base de dados
"""

from api.football_api import obter_jogos_liga
from api.mapper import converter_lista_jogos

from database.db import ligar_bd



def jogo_existe(cursor, jogo):
    """
    Verifica se o jogo já existe na BD.
    """

    cursor.execute(
        """
        SELECT id
        FROM jogos
        WHERE equipa_casa = ?
        AND equipa_fora = ?
        AND data = ?
        """,
        (
            jogo["equipa_casa"],
            jogo["equipa_fora"],
            jogo["data"]
        )
    )

    return cursor.fetchone() is not None



def guardar_jogos(jogos):
    """
    Guarda jogos evitando duplicados.
    """

    conn = ligar_bd()
    cursor = conn.cursor()


    novos = 0
    existentes = 0


    for jogo in jogos:


        if jogo_existe(cursor, jogo):

            existentes += 1

            continue



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


        novos += 1



    conn.commit()

    conn.close()


    return novos, existentes



def carregar_historico(
    liga,
    epoca
):

    print(
        "\n=========================="
    )

    print(
        " CARREGAR HISTÓRICO"
    )

    print(
        "=========================="
    )


    print(
        f"Liga: {liga}"
    )


    print(
        f"Época: {epoca}\n"
    )



    resposta = obter_jogos_liga(
        liga,
        epoca
    )


    jogos = converter_lista_jogos(
        resposta
    )


    print(
        f"Jogos encontrados: {len(jogos)}"
    )


    novos, existentes = guardar_jogos(
        jogos
    )


    print(
        f"Jogos novos adicionados: {novos}"
    )


    print(
        f"Jogos já existentes: {existentes}"
    )



if __name__ == "__main__":


    carregar_historico(

        94,

        2024

    )