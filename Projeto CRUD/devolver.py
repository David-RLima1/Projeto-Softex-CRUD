
import banco_de_dados
from listar import listar_livros

def devolver_livro():
    
    listar_livros()
    try:
        id_livro = int(input("Digite o ID do livro que deseja devolver: "))
    except ValueError:
        print("\nID inválido. Por favor, digite um número.")
        return
        
    livro_encontrado = None
    for livro in banco_de_dados.livros:
        if livro['id'] == id_livro:
            if livro['status'] == 'alugado':
                livro['status'] = 'disponível'
                livro_encontrado = livro
                break
            else:
                print("\nEste livro não estava alugado.")
                return

    if livro_encontrado:
        print(f"\nLivro '{livro_encontrado['titulo']}' devolvido com sucesso!")
    else:
        print("\nID do livro não encontrado.")