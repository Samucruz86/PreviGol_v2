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

os.makedirs(DATA_DIR, exist_ok=True)


DATABASE = os.path.join(
    DATA_DIR,
    "PreviGol.db"
)


def ligar_bd():

    return sqlite3.connect(DATABASE)


def criar_tabelas():

    conn = ligar_bd()
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nome TEXT UNIQUE NOT NULL,

        liga TEXT,

        pais TEXT,

        elo REAL DEFAULT 1500

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        data TEXT,

        equipa_casa TEXT,

        equipa_fora TEXT,

        golos_casa INTEGER,

        golos_fora INTEGER,

        estado TEXT DEFAULT 'agendado'

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estatisticas_equipas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        equipa TEXT UNIQUE,

        jogos INTEGER DEFAULT 0,

        golos_marcados INTEGER DEFAULT 0,

        golos_sofridos INTEGER DEFAULT 0,

        media_marcados REAL DEFAULT 0,

        media_sofridos REAL DEFAULT 0,

        media_casa REAL DEFAULT 0,

        media_fora REAL DEFAULT 0,

        forma TEXT

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS previsoes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        jogo_id INTEGER,

        data_previsao TEXT,

        xg_casa REAL,

        xg_fora REAL,

        over15 REAL,

        over25 REAL,

        ambas_marcam REAL,

        resultado_previsto TEXT,

        confianca REAL

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS avaliacao_previsoes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        previsao_id INTEGER,

        resultado_real TEXT,

        acertou_resultado INTEGER,

        acertou_over25 INTEGER,

        acertou_ambas INTEGER

    )
    """)


    conn.commit()
    conn.close()


if __name__ == "__main__":

    criar_tabelas()

    print("Base de dados PreviGol criada com sucesso")
