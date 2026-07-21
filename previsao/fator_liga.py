"""
Ajuste de força da competição
PreviGol v2
"""


def calcular_fator_liga(
    media_golos_liga,
    media_referencia=2.6
):
    """
    Calcula um fator de ajuste da liga.

    Ligas com mais golos aumentam o xG.
    Ligas com menos golos reduzem o xG.
    """

    if media_golos_liga <= 0:
        return 1.0


    fator = (
        media_golos_liga /
        media_referencia
    )


    # Limita valores extremos

    if fator < 0.75:
        fator = 0.75


    if fator > 1.25:
        fator = 1.25


    return round(
        fator,
        3
    )



def aplicar_fator_liga(
    xg_casa,
    xg_fora,
    fator
):
    """
    Aplica o ajuste da competição ao xG.
    """

    return {

        "xg_casa":
            round(
                xg_casa * fator,
                2
            ),

        "xg_fora":
            round(
                xg_fora * fator,
                2
            )

    }
