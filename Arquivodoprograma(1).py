def carregar_cenarios():
    avatar=input("Qual é seu nome raposão?")
    cenarios = {
        "inicio": {
            "titulo": "Saguão of the old building",
            "descricao": "Você está no saguao de entrada do prédio velho",
            "opcoes": {
                "casa do pao de queijo": "Ir até  casa do pão queijo, talvez comer algo?",
                "predio novo": "Ir de patinete da grin para rumo ao prédio de engenharia",
				'o grande elevador': 'Sempre demorado, porém sempre nos leva instantaneamente'
            }
        },
        "predio novo": {
            "titulo": "Onde a felicidade começa",
            "descricao": "Saguão do prédio novo: Onde todos entram e acham que serão felizes",
            "opcoes": {
                "inicio": "Voltar de patinete da yellow para o prédio antigo",
                "fab lab": "Pegar elevador para ir ao fab lab",
				'segundo andar':'Subir de escada para o segundo andar'
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
			'opcoes':{'predio novo':'Pegar o elevador para o saguão do prédio de engenharia',
					  'descer no tobogã':'Você consegue fazer isso?',
					  'sala do professor':'caminhe lentamente até a sala onde ele se encontra',
					  'fab lab':'va de elevador ao Fab lab'
			}
				},
		'sala do professor': {
			'titulo':'O monstro está aqui',
			'descricao':'Vai fazer alguma coisa, ou vai arregar?',
			'opcoes':{'segundo andar':'Arregue agora',
			          'assustar o professor':'faça uma bricadeirinha sadia com ele',
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
            "descricao": "{0}: 100 hit points, 15 pontos de ataque e 10 pontos de defesa\n"
            "Caixa: 10 hit points, 5 pontos de ataque e 5 pontos de defesa".format(avatar),
            "opcoes": {
                "atacar caixa": "atacar o seu oponente",
                "fugir": "última chance de fugir",
            }
        },
        "atacar caixa": {
            "titulo": "Doce Vitória",
			'descricão': 'Você saiu na porrada com a atendente e não saiu no prejú',
            "descricao": "Parabéns, você venceu! Como forma de desculpa pelo caixa louco, a casa do Pão de queijo te deu o ataque do café quente, use sabiamente",
            "opcoes": {
                "inicio": "voltar para o saguão de entrada",
            }
        },
		'o grande elevador':{
			'titulo': 'Vai num flash',
			'descricao': 'O jeito mais rápido de se percorrer o espaço tempo, de forma quase segura',
			'opcoes':{
				'responder a pergunta':'teleporte-se para onde quiser',
				'inicio': 'Estas a perder uma grande oportunidade'	
					}
				},
        'tecnico da fresadora': {
            "titulo": "O técnico assassino",
            "descricao": "Você escolheu pobreamente, o que te fez cair em ruina",
            "opcoes": {
                "acabaram as opções":"Não há nada para se fazer"
            }
        },
        'tecnico da solda': {
            "titulo": "O técnico assassino",
            "descricao": "você escolheu pobreamente, o que te fez cair em ruina",
            "opcoes": {
                "acabaram as opções":"não há nada para se fazer"
            }
        },
        'tecnico da cortadora a laser': {
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
            "descricao": "{0}: 100 hit points, 15 pontos de ataque e 10 pontos de defesa\n"
            "Técnico: 1000 hit points, 25 pontos de ataque e 25 pontos de defesa".format(avatar),
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
        'ataque do cafe quente': {
            "titulo": "Doce vitória",
            "descricao": "Você ganhou do tecnico e agora como recompensa você ganhou o belissimo rabo da raposa, vindo diretamente da impressora 3d",
            "opcoes": {
                "predio novo":"Voltar para o hall do prédio novo",
            }
        },
        'assustar o professor': {
			'titulo':'O ataque assassino',
			'descricao':'Voce matou o professor',
			'opcoes':{'Você matou o professor':'Não há nada a se fazer',
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
    
#criar variáveis
    cenarios, nome_cenario_atual = carregar_cenarios()
    itens=['Você não tem itens']
    game_over = False
    game_win = False
    
# o jogo em si
    while not game_over and not game_win:
        cenario_atual = cenarios[nome_cenario_atual]
		
		# feature batalha na casa de pao de queijo
        if nome_cenario_atual == "atacar caixa":
            print()
            del itens[0]
            #feature itens
            itens.append("ataque do café quente")
            
        # perdendo no fab lab    
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
            print("Você escolheu probreamente, já que o técnico era na verdade um vilão que te matou com a cortadora laser")
            print()
            game_over = True
            break
        
        #batalha com tecnico
        if nome_cenario_atual == "atacar o tecnico":
            print()
            print("Você claramente não tinha chance e mesmo assim atacou... bem, você perdeu")
            print()
            game_over = True
            break
        
        #ganhando do tecnico
        if nome_cenario_atual == "ataque do cafe quente":
            if itens[0]=='ataque do café quente':
                del itens[0]
                itens.append('rabo da raposa louca')
            else:
                print()
                print('Você não tem o ataque do café quente seu bobo')
                game_over=True
                break
            
        #ganhar o jogo assustando o professor
        if nome_cenario_atual == "assustar o professor":
            print()
            print('Parabéns, você ganhou o jogo, já que o professor morreu de ataque cardíaco e não tem mais entrega de EP, mas você foi preso...')
            game_win=True
            break


        #Apresentação do cenário
        for titulo,sala in cenario_atual.items():
            if titulo == 'titulo':
                print()
                print(sala)
                print('-'*len(sala))
                print()
                print("Você tem esses itens: ", end = '')
                print()
                for i in itens:
                    print(i, end = '')
                    print()
                    print()
                for descricao,texto in cenario_atual.items():
                    if descricao == 'descricao':
                        print(texto)
                print()                                


        #Interação com o usuário
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
			
        else:
            for cenario, descricao in opcoes.items():
                print('{0}: {1}'. format(cenario, descricao))
            escolha = input("o que você quer fazer?")
            
            #feature transporte
            if escolha == 'responder a pergunta':
               nome_cenario_atual=input('Escolha qualquer lugar do mundo ')
               if nome_cenario_atual in cenarios:
                  nome_cenario_atual=nome_cenario_atual
               else:
                print("essa opção não existe, tente novamente")
                escolha=input("o que você quer fazer?")
                nome_cenario_atual = escolha
                
            #ir para cenário    
            elif escolha in opcoes:
                nome_cenario_atual = escolha
            while escolha not in opcoes:
                print("essa opção não existe, tente novamente")
                escolha=input("o que você quer fazer?")
                nome_cenario_atual = escolha
                
    #ganhando ou perdendo o jogo            
    if game_over==True:
        print("Você morreu!")
    elif game_win==True:
        print("Você venceu!")


# Programa principal.
if __name__ == "__main__":
    main()

