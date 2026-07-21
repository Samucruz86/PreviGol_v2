"""
Ligação à API-Football
PreviGol v0.7
"""

import os
import sys
import requests


# permite importar ficheiros da raiz do projeto

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from config import API



def testar_ligacao():

    url = API["url"] + "/status"


    headers = {

        "x-apisports-key": API["key"]

    }


    resposta = requests.get(
        url,
        headers=headers
    )


    return resposta.json()



if __name__ == "__main__":

    resultado = testar_ligacao()

    print(resultado)