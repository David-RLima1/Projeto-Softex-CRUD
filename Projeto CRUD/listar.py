import banco_de_dados

def listar_livros():
    
    if not banco_de_dados.livros:
        print("\nNenhum livro cadastrado ainda.")
        return False

    print("\n--- Lista de Livros ---")
    for livro in banco_de_dados.livros:
        print(f"ID: {livro['id']:02} | Título: {livro['titulo']:<40} | Autor: {livro['autor']:<30} | Status: {livro['status']}")
    
    return True
    