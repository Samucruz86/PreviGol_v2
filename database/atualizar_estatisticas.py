"""
Atualização de estatísticas das equipas
PreviGol v2.2
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
                "jogos":0,
                "marcados":0,
                "sofridos":0,
                "casa_marcados":[],
                "casa_sofridos":[],
                "fora_marcados":[],
                "fora_sofridos":[]
            }



        if fora not in equipas:

            equipas[fora] = {
                "jogos":0,
                "marcados":0,
                "sofridos":0,
                "casa_marcados":[],
                "casa_sofridos":[],
                "fora_marcados":[],
                "fora_sofridos":[]
            }



        # Casa

        equipas[casa]["jogos"] += 1

        equipas[casa]["marcados"] += gc

        equipas[casa]["sofridos"] += gf


        equipas[casa]["casa_marcados"].append(gc)

        equipas[casa]["casa_sofridos"].append(gf)



        # Fora

        equipas[fora]["jogos"] += 1

        equipas[fora]["marcados"] += gf

        equipas[fora]["sofridos"] += gc


        equipas[fora]["fora_marcados"].append(gf)

        equipas[fora]["fora_sofridos"].append(gc)



    for equipa,dados in equipas.items():


        media_marcados_casa = (
            sum(dados["casa_marcados"]) /
            len(dados["casa_marcados"])
            if dados["casa_marcados"]
            else 0
        )


        media_sofridos_casa = (
            sum(dados["casa_sofridos"]) /
            len(dados["casa_sofridos"])
            if dados["casa_sofridos"]
            else 0
        )


        media_marcados_fora = (
            sum(dados["fora_marcados"]) /
            len(dados["fora_marcados"])
            if dados["fora_marcados"]
            else 0
        )


        media_sofridos_fora = (
            sum(dados["fora_sofridos"]) /
            len(dados["fora_sofridos"])
            if dados["fora_sofridos"]
            else 0
        )


        forma = round(
            (dados["marcados"] + 1) /
            (dados["sofridos"] + 1),
            2
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

        VALUES (?,?,?,?,?,?,?,?,?,?,?)

        ON CONFLICT(equipa)

        DO UPDATE SET

        jogos=excluded.jogos,
        golos_marcados=excluded.golos_marcados,
        golos_sofridos=excluded.golos_sofridos,
        media_casa=excluded.media_casa,
        media_fora=excluded.media_fora,
        media_marcados_casa=excluded.media_marcados_casa,
        media_sofridos_casa=excluded.media_sofridos_casa,
        media_marcados_fora=excluded.media_marcados_fora,
        media_sofridos_fora=excluded.media_sofridos_fora,
        forma=excluded.forma

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

            forma
        ))



    conn.commit()

    conn.close()


    print(
        f"{len(equipas)} equipas atualizadas."
    )



if __name__ == "__main__":

    atualizar_estatisticas()