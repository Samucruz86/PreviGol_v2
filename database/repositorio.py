"""
Repositório de acesso à base de dados
PreviGol v3.0
"""

from database.db import ligar_bd



def obter_estatisticas_equipa(equipa):

    conn = ligar_bd()
    cursor = conn.cursor()

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
            (f"%{equipa}%",)
        )

        dados = cursor.fetchone()


    conn.close()


    if not dados:

        return {

            "dados_validos": False,

            "jogos": 0,
            "golos_marcados": 0,
            "golos_sofridos": 0,

            "media_casa": 0,
            "media_fora": 0,

            "forma": 0,

            "media_marcados_casa": 0,
            "media_sofridos_casa": 0,

            "media_marcados_fora": 0,
            "media_sofridos_fora": 0

        }


    return {

        "dados_validos": True,

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
            confianca,
            mercado_recomendado,
            probabilidade_mercado,
            comentario_analise
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """,

        (

            previsao.get("equipa_casa"),

            previsao.get("equipa_fora"),

            previsao.get("xg_casa"),

            previsao.get("xg_fora"),

            previsao.get("resultado_previsto"),

            previsao.get("over15"),

            previsao.get("over25"),

            previsao.get("ambas_marcam"),

            previsao.get("confianca"),

            previsao.get("mercado_recomendado"),

            previsao.get("probabilidade_mercado"),

            previsao.get("comentario_analise")

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

        WHERE equipa_casa = ?

        AND equipa_fora = ?

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

        WHERE equipa_casa = ?

        AND equipa_fora = ?

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

        "confianca": dados[9],

        "mercado_recomendado": dados[10],

        "probabilidade_mercado": dados[11],

        "comentario_analise": dados[12]

    }

def obter_previsoes_pendentes():

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *

        FROM previsoes

        ORDER BY id ASC

        """
    )


    dados = cursor.fetchall()


    conn.close()


    previsoes = []


    for linha in dados:

        previsoes.append({

            "id": linha[0],

            "equipa_casa": linha[1],

            "equipa_fora": linha[2],

            "xg_casa": linha[3],

            "xg_fora": linha[4],

            "resultado_previsto": linha[5],

            "over15": linha[6],

            "over25": linha[7],

            "ambas_marcam": linha[8],

            "confianca": linha[9],

            "mercado_recomendado": linha[10],

            "probabilidade_mercado": linha[11],

            "comentario_analise": linha[12]

        })


    return previsoes





def previsao_ja_avaliada(previsao_id):

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT id

        FROM avaliacao_previsoes

        WHERE previsao_id = ?

        """,

        (
            previsao_id,
        )

    )


    resultado = cursor.fetchone()


    conn.close()


    return resultado is not None





def guardar_avaliacao(avaliacao):

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO avaliacao_previsoes
        (

            previsao_id,

            resultado_real,

            acertou,

            acertou_over15,

            acertou_over25,

            acertou_ambas

        )

        VALUES (?, ?, ?, ?, ?, ?)

        """,

        (

            avaliacao["previsao_id"],

            avaliacao["resultado_real"],

            avaliacao["acertou"],

            avaliacao["acertou_over15"],

            avaliacao["acertou_over25"],

            avaliacao["acertou_ambas"]

        )

    )


    conn.commit()
    conn.close()

def obter_historico_previsoes():

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT

            p.id,

            p.equipa_casa,

            p.equipa_fora,

            p.resultado_previsto,

            a.resultado_real,

            a.acertou

        FROM previsoes p

        LEFT JOIN avaliacao_previsoes a

            ON p.id = a.previsao_id

        ORDER BY p.id
        """
    )


    dados = cursor.fetchall()


    conn.close()


    historico = []


    for linha in dados:

        historico.append(

            {

                "id": linha[0],

                "equipa_casa": linha[1],

                "equipa_fora": linha[2],

                "resultado_previsto": linha[3],

                "resultado_real": linha[4],

                "acertou": linha[5]

            }

        )


    return historico