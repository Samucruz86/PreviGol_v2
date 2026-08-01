"""
Teste do sistema de força das equipas
PreviGol v3.4.1
"""


import sqlite3

from previsao.forca_equipas import calcular_forca_equipa



DATABASE = "data/PreviGol.db"



def testar_forcas():

    conn = sqlite3.connect(
        DATABASE
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()


    cursor.execute("""
    SELECT *
    FROM estatisticas_equipas
    WHERE equipa IN (
        'Benfica',
        'FC Porto',
        'Sporting CP'
    )
    """)


    equipas = cursor.fetchall()


    conn.close()


    if not equipas:

        print(
            "Nenhuma equipa encontrada"
        )

        return


    print(
        "\n=== TESTE FORÇA DAS EQUIPAS v3.4.1 ===\n"
    )


    for equipa in equipas:

        dados = dict(equipa)


        resultado = calcular_forca_equipa(
            dados
        )


        print(
            dados["equipa"]
        )

        print(
            resultado
        )

        print(
            "-" * 40
        )



if __name__ == "__main__":

    testar_forcas()