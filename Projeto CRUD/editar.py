import banco_de_dados
from listar import listar_livros

def editar_livro():
   
    if not listar_livros():
        return

    try:
        id_livro = int(input("\nDigite o ID do livro que deseja editar: "))
    except ValueError:
        print("\nERRO: ID inválido. Por favor, digite apenas números.")
        return

    livro_encontrado = None
    for livro in banco_de_dados.livros:
        if livro['id'] == id_livro:
            livro_encontrado = livro
            break
    
    if not livro_encontrado:
        print("\nERRO: Livro com este ID não foi encontrado.")
        return

    print("\n--- Editando Livro ---")
    print(f"ID: {livro_encontrado['id']}")
    print(f"Título Atual: {livro_encontrado['titulo']}")
    print(f"Autor Atual: {livro_encontrado['autor']}")
    print(f"Ano Atual: {livro_encontrado['ano']}")
    print("(Deixe em branco e pressione Enter para manter a informação atual)")

    novo_titulo = input(f"Novo título: ")
    novo_autor = input(f"Novo autor: ")
    novo_ano = input(f"Novo ano de publicação: ")

    if novo_titulo.strip(): 
        livro_encontrado['titulo'] = novo_titulo
    
    if novo_autor.strip():
        livro_encontrado['autor'] = novo_autor
        
    if novo_ano.strip():
        # Validação extra para garantir que o ano seja um número
        try:
            livro_encontrado['ano'] = int(novo_ano)
        except ValueError:
            print("\nAVISO: O ano não foi alterado pois o valor digitado não é um número.")

    print(f"\nLivro '{livro_encontrado['titulo']}' atualizado com sucesso!")