from nodestate_lib import *







def astar(raiz: nodeState, obj):
    ABERTOS = [raiz]
    FECHADOS = []

    while ABERTOS != []:
        filhoAtual = ABERTOS.pop(0)
        printanode(filhoAtual)

        if filhoAtual.matriz == obj:
            return 'SUCESSO', filhoAtual
        
        filhosGerados = gerar_filhos(filhoAtual)

        #################
        for filhoGerado in filhosGerados:
            atualizaErrados(filhoGerado, obj)
            
            #atualiza valor heuristico Fn
            filhoGerado.heuristico = (filhoGerado.errados * 2) + filhoGerado.nivel

            #detecta se está repetido em abertos ou fechados
            repetido = False
            for nodeAberto in ABERTOS:
                if filhoGerado.matriz == nodeAberto.matriz: #ja esta em abertos 
                    repetido = True
                    #Se o filho foi alcançado por um caminho mais curto, então:
                    #* de ao estado em ABERTOS o caminho mais curto
                    if filhoGerado.nivel < nodeAberto.nivel:
                        nodeAberto.pai = filhoGerado.pai
                    break

            for nodeFechado in FECHADOS:
                if repetido == True:
                    break

                if filhoGerado.matriz == nodeFechado.matriz: #ja esta em fechados 
                    repetido = True
                    #Se o filho foi alcançado por um caminho mais curto, então:
                    #* retire o estado de FECHADOS
                    #* adicione o filho em ABERTOS
                    if filhoGerado.nivel < nodeFechado.nivel:
                        FECHADOS.remove(nodeFechado)
                        ABERTOS.append(filhoGerado)
                    break
            
            if repetido == False: #nao esta em fechados ou abertos
                ABERTOS.append(filhoGerado)
        ######################

        FECHADOS.append(filhoAtual)
        ABERTOS.sort(key=lambda x: x.heuristico) #funcao achada no google
    return 'FALHA', None









if __name__ == "__main__":
    #0 = vazio
    raiz = nodeState([1, 0, 2,
                      5, 3, 7,
                      8, 6, 4])
    matrizObjetivo = [1, 2, 3,
                      4, 5, 6,
                      7, 8, 0]
    
    nivelMax = -1
    escolha = -1
    



    print(f'Quantidade máxima de níveis: ', end='')
    nivelMax = int(input())

    if nivelMax < 1:
        exit("maior q zero pls!")
    



    resultado, filhoFinal = astar(raiz, matrizObjetivo)




    print(f'\n\n\n{resultado}!')
    if resultado == 'SUCESSO':
        print(f'\n\tNível achado: {filhoFinal.nivel}, nó final:')
        printanode(filhoFinal)

        print(f'\tPrintando caminho:\n ', end='')
        printaCaminhoAteRaiz(filhoFinal)
        print(f'\n')
    else:
        print(f'\n\tErro! Não foi achado o objetivo.')