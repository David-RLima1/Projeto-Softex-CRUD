import banco_de_dados

def buscar_por_nome():
   
    termo_busca = input("Digite o nome ou parte do nome do livro para buscar: ").lower()
    
    
    resultados = [
        livro for livro in banco_de_dados.livros 
        if termo_busca in livro['titulo'].lower()
    ]

    if not resultados:
        print(f"\nNenhum livro encontrado com o termo '{termo_busca}'.")
        return

    print("\n--- Resultados da Busca ---")
    for livro in resultados:
        print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Status: {livro['status']}")
    