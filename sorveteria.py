
# Cria um vetor para os sabores do sorvete
vetorSorvete = []

# Cria variável para armazenar a escolha
opEscolhida = 0

# Mostra mensagem de boas vindas
print(f'\nOlá :D Seja bem-vindo à sorveteria do LeLé!')

# Cria loop do menu
while opEscolhida != 4:

    # Armazena a escolha na variável
    opEscolhida = int(input('\n1 - Adicionar sabor\n2 - Remover sabor\n3 - Visualizar sorvete\n4 - Finalizar pedido\n\nEscolha uma opção: '))

    # Usa estrutura de seleção match/case na variável
    match opEscolhida:

        # Caso opção 1 (adicionar)
        case 1:

            # Verifica se o sorvete não está no limite de sabores
            if len(vetorSorvete) < 4:

                # Recebe e armazena o sabor a ser adicionado
                saborAdd = (input(f'Digite o {len(vetorSorvete) + 1}º sabor do sorvete: ')).upper()
                
                # Adiciona o sabor no vetor de sabores
                vetorSorvete.append(saborAdd)

                # Mostra ao usuário mensagem de sabor adicionado
                print(f'O sabor {saborAdd} foi adicionado! :D')

            # Caso o sorvete já esteja com o limite de sabores
            else:

                # Mostra ao usuário mensagem de limite de sabores atingido
                print(f'Limite de sabores atingido, remova um sabor para poder adicionar!')

        # Caso opção 2 (remover)
        case 2:

            # Verifica se o sorvete já possui sabores
            if len(vetorSorvete) > 0:

                # Recebe e armazena o sabor a ser removido
                saborRemover = (input(f'Digite o sabor a ser removido: ')).upper()

                # Percorre o vetor de sabores 
                if saborRemover in vetorSorvete:

                    # Armazena o índice do sabor a ser removido
                    indice = vetorSorvete.index(saborRemover)

                    # Verifica se o índice corresponde à ultima posição do vetor
                    if indice == (len(vetorSorvete) - 1):  

                        # Remove o sabor da última posição
                        vetorSorvete.pop(indice)

                        # Mostra ao usuário mensagem de sabor removido
                        print(f'O sabor {saborRemover} foi removido! :)')

                    else:

                        # Mostra ao usuário mensagem de sabor não está na última camada
                        print(f'\n O sabor{saborRemover} está na {indice + 1}ª camada.\nNão é possível remover o sabor, pois ele não está na última camada! :T')
                
                # Caso o sabor não seja encontrado no sorvete
                else:

                    # Mostra ao usuário mensagem de sabor não encontrado
                    print(f'O sabor {saborRemover} não está no sorvete! :T')

            # Caso o sorvete ainda não possua sabores
            else:

                # Mostra ao usuário mensagem de sorvete ainda não possui sabores
                print(f'\nNão é possível remover, pois o seu sorvete ainda não possui sabores! :T\n')

        # Caso opção 3 (visualizar)
        case 3:

            # Verifica se o sorvete já possui sabores
            if len(vetorSorvete) > 0:

                # Mostra ao usuário os sabores atuais do sorvete
                print(f'Seu sorvete possui atualmente esses sabores: {vetorSorvete}')

            # Caso o sorvete ainda não possua sabores
            else:

                # Mostra ao usuário mensagem de sorvete ainda sem sabores
                print(f'\nSeu sorvete ainda não possui sabores! ^^\n')

        # Caso opção 4 (finalizar)
        case 4:

            # Verifica se o sorvete já possui sabores
            if len(vetorSorvete) > 0:

                # Mostra ao usuário mensagem de pedido finalizado e os sabores
                print(f'\nPedido finalizado! Seu sorvete: {vetorSorvete}')

            # Caso o sorvete ainda não possua sabores
            else:

                # Mostra ao usuário mensagem de sorvete ainda sem sabores
                print(f'\nO seu sorvete não possui sabores. Adicione pelo menos um sabor! :)\n')

                # Reinicia opção para 0 mantendo o loop
                opEscolhida = 0

        # Caso não seja nenhuma das opções 1, 2, 3, 4
        case _:

            # Mostra ao usuário mensagem de opção inválida
            print(f'\nOpção inválida! >.<\n')