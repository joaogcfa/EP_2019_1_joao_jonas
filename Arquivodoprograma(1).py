def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguão of the old building",
            "descricao": "Voce esta no saguao de entrada do prédio um do insper",
            "opcoes": {
                "casa do pao de queijo": "Ir até  casa do pão queijo, talvez comer algo?",
                "predio novo": "Ir de patinete da grin para rumo ao prédio de engenharia",
				'O grande elevador': 'sempre demorado, porém sempre nos leva instantaneamente'
            }
        },
        "predio novo": {
            "titulo": "Onde a felicidade começa",
            "descricao": "Saguão do prédio novo:Onde todos entram e acham que serão felizes",
            "opcoes": {
                "inicio": "Voltar de patinete da yellow para o prédio antigo",
                "fab lab": "Pegar elevador para ir ao fab lab",
				'segundo andar':'subir de escada para o segundo andar'
            }
        },
        "fab lab": {
            "titulo": "Os QUATRO terrores",
            "descricao": "Um dos técnicos te fará vencer, já os outros...",
            "opcoes": {"tecnico da cortadora a laser": "Pra que a cortadora a laser serve?", 
					   'tecnico da fresadora':'O que a fresadora faz? ',
					   'tecnico de solda':'O que se aprende no job rotation de solda?', 
					   'tecnico da impressora 3d': 'O que se pode fazer com uma impressora 3d?', 
					   'predio novo':'Pegar elevador para o térreo do prédio'}
        },
        'casa do pao de queijo': {
            "titulo": "O cafezin da sorte",
            "descricao": "Você está na Casa do pão de queijo",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada", 
				'comprar pao de queijo':'Você tem dinheiro pra isso?'
            }
        },
		'segundo andar': {
			'titulo': 'A hora da verdade',
			'descrição':'Acho que o professor está aqui',
			'opções':{'predio novo':'pegar elevador para o saguão do prédio de engenharia',
					  'descer no tobogã':'você consegue fazer isso?',
					  'sala do professor':'caminhe lentamente até a sala onde ele se encontra',
					  'fab lab':'va de elevador ao Fab lab'
			}
				},
		'sala do professor': {
			'titulo':'O monstro está aqui',
			'desrição':'faça alguma coisa, ou vai arregar?',
			'opções':{'segundo andar':'Arregue agora',
			          'assuste o professor':'faça uma bricadeirinha sadia com ele',
					  'va falar com o professor':'agora é a hora da verdade'}
			   },
        "comprar pao de queijo": {
            "titulo": "Hora da batalha",
            "descricao": "Quando você foi comprar seu pão de queijo, você irritou a caixa e agora ela está te desafiando para uma batalha 1 contra 1",
            "opcoes": {
                "incio": "Você é um medroso que fugirá de suas batalhas e voltará para o saguão de entrada",
                "lutar": "Iniciar sua batlha",
            }
        },
        "lutar": {
            "titulo": "Sua batalha começou",
            "descricao": "Você: 100 hit points, 15 pontos de ataque e 10 pontos de defesa\n"
            "Caixa: 10 hit points, 5 pontos de ataque e 5 pontos de defesa",
            "opcoes": {
                "atacar caixa": "atacar o seu oponente",
                "fugir": "última chance de fugir",
            }
        },
        "atacar caixa": {
            "titulo": "Doce Vitória",
            "descricao": "Parabéns, você venceu! Como forma de desculpa pelo caixa louco, a casa do Pão de queijo te deu o ataque do café quente, use sabiamente",
            "opcoes": {
                "inicio": "voltar para o saguão de entrada",
            }
        },
		'O grande elevador':{
			'titulo': 'Vai num flash',
			'Descrição': 'O jeito mais rápido de se percorrer o espaço tempo, de forma quase segura',
			'opcoes':{
				'responder a pergunta':'teleporte-se para onde quiser',
				'voltar ao saguão': 'Estas a perder uma grande oportunidade'	
					}
				},
        'tecnico da fresadora': {
            "titulo": "O técnico assassino",
            "descricao": "você escolheu pobreamente, o que te fez cair em ruina",
            "opcoes": {
                "acabaram as opções":"não há nada para se fazer"
            }
        },
        'tecnico da solda': {
            "titulo": "O técnico assassino",
            "descricao": "você escolheu pobreamente, o que te fez cair em ruina",
            "opcoes": {
                "acabaram as opções":"não há nada para se fazer"
            }
        },
        'tecnico da cortadora laser': {
            "titulo": "",
            "descricao": "você escolheu pobreamente, o que te fez cair em ruina",
            "opcoes": {
                "acabaram as opções":"não há nada para se fazer"
            }
        },
        'tecnico da impressora 3d': {
            "titulo": "O técnico maluco",
            "descricao": "O técnico escolhido ficou indignado que vc não consguiu fazer o EP para hoje e está te desafiando a uma batalha para lhe dar uma lição",
            "opcoes": {
                "predio novo":"você ficou com medo do que ele poderia fazer e quais armas ele poderia ter feito na impressora 3D",
                "lutar com o tecnico":"desafiar o tecnico"
            }
        },
        'lutar com o tecnico': {
            "titulo": "A batalha",
            "descricao": "Você: 100 hit points, 15 pontos de ataque e 10 pontos de defesa\n"
            "Caixa: 1000 hit points, 25 pontos de ataque e 25 pontos de defesa",
            "opcoes": {
                "predio novo":"você ficou com medo do que ele poderia fazer",
                "atacar o tecnico":"desafiar o tecnico",
                "ataque do cafe quente": "usar o ataque do café quente"
            }
        },
        'atacar o tecnico': {
            "titulo": "",
            "descricao": "você escolheu pobreamente, o que te fez cair em ruina",
            "opcoes": {
                "acabaram as opções":"não há nada para se fazer"
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
		
		
        if nome_cenario_atual == "atacar caixa":
            print('Você saiu na porrada com a atendente e não saiu no prejú')
            itens.append("ataque do café quente")
        if nome_cenario_atual == "tecnico da fresadora":
            print()
            print("Você escolheu probreamente, já que o técnico era na verdade um vilão que te matou com a fresadora")
            print()
            game_over = True
            break
        if nome_cenario_atual == "tecnico da solda":
            print()
            print("Você escolheu probreamente, já que o técnico era na verdade um vilão que te matou com a solda")
            print()
            game_over = True
            break
        if nome_cenario_atual == "tecnico da cortadora a laser":
            print()
            print("Você escolheu probreamente, já que o técnico era na verdade um vilão que te matou com a cortadora laiser")
            print()
            game_over = True
            break
        if nome_cenario_atual == "tecnico da cortadora a laser":
            print()
            print("Você escolheu probreamente, já que o técnico era na verdade um vilão que te matou com a cortadora laiser")
            print()
            game_over = True
            break        
#parte do teleporte, dá uma verificada se vai, também adicionei o cenário do elevador			
        elif cenario_atual == 'O grande elevador':
            for opção in cenario_atual['opcoes']:
               if opção == 'responder a pergunta':
                  nome_cenario_atual=input('fale o lugar pra onde quer ir')
                  if nome_cenario_atual != "inicio" or "Prédio novo" or "Fab lab" or 'casa do pao de queijo' or 'Segundo andar' or 'sala do professor': 
                      print('Você se teleportou para um lugar que não existe nessa dimensão e se perdeu no espaço tempo, parabéns pela burrice!!!') 
                      game_over=True
					   
        for titulo,sala in cenario_atual.items():
            if titulo == 'titulo':
                print()
                print(sala)
                print('-'*len(sala))
                print()
                print("voce tem esses itens:", end = '')
                for i in itens:
                    print(i, end = '')
                print()
                for descricao,texto in cenario_atual.items():
                    if descricao == 'descricao':
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
                print("Demoro, se FERRO, não foi dessa vez irmão")
                game_over=True
                

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()

