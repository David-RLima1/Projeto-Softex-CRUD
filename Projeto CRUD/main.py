from menu import exibir_menu
from adicionar import adicionar_livro
from listar import listar_livros
from alugar import alugar_livro
from devolver import devolver_livro
from busca import buscar_por_nome

def main():
   
    while True:
        opcao = exibir_menu()

        match opcao:
            case '1':
                adicionar_livro()
            case '2':
                listar_livros()
            case '3':
                alugar_livro()
            case '4':
                devolver_livro()
            case '5':
                buscar_por_nome()
            case '6':
                print("Obrigado por usar o sistema! Até logo.")
                break
            case _: 
                print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()