"""
Ligação à API-Football
PreviGol v0.7.2
"""

import os
import sys
import requests


# Permite importar ficheiros da raiz do projeto

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from config import API



def testar_ligacao():
    """
    Testa a ligação à API-Football.
    """

    url = API["url"] + "/status"


    headers = {

        "x-apisports-key": API["key"]

    }


    resposta = requests.get(
        url,
        headers=headers
    )


    return resposta.json()



def obter_jogos(data):
    """
    Obtém jogos de uma determinada data.
    """

    url = API["url"] + "/fixtures"


    headers = {

        "x-apisports-key": API["key"]

    }


    parametros = {

        "date": data

    }


    resposta = requests.get(
        url,
        headers=headers,
        params=parametros
    )


    return resposta.json()



if __name__ == "__main__":


    print("Teste de ligação API:")
    
    estado = testar_ligacao()

    print(estado)


    print("\nJogos do dia:")

    jogos = obter_jogos(
        "2026-07-21"
    )

    print(jogos)