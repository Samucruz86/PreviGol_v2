"""
Aprendizagem adaptativa de pesos
PreviGol v2.4
"""

import json
import os

from previsao.estatisticas_modelo import obter_estatisticas



FICHEIRO_PESOS = "data/pesos_modelo.json"



def calcular_pesos():

    estatisticas = obter_estatisticas()


    pesos = {

        "resultado":
            estatisticas["resultado_exato"] / 100,


        "over15":
            estatisticas["over15"] / 100,


        "over25":
            estatisticas["over25"] / 100,


        "ambas":
            estatisticas["ambas_marcam"] / 100

    }


    return pesos




def guardar_pesos():

    pesos = calcular_pesos()


    os.makedirs(
        "data",
        exist_ok=True
    )


    with open(
        FICHEIRO_PESOS,
        "w",
        encoding="utf-8"
    ) as ficheiro:

        json.dump(
            pesos,
            ficheiro,
            indent=4
        )


    return pesos




def carregar_pesos():

    if not os.path.exists(
        FICHEIRO_PESOS
    ):

        return None


    with open(
        FICHEIRO_PESOS,
        "r",
        encoding="utf-8"
    ) as ficheiro:

        return json.load(
            ficheiro
        )




if __name__ == "__main__":

    resultado = guardar_pesos()


    print(
        "Pesos atualizados:"
    )

    print(
        resultado
    )
