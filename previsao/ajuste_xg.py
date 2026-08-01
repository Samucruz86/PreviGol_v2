"""
Ajuste inteligente de xG
PreviGol v3.5

Ajusta xG com base na força relativa
das equipas.

Retorna também os fatores aplicados.
"""


def limitar(valor, minimo=0.1, maximo=5):

    return round(
        max(min(valor, maximo), minimo),
        2
    )



def calcular_fator_forca(
    forca_casa,
    forca_fora
):

    diferenca = (
        forca_casa - forca_fora
    )


    fator = 1 + (
        diferenca / 200
    )


    return round(
        fator,
        3
    )



def ajustar_xg(
    xg_casa,
    xg_fora,
    forca_casa,
    forca_fora
):

    fator_casa = calcular_fator_forca(
        forca_casa,
        forca_fora
    )


    fator_fora = calcular_fator_forca(
        forca_fora,
        forca_casa
    )


    novo_xg_casa = limitar(
        xg_casa * fator_casa
    )


    novo_xg_fora = limitar(
        xg_fora * fator_fora
    )


    return {

        "xg_casa_ajustado":
            novo_xg_casa,

        "xg_fora_ajustado":
            novo_xg_fora,

        "fator_casa":
            fator_casa,

        "fator_fora":
            fator_fora

    }