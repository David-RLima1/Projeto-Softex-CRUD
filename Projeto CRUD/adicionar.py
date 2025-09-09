import banco_de_dados

def adicionar_livro():
    
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação: ")

   
    if banco_de_dados.livros:
        novo_id = banco_de_dados.livros[-1]['id'] + 1
    else:
        novo_id = 1

    novo_livro = {
        'id': novo_id,
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'status': 'disponível'
    }

    
    banco_de_dados.livros.append(novo_livro)
    print(f"\nLivro '{titulo}' adicionado com sucesso!")