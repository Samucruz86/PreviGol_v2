"""
PreviGol v2.1
Sistema de previsão de golos
"""

from previsao.motor import gerar_previsao
from previsao.gerador_diario import gerar_previsoes_diarias


def menu():

    while True:

        print("\n====================")
        print("      PreviGol v2.1")
        print("====================")

        print("1 - Gerar previsão manual")
        print("2 - Gerar previsões do dia")
        print("3 - Sair")


        opcao = input("\nEscolha uma opção: ")


        if opcao == "1":

            casa = input("Equipa da casa: ")
            fora = input("Equipa visitante: ")


            resultado = gerar_previsao(
                casa,
                fora
            )


            print("\nRESULTADO")
            print(resultado)



        elif opcao == "2":

            gerar_previsoes_diarias()



        elif opcao == "3":

            print("A terminar PreviGol...")
            break



        else:

            print("Opção inválida.")



if __name__ == "__main__":

    menu()