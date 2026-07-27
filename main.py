"""
PreviGol v2.4
Sistema de previsão de golos
"""

from previsao.motor import gerar_previsao
from previsao.gerador_diario import gerar_previsoes_diarias

from previsao.processar_avaliacoes import avaliar_jogo

from previsao.estatisticas_modelo import obter_estatisticas

from previsao.aprendizagem import analisar_desempenho

from previsao.dashboard import mostrar_dashboard

from previsao.historico import mostrar_historico



def menu():

    while True:

        print("\n==========================")
        print("        PreviGol v2.4")
        print("==========================")

        print("1 - Gerar previsão manual")
        print("2 - Gerar previsões do dia")
        print("3 - Avaliar resultado de jogo")
        print("4 - Estatísticas do modelo")
        print("5 - Aprendizagem do modelo")
        print("6 - Dashboard Analytics")
        print("7 - Histórico de previsões")
        print("8 - Sair")


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

            previsao_id = int(

                input("ID da previsão: ")

            )


            resultado_real = input(

                "Resultado real (ex: 2-1): "

            )


            resultado = avaliar_jogo(

                previsao_id,

                resultado_real

            )


            print(resultado)



        elif opcao == "4":


            dados = obter_estatisticas()


            print("\nESTATÍSTICAS DO MODELO")
            print("======================")


            print(

                "Total avaliações:",

                dados["total_avaliacoes"]

            )


            print(

                "Resultado exato:",

                dados["resultado_exato"],

                "%"

            )


            print(

                "Over 1.5:",

                dados["over15"],

                "%"

            )


            print(

                "Over 2.5:",

                dados["over25"],

                "%"

            )


            print(

                "Ambas marcam:",

                dados["ambas_marcam"],

                "%"

            )



        elif opcao == "5":

            analisar_desempenho()



        elif opcao == "6":

            mostrar_dashboard()



        elif opcao == "7":

            mostrar_historico()



        elif opcao == "8":

            print(
                "A terminar PreviGol..."
            )

            break



        else:

            print(
                "Opção inválida."
            )



if __name__ == "__main__":

    menu()