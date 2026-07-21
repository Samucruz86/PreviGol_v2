"""
Estatísticas do modelo PreviGol
"""


from database.repositorio import ligar_bd



def obter_estatisticas():

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT
        COUNT(*),
        SUM(acertou),
        SUM(acertou_over15),
        SUM(acertou_over25),
        SUM(acertou_ambas)
    FROM avaliacao_previsoes
    """)


    dados = cursor.fetchone()


    conn.close()


    total = dados[0] or 0

    resultado = dados[1] or 0

    over15 = dados[2] or 0

    over25 = dados[3] or 0

    ambas = dados[4] or 0



    def percentagem(valor):

        if total == 0:
            return 0

        return round(
            (valor / total) * 100,
            2
        )



    return {

        "total_avaliacoes": total,

        "resultado_exato": percentagem(resultado),

        "over15": percentagem(over15),

        "over25": percentagem(over25),

        "ambas_marcam": percentagem(ambas)

    }