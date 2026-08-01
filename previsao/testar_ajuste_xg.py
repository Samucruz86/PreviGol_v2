"""
Teste ajuste inteligente de xG
PreviGol v3.5
"""


from previsao.ajuste_xg import ajustar_xg



def testar_jogo(
    casa,
    fora,
    xg_casa,
    xg_fora,
    forca_casa,
    forca_fora
):

    resultado = ajustar_xg(
        xg_casa,
        xg_fora,
        forca_casa,
        forca_fora
    )


    print("\n", casa, "vs", fora)

    print(
        "xG original:",
        xg_casa,
        "-",
        xg_fora
    )

    print(
        "Forças:",
        forca_casa,
        "-",
        forca_fora
    )

    print(
        "xG ajustado:",
        resultado
    )



if __name__ == "__main__":


    testar_jogo(
        "Benfica",
        "FC Porto",
        1.8,
        1.2,
        85.83,
        77.33
    )


    testar_jogo(
        "Benfica",
        "Sporting CP",
        1.8,
        1.2,
        85.83,
        88.19
    )


    testar_jogo(
        "Benfica",
        "Estoril",
        2.6,
        0.71,
        85.83,
        60
    )