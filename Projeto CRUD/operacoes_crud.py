
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

def listar_livros():
    
    if not banco_de_dados.livros:
        print("\nNenhum livro cadastrado ainda.")
        return

    print("\n--- Lista de Livros ---")
    for livro in banco_de_dados.livros:
        print(f"ID: {livro['id']:02} | Título: {livro['titulo']:<40} | Autor: {livro['autor']:<30} | Status: {livro['status']}")
    

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