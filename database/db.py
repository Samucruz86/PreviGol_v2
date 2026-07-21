"""
Gestão da Base de Dados PreviGol v2
"""

import sqlite3
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)


os.makedirs(
    DATA_DIR,
    exist_ok=True
)


DATABASE = os.path.join(
    DATA_DIR,
    "PreviGol.db"
)



def ligar_bd():

    return sqlite3.connect(
        DATABASE
    )



def criar_tabelas():

    conn = ligar_bd()
    cursor = conn.cursor()


    # Equipas

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nome TEXT UNIQUE NOT NULL,

        liga TEXT,

        pais TEXT,

        elo REAL DEFAULT 1500

    )
    """)



    # Jogos

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        equipa_casa TEXT,

        equipa_fora TEXT,

        golos_casa INTEGER,

        golos_fora INTEGER,

        data TEXT,

        estado TEXT

    )
    """)



    # Estatísticas

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estatisticas_equipas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        equipa TEXT UNIQUE,

        jogos INTEGER DEFAULT 0,

        golos_marcados INTEGER DEFAULT 0,

        golos_sofridos INTEGER DEFAULT 0,

        media_casa REAL DEFAULT 0,

        media_fora REAL DEFAULT 0,

        forma REAL DEFAULT 0

    )
    """)



    # Previsões

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS previsoes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        equipa_casa TEXT,

        equipa_fora TEXT,

        xg_casa REAL,

        xg_fora REAL,

        resultado_previsto TEXT,

        over15 REAL,

        over25 REAL,

        ambas_marcam REAL,

        confianca REAL,

        mercado_recomendado TEXT,

        probabilidade_mercado REAL,

        comentario_analise TEXT

    )
    """)



    # Avaliações

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS avaliacao_previsoes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        previsao_id INTEGER,

        resultado_real TEXT,

        acertou INTEGER,

        acertou_over15 INTEGER,

        acertou_over25 INTEGER,

        acertou_ambas INTEGER

    )
    """)



    conn.commit()
    conn.close()



if __name__ == "__main__":

    criar_tabelas()

    print(
        "Base de dados PreviGol criada/verificada com sucesso"
    )