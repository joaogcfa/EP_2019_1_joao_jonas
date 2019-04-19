# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Jonas da Silva Lopes, jonasl1@al.insper.edu.br
# - aluno B: João Guilherme Almeida, joaogcfa@al.insper.edu.br

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    
    print("The Fox Tale")
    print("------------")
    print()
    print("'Amanhã eu faço', você dizia. 'Deixa pra outro dia'... e adiou, adiou."
          " Chegou o dia da entrega do EP e você, raposão aluno insper,"
          " não fez a entrega POR PREGUIÇA ")
    print()
    print('Mas ainda há esperança. Assuste-se, você tem pouco tempo, mas tem tempo')
    print()
    print("Você está na entrada do Insper e terá que fazer as escolhas certas para poder"
          " conseguir convencer o professor a adiar o temido EP")
    print()

    cenario, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenario[nome_cenario_atual]
        
        for titulo,sala in cenario_atual.items():
            if titulo== 'titulo':
                print(sala)
                print('-'*len(sala))
                print()
                for titulo,sala in cenario_atual.items():
                    if titulo== 'descricao':
                        print(sala)
                        print()

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            for cenario, descricao in opcoes.items():
                print('{0}: {1}'. format(cenario, descricao))
            escolha = input("o que você quer fazer?")
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
