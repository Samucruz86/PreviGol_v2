"""
Sistema de força das equipas
PreviGol v3.4.1

Calcula:
- força ofensiva
- força defensiva
- força global

Sem alterar a base de dados.
"""


def limitar(valor, minimo=0, maximo=100):

    return round(
        max(min(valor, maximo), minimo),
        2
    )



def calcular_experiencia(jogos):

    if jogos >= 30:
        return 100

    elif jogos >= 20:
        return 80

    elif jogos >= 10:
        return 60

    else:
        return 40



def calcular_forca_ofensiva(dados):

    jogos = dados.get("jogos", 0)

    marcados = dados.get(
        "golos_marcados",
        0
    )

    media_golos = (
        marcados / jogos
        if jogos > 0
        else 0
    )


    forma = dados.get(
        "forma",
        1
    )


    experiencia = calcular_experiencia(
        jogos
    )


    ataque = (

        (media_golos / 3 * 50)

        +

        (forma / 3 * 30)

        +

        (experiencia * 0.20)

    )


    return limitar(ataque)



def calcular_forca_defensiva(dados):

    jogos = dados.get("jogos", 0)

    sofridos = dados.get(
        "golos_sofridos",
        0
    )


    media_sofridos = (

        sofridos / jogos

        if jogos > 0

        else 0

    )


    media_casa = dados.get(
        "media_sofridos_casa",
        media_sofridos
    )


    media_fora = dados.get(
        "media_sofridos_fora",
        media_sofridos
    )


    experiencia = calcular_experiencia(
        jogos
    )


    defesa = (

        ((3 - media_sofridos)
        /
        3
        *
        60)

        +

        ((3 - ((media_casa + media_fora) / 2))
        /
        3
        *
        20)

        +

        (experiencia * 0.20)

    )


    return limitar(defesa)



def calcular_forca_equipa(dados):


    ataque = calcular_forca_ofensiva(
        dados
    )


    defesa = calcular_forca_defensiva(
        dados
    )


    experiencia = calcular_experiencia(
        dados.get("jogos", 0)
    )


    forca_global = (

        ataque * 0.45

        +

        defesa * 0.45

        +

        experiencia * 0.10

    )


    return {

        "ataque": ataque,

        "defesa": defesa,

        "forca_global": limitar(
            forca_global
        )

    }