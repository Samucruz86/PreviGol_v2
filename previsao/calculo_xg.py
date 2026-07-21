"""
Cálculo de Expected Goals (xG)
PreviGol v2
"""


def limitar(valor, minimo=0.1, maximo=5.0):

    return max(minimo, min(valor, maximo))


def calcular_xg(
    media_casa_marcados,
    media_casa_sofridos,
    media_fora_marcados,
    media_fora_sofridos,
    forma_casa=0,
    forma_fora=0,
    fator_casa=1.10
):

    """
    Calcula o xG esperado de cada equipa.

    Entrada:
    - média golos marcados em casa
    - média golos sofridos em casa
    - média golos marcados fora
    - média golos sofridos fora
    - fator de forma

    Saída:
    {
        "xg_casa": valor,
        "xg_fora": valor
    }
    """


    ataque_casa = (
        media_casa_marcados +
        media_fora_sofridos
    ) / 2


    ataque_fora = (
        media_fora_marcados +
        media_casa_sofridos
    ) / 2


    xg_casa = (
        ataque_casa *
        fator_casa
    )


    xg_fora = ataque_fora


    # Pequeno ajuste pela forma recente

    xg_casa += forma_casa * 0.05

    xg_fora += forma_fora * 0.05


    return {

        "xg_casa": round(
            limitar(xg_casa),
            2
        ),

        "xg_fora": round(
            limitar(xg_fora),
            2
        )

    }
