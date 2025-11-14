import os

restaurantes = [{'nome':'la mole', 'categoria': 'frances','ativo':False},
                {'nome':'Migal', 'categoria':'Tailadesa','ativo':True},
                {'nome':'Bellitalia', 'categoria':'italiana','ativo':False},
                {'nome':'churrascaria', 'categoria':'Brasil','ativo':False}]

def exibir_nome_programa():
    
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
     input('\nDigite uma tecla para voltar ao menu principal:')
     main()

def opcao_invalida():
    print('opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    #os.system('cls')-> é usado para limpar tudo
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def altenar_estado_restaurante():
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input ('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

        voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando novos restaurantes:')

#   para cada restaurante na lista restaurante:
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante ['ativo'] else 'desativado'
        print(f'.  {nome_restaurante}  |  {categoria} |  {ativo}')

    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    #docstring mostrar o que a função está fazendo
    '''Essa função  é responsável por cadastrar um novo restaurante
    
    Inputs:
    -Nome do restaurante
    -Categoria

    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    
    '''
    # append() método acrescenta um  elemento ao final da lista
    exibir_subtitulo('cadastrar novos restaurantes:')
    nome_restaurante = input('Digite o nome que você quer cadastrar: ')
    categoria = input ('Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    input('\nDigite uma tecla para voltar ao menu principal! ')
    main()
     
def escolher_opcoes():
    # if : se  
    # elif : se as condições anteriores não forem verdadeiras, então tente esta condição
    # else : senão
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
              cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
              listar_restaurantes()
        elif opcao_escolhida == 3:
              altenar_estado_restaurante()
        elif opcao_escolhida == 4:
                finalizar_app()
        else:
                opcao_invalida()
    except:
          opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()