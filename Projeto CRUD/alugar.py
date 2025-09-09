import banco_de_dados
from listar import listar_livros



def alugar_livro():
   
    listar_livros()
    try:
        id_livro = int(input("Digite o ID do livro que deseja alugar: "))
    except ValueError:
        print("\nID inválido. Por favor, digite um número.")
        return

    livro_encontrado = None
    for livro in banco_de_dados.livros:
        if livro['id'] == id_livro:
            if livro['status'] == 'disponível':
                livro['status'] = 'alugado'
                livro_encontrado = livro
                break
            else:
                print("\nEste livro já está alugado.")
                return
    
    if livro_encontrado:
        print(f"\nLivro '{livro_encontrado['titulo']}' alugado com sucesso!")
    else:
        print("\nID do livro não encontrado.")
