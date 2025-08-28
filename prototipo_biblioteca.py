import datetime


### LISTAS QUE IRÃO GUARDAR OS LIVROS DISPONÍVEIS E OS LIVROS ALUGADOS

lista_de_livros = []
lista_de_livros_alugados = []

###FUNÇÃO PARA LISTAR OS LIVROS DISPONÍVEIS


def listar_livros():
    print('\nLISTA DE LIVROS')
    print('=' * 100)
    if not lista_de_livros:
        print('-> Lista vazia.')
        print('=' * 100)
        return
    
    
    
    for i, livro in enumerate(lista_de_livros, 1):
        print(f'{i:02}. {livro['Livro']:<45} | {livro['Autor']:<20} | {livro['Ano']:<10} | {livro['Código']:<10}')
    print('=' * 100)

### FUNÇÃO PARA ADICIONAR LIVROS À NOSSA BIBLIOTECA

def adicionar_livros():
    livro = input('Digite o nome do livro que deseja adicionar: ')
    autor = input('Digite o nome do autor: ')
    ano = checar_numero('Digite o ano: ')
    codigo = input('Digite o código de verificação do livro: ')

    livro_encontrado = False
    
    for livro_atual in lista_de_livros:
        if livro == livro_atual['Livro']:
            print(f"O livro '{livro}' já está na sua lista.")
            livro_encontrado = True
            break

    if not livro_encontrado:

        lista_de_livros.append({'Livro':livro, 'Autor':autor, 'Ano':ano, 'Código':codigo, 'Disponível':True})
        print(f"O livro '{livro}' foi adicionado com sucesso!" )


    
### FUNÇÃO PARA ALUGAR LIVROS

def alugar_livro():
    listar_livros()

    if not lista_de_livros:
        return

    try:
        
        escolha = int(input('Digite o número do livro que deseja alugar: ')) - 1
        if escolha >= len(lista_de_livros) or escolha < 0:
            print('Digite uma opção válida.')
            return
        

        livro_alugado = lista_de_livros.pop(escolha) 
        livro_alugado['Disponível'] = False
        lista_de_livros_alugados.append(livro_alugado)    

        print(f'\nO livro "{livro_alugado['Livro']}" foi alugado com sucesso!')  


    except ValueError:
        print('Digite um número válido.')


### FUNÇÃO PARA LISTAR TODOS OS LIVROS QUE FORAM ALUGADOS


def livros_alugados():
    print('\nLISTA DE LIVROS ALUGADOS')
    print('=' * 100)
   
    if not lista_de_livros_alugados:
        print('-> Lista vazia.')
        print('=' * 100)
        return
    
    for i, livro in enumerate(lista_de_livros_alugados, 1):
           print(f'{i:02}. {livro['Livro']:<45} | {livro['Autor']:<20} | {livro['Ano']:<10} | {livro['Código']:<10}')
        


########################## FUNÇÕES AUXILIARES ############################



### FUNÇÃO PARA CHECAR O ANO DO LIVRO QUE FOI ADICIONADO À NOSSA BIBLIOTECA



def checar_numero(prompt):
    while True:
        try:
            ano = int(input(prompt))
            if ano > datetime.datetime.now().year or ano < 1200:
              print('Ano inválido.')
              continue
            else:
            
             return ano
            
        except ValueError:
            print('Digite um ano válido.')



### FUNÇÃO PARA VALIDAR O NÚMERO QUE O USUÁRIO IRÁ ESCOLHER NO MENU


def escolha_menu():

     try:
        escolha = int(input('Digite a opção desejada: '))
        if 0 <= escolha <= 4:
            return escolha
        else:
            print('Opção inválida. Escolha um número de 0 a 4.')

     except ValueError:
        print('Digite uma opção válida')




### SISTEMA DA BIBLIOTECA ###

def menu():
    print('\n📚 BIBLIOTECA DA GUIA📚')
    print('\nMENU')
    print('=' * 100)
    print('1. Listar livros disponíveis')
    print('2. Adicionar Livros')
    print('3. Alugar livros')
    print('4. Listar livros alugados')
    print('0. Sair')
    print('=' * 100)

while True:
    menu()
    escolha = escolha_menu()

    match escolha:
        case 1:
            listar_livros()
        case 2:
            adicionar_livros()
        case 3:
            alugar_livro()
        case 4:
            livros_alugados()
        case 0:
            print('Saindo...')
            break

   



    