"""
Cálculo Expected Goals (xG)
PreviGol v2.9.4

Melhorias:
- regressão à média
- peso bayesiano por número de jogos
- proteção contra amostras pequenas
- vantagem casa ajustada
- controlo de ataques extremos
- ajuste de forma
- limites realistas
"""


def limitar(valor, minimo, maximo):

    return max(
        minimo,
        min(valor, maximo)
    )



def ajustar_amostra(
    valor,
    jogos,
    media_liga
):

    """
    Reduz impacto de equipas
    com poucas partidas.

    Mais jogos = mais confiança.
    """

    peso = jogos / (jogos + 10)


    return (

        valor * peso

        +

        media_liga * (1 - peso)

    )



def calcular_xg(

    media_marcados_casa,

    media_sofridos_casa,

    media_marcados_fora,

    media_sofridos_fora,

    forma_casa,

    forma_fora,

    jogos_casa=20,

    jogos_fora=20,

    media_liga=1.45

):


    # ==========================
    # Ajuste por amostra
    # ==========================


    ataque_casa = ajustar_amostra(

        media_marcados_casa,

        jogos_casa,

        media_liga

    )


    defesa_casa = ajustar_amostra(

        media_sofridos_casa,

        jogos_casa,

        media_liga

    )


    ataque_fora = ajustar_amostra(

        media_marcados_fora,

        jogos_fora,

        media_liga

    )


    defesa_fora = ajustar_amostra(

        media_sofridos_fora,

        jogos_fora,

        media_liga

    )



    # ==========================
    # Forças relativas
    # ==========================


    forca_ataque_casa = ataque_casa / media_liga

    forca_ataque_casa *= 0.95


    forca_defesa_fora = defesa_fora / media_liga



    forca_ataque_fora = ataque_fora / media_liga

    forca_ataque_fora *= 0.95


    forca_defesa_casa = defesa_casa / media_liga



    # ==========================
    # xG base
    # ==========================


    xg_casa = (

        forca_ataque_casa

        *

        forca_defesa_fora

        *

        media_liga

    )


    xg_fora = (

        forca_ataque_fora

        *

        forca_defesa_casa

        *

        media_liga

        *

        0.85

    )



    # ==========================
    # vantagem casa
    # ==========================


    xg_casa *= 1.05



    # ==========================
    # Forma recente
    # ==========================


    xg_casa += (

        forma_casa - 3

    ) * 0.03



    xg_fora += (

        forma_fora - 3

    ) * 0.03



    # ==========================
    # Limites realistas
    # ==========================


    xg_casa = limitar(

        round(xg_casa, 2),

        0.30,

        2.60

    )


    xg_fora = limitar(

        round(xg_fora, 2),

        0.30,

        2.30

    )



    return {

        "xg_casa": xg_casa,

        "xg_fora": xg_fora

    }