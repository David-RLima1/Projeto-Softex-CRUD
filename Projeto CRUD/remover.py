import banco_de_dados
from listar import listar_livros

class IDinvalidoError(Exception):
    pass

def remover():

    if not listar_livros():
        print('Lista vazia.')
        return False
    
    listar_livros()
    while True: 
        try:
            num = int(input('Digite o ID do livro que deseja remover: '))

            if num >= len(banco_de_dados.livros) or num < 0:
                raise IDinvalidoError('Digite um ID válido.')
            
            break
        
        except ValueError:
            print('Digite um ID válido.')
        except IDinvalidoError as e:
            print(f'ERRO: {e}')

    for livro in banco_de_dados.livros:
        if livro['id'] == num:
            print(f'Livro "{livro['titulo']}" removido com sucesso!')
            banco_de_dados.livros.remove(livro)
            return True
    

    



