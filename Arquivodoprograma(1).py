def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguão of the old building",
            "descricao": "Voce esta no saguao de entrada do prédio um do insper",
            "opcoes": {
                "Casa do pão de queijo": "Ir até  casa do pão queijo, talvez comer algo?",
                "Prédio novo": "Ir de patinete da grin para rumo ao prédio de engenharia",
            }
        },
        "Prédio novo": {
            "titulo": "Onde a felicidade começa",
            "descricao": "Saguão do prédio novo:Onde todos entram e acham que serão felizes",
            "opcoes": {
                "inicio": "Voltar de patinete da yellow para o prédio antigo",
                "Fab lab": "Pegar elevador para ir ao fab lab",
				'segundo andar':'subir de escada para o segundo andar'
            }
        },
        "Fab lab": {
            "titulo": "Os QUATRO terrores",
            "descricao": "Um dos técnicos te fará vencer, já os outros...",
            "opcoes": {"Técnico da cortadora a laser": "Pra que a cortadora a laser serve?", 
					   'Técnico da fresadora':'O que a fresadora faz? ',
					   'Técnico de solda':'O que se aprende no job rotation de solda?', 
					   'Técnico da impressora 3d': 'O que se pode fazer com uma cortadora a laser?', 
					   'Prédio novo':'Pegar elevador para o térreo do prédio'}
        },
        'Casa do pão de queijo': {
            "titulo": "O cafezin da sorte",
            "descricao": "Você está na Casa do pão de queijo?",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada", 
				'Comprar pão de queijo':'Você tem dinheiro pra isso?'
            }
        },
		'Segundo andar': {
			'titulo': 'A hora da verdade',
			'descrição':'Acho que o professor está aqui',
			'opções':{'Prédio novo':'pegar elevador para o saguão do prédio de engenharia',
					  'descer no tobogã':'você consegue fazer isso?',
					  'sala do professor':'caminhe lentamente até a sala onde ele se encontra',
					  'Fab lab':'va de elevador ao Fab lab'
			}
				},
		'sala do professor': {
			'titulo':'O monstro está aqui',
			'desrição':'faça alguma coisa, ou vai arregar?',
			'opções':{'segundo andar':'Arregue agora',
			          'assuste o professor':'faça uma bricadeirinha sadia com ele',
					  'vá falar com o professor':'agora é a hora da verdade'}
			   }
	}
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
		   
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

