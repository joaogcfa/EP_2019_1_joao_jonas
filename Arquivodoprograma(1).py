def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguão of the old building",
            "descricao": "Voce esta no saguao de entrada do prédio um do insper",
            "opcoes": {
                "casa do pao de queijo": "Ir até  casa do pão queijo, talvez comer algo?",
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
					   'Técnico da impressora 3d': 'O que se pode fazer com uma impressora 3d?', 
					   'Prédio novo':'Pegar elevador para o térreo do prédio'}
        },
        'casa do pao de queijo': {
            "titulo": "O cafezin da sorte",
            "descricao": "Você está na Casa do pão de queijo",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada", 
				'comprar pao de queijo':'Você tem dinheiro pra isso?'
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
			   },
        "comprar pao de queijo": {
            "titulo": "Hora da batalha",
            "descricao": "Quando você foi comprar seu pão de queijo, você irritou a caixa e agora ela está te desafiando para uma batalha 1 contra 1",
            "opcoes": {
                "incio": "Você é um medroso que fugirá de suas batalhas e voltará para o saguão de entrada",
                "Lutar": "Iniciar sua batlha",
            }
        },
        "Lutar": {
            "titulo": "Sua batalha começou",
            "descricao": "Você: 100 hit points, 15 pontos de ataque e 10 pontos de defesa"
            "Caixa: 10 hit points, 5 pontos de ataque e 5 pontos de defesa",
            "opcoes": {
                "atacar caixa": "Atacar o seu oponente",
                "fugir": "última chance de fugir",
            }
        },
        "atacar caixa": {
            "titulo": "Doce Vitória",
            "descricao": "Parabéns, você venceu! Como forma de desculpa pelo caixa louco, a casa do Pão de queijo te deu o ataque do café quente, use sabiamente",
            "opcoes": {
                "inicio": "Voltar para o saguão de entrada",
            }
        },
        
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
    avatar=input("Qual é seu nome raposão?")

    cenarios, nome_cenario_atual = carregar_cenarios()
    itens=[]
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        if nome_cenario_atual== "atacar caixa":
            itens.append("ataque do café quente")
        for titulo,sala in cenario_atual.items():
            if titulo== 'titulo':
                print()
                print(sala)
                print('-'*len(sala))
                print()
                print("você tem esses itens:",itens)
                for descricao,texto in cenario_atual.items():
                    if descricao== 'descricao':
                        print(texto)
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
                print("Sua indecisão te levou a ruína")
                game_over=True
                

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()

