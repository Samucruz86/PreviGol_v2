"""
Atualização de estatísticas das equipas
PreviGol v0.9.0
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


    for casa, fora, gc, gf in jogos:


        if casa not in equipas:

            equipas[casa] = {

                "jogos": 0,

                "marcados": 0,

                "sofridos": 0,

                "marcados_casa": [],
                "sofridos_casa": [],

                "marcados_fora": [],
                "sofridos_fora": []

            }



        if fora not in equipas:

            equipas[fora] = {

                "jogos": 0,

                "marcados": 0,

                "sofridos": 0,

                "marcados_casa": [],
                "sofridos_casa": [],

                "marcados_fora": [],
                "sofridos_fora": []

            }



        # equipa da casa

        equipas[casa]["jogos"] += 1

        equipas[casa]["marcados"] += gc

        equipas[casa]["sofridos"] += gf


        equipas[casa]["marcados_casa"].append(gc)

        equipas[casa]["sofridos_casa"].append(gf)



        # equipa visitante

        equipas[fora]["jogos"] += 1

        equipas[fora]["marcados"] += gf

        equipas[fora]["sofridos"] += gc


        equipas[fora]["marcados_fora"].append(gf)

        equipas[fora]["sofridos_fora"].append(gc)



    for equipa, dados in equipas.items():


        media_marcados_casa = (
            sum(dados["marcados_casa"]) /
            len(dados["marcados_casa"])
            if dados["marcados_casa"]
            else 0
        )


        media_sofridos_casa = (
            sum(dados["sofridos_casa"]) /
            len(dados["sofridos_casa"])
            if dados["sofridos_casa"]
            else 0
        )


        media_marcados_fora = (
            sum(dados["marcados_fora"]) /
            len(dados["marcados_fora"])
            if dados["marcados_fora"]
            else 0
        )


        media_sofridos_fora = (
            sum(dados["sofridos_fora"]) /
            len(dados["sofridos_fora"])
            if dados["sofridos_fora"]
            else 0
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
                media_marcados_casa,
                media_sofridos_casa,
                media_marcados_fora,
                media_sofridos_fora,
                forma
            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)


            ON CONFLICT(equipa)

            DO UPDATE SET

                jogos=excluded.jogos,

                golos_marcados=excluded.golos_marcados,

                golos_sofridos=excluded.golos_sofridos,

                media_casa=excluded.media_casa,

                media_fora=excluded.media_fora,

                media_marcados_casa=
                    excluded.media_marcados_casa,

                media_sofridos_casa=
                    excluded.media_sofridos_casa,

                media_marcados_fora=
                    excluded.media_marcados_fora,

                media_sofridos_fora=
                    excluded.media_sofridos_fora

        """,
        (
            equipa,

            dados["jogos"],

            dados["marcados"],

            dados["sofridos"],

            media_marcados_casa,

            media_marcados_fora,

            media_marcados_casa,

            media_sofridos_casa,

            media_marcados_fora,

            media_sofridos_fora,

            0
        ))



    conn.commit()

    conn.close()


    print(
        f"{len(equipas)} equipas atualizadas."
    )



if __name__ == "__main__":

    atualizar_estatisticas()