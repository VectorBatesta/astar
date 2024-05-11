from nodestate_lib import *



















if __name__ == "__main__":
    #0 = vazio
    raiz = nodeState([0, 1, 3,
                      5, 2, 6,
                      4, 7, 8])
    matrizObjetivo = [1, 2, 3,
                      4, 5, 6,
                      7, 8, 0]
    
    nivelMax = -1
    escolha = -1
    



    print(f'Quantidade máxima de níveis: ', end='')
    nivelMax = int(input())

    if nivelMax < 1:
        exit("maior q zero pls!")
    



    print(f'1-heuristica hill climbing, 2-heuristica melhor escolha?: ', end='')
    escolha = int(input())
    
    match escolha:
        case 1:
            resultado, filhoFinal = heuristica_hill_climbing(raiz, matrizObjetivo, nivelMax)
        case 2:
            resultado, filhoFinal = heuristica_melhorescolha(raiz, matrizObjetivo, nivelMax)
        case _:
            exit(f'1 ou 2 pls!')





    print(f'\n\n\n{resultado}!')
    if resultado == 'SUCESSO':
        print(f'\n\tNível achado: {filhoFinal.nivel}, nó final:')
        printanode(filhoFinal)

        print(f'\tPrintando caminho:\n ', end='')
        printaCaminhoAteRaiz(filhoFinal)
        print(f'\n')
    else:
        print(f'\n\tErro! Não foi achado o objetivo.')