"""
Repositório de dados PreviGol v2
Gestão de consultas à base de dados
"""

from database.db import ligar_bd



def obter_estatisticas_equipa(equipa):
    """
    Obtém estatísticas de uma equipa.
    """

    conn = ligar_bd()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            golos_marcados,
            golos_sofridos,
            media_casa,
            media_fora,
            forma
        FROM estatisticas_equipas
        WHERE equipa = ?
        """,
        (equipa,)
    )

    dados = cursor.fetchone()

    conn.close()


    if dados:

        return {

            "golos_marcados":
                dados[0],

            "golos_sofridos":
                dados[1],

            "media_casa":
                dados[2],

            "media_fora":
                dados[3],

            "forma":
                dados[4]

        }


    # Valores neutros caso não exista equipa

    return {

        "golos_marcados": 1.5,

        "golos_sofridos": 1.2,

        "media_casa": 1.5,

        "media_fora": 1.2,

        "forma": 5

    }


def obter_ultimos_jogos(equipa, limite=5):
    """
    Obtém últimos jogos de uma equipa.
    """

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            equipa_casa,
            equipa_fora,
            golos_casa,
            golos_fora,
            data
        FROM jogos
        WHERE equipa_casa = ?
        OR equipa_fora = ?
        ORDER BY data DESC
        LIMIT ?
        """,
        (
            equipa,
            equipa,
            limite
        )
    )


    jogos = cursor.fetchall()

    conn.close()


    return jogos



def guardar_previsao(previsao):
    """
    Guarda uma previsão na base de dados.
    """

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
            previsao["equipa_casa"],
            previsao["equipa_fora"],
            previsao["xg_casa"],
            previsao["xg_fora"],
            previsao["resultado_previsto"],
            previsao["over15"],
            previsao["over25"],
            previsao["ambas_marcam"],
            previsao["confianca"],
            previsao["analise"]["mercado"],
            previsao["analise"]["probabilidade"],
            previsao["analise"]["comentario"]
        )
    )


    conn.commit()

    conn.close()

def previsao_ja_avaliada(previsao_id):

    conn = ligar_bd()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM avaliacao_previsoes
        WHERE previsao_id = ?
        """,
        (previsao_id,)
    )

    resultado = cursor.fetchone()

    conn.close()


    return resultado is not None


def guardar_avaliacao(avaliacao):
    """
    Guarda a avaliação de uma previsão.
    """

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

def obter_previsoes_pendentes():
    """
    Obtém previsões ainda sem avaliação.
    """

    conn = ligar_bd()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            equipa_casa,
            equipa_fora,
            resultado_previsto,
            over15,
            over25,
            ambas_marcam
        FROM previsoes
        WHERE id NOT IN (
            SELECT previsao_id
            FROM avaliacao_previsoes
        )
        """
    )

    dados = cursor.fetchall()

    conn.close()

    previsoes = []

    for linha in dados:

        previsoes.append(
            {
                "id": linha[0],
                "equipa_casa": linha[1],
                "equipa_fora": linha[2],
                "resultado_previsto": linha[3],
                "over15": linha[4],
                "over25": linha[5],
                "ambas_marcam": linha[6]
            }
        )

    return previsoes