"""
Repositório de acesso à base de dados
PreviGol v2.9
"""

from database.db import ligar_bd



def obter_estatisticas_equipa(equipa):

    conn = ligar_bd()
    cursor = conn.cursor()


    # Pesquisa exata

    cursor.execute(
        """
        SELECT

            jogos,

            golos_marcados,

            golos_sofridos,

            media_casa,

            media_fora,

            forma,

            media_marcados_casa,

            media_sofridos_casa,

            media_marcados_fora,

            media_sofridos_fora

        FROM estatisticas_equipas

        WHERE equipa = ?

        """,
        (equipa,)
    )


    dados = cursor.fetchone()



    # Pesquisa aproximada

    if not dados:

        cursor.execute(
            """
            SELECT

                jogos,

                golos_marcados,

                golos_sofridos,

                media_casa,

                media_fora,

                forma,

                media_marcados_casa,

                media_sofridos_casa,

                media_marcados_fora,

                media_sofridos_fora

            FROM estatisticas_equipas

            WHERE equipa LIKE ?

            LIMIT 1

            """,
            (
                f"%{equipa}%",
            )
        )


        dados = cursor.fetchone()



    conn.close()



    # Equipa inexistente

    if not dados:

        return {

            "jogos": 0,

            "golos_marcados": 1.5,

            "golos_sofridos": 1.2,

            "media_casa": 1.5,

            "media_fora": 1.2,

            "forma": 3,

            "media_marcados_casa": 1.5,

            "media_sofridos_casa": 1.2,

            "media_marcados_fora": 1.2,

            "media_sofridos_fora": 1.5

        }



    return {

        "jogos": dados[0],

        "golos_marcados": dados[1],

        "golos_sofridos": dados[2],

        "media_casa": dados[3],

        "media_fora": dados[4],

        "forma": dados[5],

        "media_marcados_casa": dados[6],

        "media_sofridos_casa": dados[7],

        "media_marcados_fora": dados[8],

        "media_sofridos_fora": dados[9]

    }




def obter_media_liga():

    """
    Calcula média global de golos da liga.
    """

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT

            AVG(golos_casa),

            AVG(golos_fora)

        FROM jogos

        WHERE estado IN ('FT','AET','PEN')

        """
    )


    dados = cursor.fetchone()


    conn.close()



    if not dados or not dados[0]:

        return 1.45



    return round(

        (dados[0] + dados[1]) / 2,

        2

    )




def guardar_previsao(previsao):

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO previsoes
        (

            equipa_casa,

            equipa_fora,

            xg_casa,

            xg_fora,

            resultado_previsto,

            over15,

            over25,

            ambas_marcam,

            confianca

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

        """,

        (

            previsao["equipa_casa"],

            previsao["equipa_fora"],

            previsao["xg_casa"],

            previsao["xg_fora"],

            previsao["resultado_previsto"],

            previsao["over15"],

            previsao["over25"],

            previsao["ambas_marcam"],

            previsao["confianca"]

        )

    )


    conn.commit()

    conn.close()




def previsao_existente(
    equipa_casa,
    equipa_fora
):

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT id

        FROM previsoes

        WHERE equipa_casa=?

        AND equipa_fora=?

        """,

        (
            equipa_casa,

            equipa_fora

        )

    )


    resultado = cursor.fetchone()


    conn.close()


    return resultado is not None




def obter_previsao_existente(
    equipa_casa,
    equipa_fora
):

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *

        FROM previsoes

        WHERE equipa_casa=?

        AND equipa_fora=?

        ORDER BY id DESC

        LIMIT 1

        """,

        (
            equipa_casa,

            equipa_fora

        )

    )


    dados = cursor.fetchone()


    conn.close()



    if not dados:

        return None



    return {

        "id": dados[0],

        "equipa_casa": dados[1],

        "equipa_fora": dados[2],

        "xg_casa": dados[3],

        "xg_fora": dados[4],

        "resultado_previsto": dados[5],

        "over15": dados[6],

        "over25": dados[7],

        "ambas_marcam": dados[8],

        "confianca": dados[9]

    }