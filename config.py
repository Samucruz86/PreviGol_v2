import os


# Diretório principal do projeto

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# Base de dados

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

DATABASE = os.path.join(
    DATA_DIR,
    "PreviGol.db"
)


# Configuração do modelo

MODELO = {

    "max_golos_simulacao": 6,

    "peso_casa": 1.10,

    "peso_forma": 0.20,

    "peso_elo": 0.15,

    "peso_liga": 0.10

}


# Telegram

TELEGRAM = {

    "token": os.getenv(
        "TELEGRAM_TOKEN",
        ""
    )

}


# Ligas iniciais

LIGAS_SUPORTADAS = [

    "Portugal",

    "Espanha",

    "Inglaterra",

    "Alemanha",

    "Itália",

    "França"

]
