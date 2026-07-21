"""
Atualização de estatísticas das equipas
PreviGol v0.8.0
"""

from database.db import ligar_bd



def atualizar_estatisticas():

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute("""
        SELECT
            equipa_casa,
            equipa_fora,
            golos_casa,
            golos_fora
        FROM jogos
        WHERE estado IN ('FT','AET','PEN')
    """)


    jogos = cursor.fetchall()


    equipas = {}


    for jogo in jogos:

        casa, fora, gc, gf = jogo


        if casa not in equipas:
            equipas[casa] = {
                "jogos": 0,
                "marcados": 0,
                "sofridos": 0,
                "casa": [],
                "fora": []
            }


        if fora not in equipas:
            equipas[fora] = {
                "jogos": 0,
                "marcados": 0,
                "sofridos": 0,
                "casa": [],
                "fora": []
            }


        equipas[casa]["jogos"] += 1
        equipas[casa]["marcados"] += gc
        equipas[casa]["sofridos"] += gf
        equipas[casa]["casa"].append(gc)


        equipas[fora]["jogos"] += 1
        equipas[fora]["marcados"] += gf
        equipas[fora]["sofridos"] += gc
        equipas[fora]["fora"].append(gf)



    for equipa, dados in equipas.items():

        media_casa = (
            sum(dados["casa"]) / len(dados["casa"])
            if dados["casa"] else 0
        )


        media_fora = (
            sum(dados["fora"]) / len(dados["fora"])
            if dados["fora"] else 0
        )


        cursor.execute("""
            INSERT INTO estatisticas_equipas
            (
                equipa,
                jogos,
                golos_marcados,
                golos_sofridos,
                media_casa,
                media_fora,
                forma
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)

            ON CONFLICT(equipa)
            DO UPDATE SET

                jogos=excluded.jogos,
                golos_marcados=excluded.golos_marcados,
                golos_sofridos=excluded.golos_sofridos,
                media_casa=excluded.media_casa,
                media_fora=excluded.media_fora

        """,
        (
            equipa,
            dados["jogos"],
            dados["marcados"],
            dados["sofridos"],
            media_casa,
            media_fora,
            0
        ))


    conn.commit()
    conn.close()


    print(
        f"{len(equipas)} equipas atualizadas."
    )



if __name__ == "__main__":

    atualizar_estatisticas()