"""
Ligação API-Football
PreviGol v2.2

Responsável por:
- testar ligação API
- obter jogos por data
- obter jogos por liga
- preparar dados para o atualizador
"""

import os
import sys
import requests


# Permite importar config a partir da raiz do projeto

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from config import API



def criar_headers():
    """
    Cria cabeçalhos da API.
    """

    return {

        "x-apisports-key":
            API["key"]

    }



def testar_ligacao():
    """
    Testa estado da conta API.
    """

    url = (
        API["url"]
        +
        "/status"
    )


    resposta = requests.get(
        url,
        headers=criar_headers()
    )


    return resposta.json()



def obter_jogos_data(
    data
):
    """
    Obtém todos os jogos de uma data.
    """

    url = (
        API["url"]
        +
        "/fixtures"
    )


    parametros = {

        "date":
            data

    }


    resposta = requests.get(

        url,

        headers=criar_headers(),

        params=parametros

    )


    return resposta.json()



def obter_jogos_liga(
    liga,
    temporada
):
    """
    Obtém jogos de uma liga
    numa determinada época.
    """

    url = (
        API["url"]
        +
        "/fixtures"
    )


    parametros = {

        "league":
            liga,

        "season":
            temporada

    }


    resposta = requests.get(

        url,

        headers=criar_headers(),

        params=parametros

    )


    return resposta.json()



def obter_proximos_jogos_liga(
    liga,
    temporada
):
    """
    Obtém próximos jogos de uma liga.
    """

    url = (
        API["url"]
        +
        "/fixtures"
    )


    parametros = {

        "league":
            liga,

        "season":
            temporada,

        "next":
            20

    }


    resposta = requests.get(

        url,

        headers=criar_headers(),

        params=parametros

    )


    return resposta.json()



def contar_resultados(
    resposta
):

    if not resposta:

        return 0


    if "response" not in resposta:

        return 0


    return len(
        resposta["response"]
    )





if __name__ == "__main__":


    print(
        "\n=========================="
    )

    print(
        " TESTE ÉPOCAS PORTUGAL"
    )

    print(
        "==========================\n"
    )


    for temporada in range(2022, 2027):


        jogos = obter_jogos_liga(

            94,

            temporada

        )


        total = contar_resultados(
            jogos
        )


        print(
            f"Época {temporada}: {total} jogos"
        )