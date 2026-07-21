"""
Análise de forma recente das equipas
PreviGol v2
"""

from database.db import ligar_bd



def obter_forma(equipa, ultimos=5):

    """
    Calcula a forma da equipa
    com base nos últimos jogos.

    Retorna uma pontuação entre 0 e 10.
    """

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT 
            equipa_casa,
            equipa_fora,
            golos_casa,
            golos_fora
        FROM jogos
        WHERE equipa_casa = ?
           OR equipa_fora = ?
        ORDER BY data DESC
        LIMIT ?
        """,
        (
            equipa,
            equipa,
            ultimos
        )
    )


    jogos = cursor.fetchall()

    conn.close()


    if not jogos:

        return {

            "forma": 5,

            "vitorias": 0,

            "empates": 0,

            "derrotas": 0

        }


    pontos = 0

    vitorias = 0

    empates = 0

    derrotas = 0



    for jogo in jogos:

        casa = jogo[0]

        fora = jogo[1]

        golos_casa = jogo[2]

        golos_fora = jogo[3]


        if equipa == casa:

            marcados = golos_casa

            sofridos = golos_fora


        else:

            marcados = golos_fora

            sofridos = golos_casa



        if marcados > sofridos:

            pontos += 3

            vitorias += 1


        elif marcados == sofridos:

            pontos += 1

            empates += 1


        else:

            derrotas += 1



    maximo = len(jogos) * 3


    forma = (
        pontos /
        maximo
    ) * 10



    return {

        "forma":

            round(
                forma,
                2
            ),

        "vitorias":

            vitorias,

        "empates":

            empates,

        "derrotas":

            derrotas

    }
