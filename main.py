

def main():
    estadoincial = [0, 0]
    capacidade = [4, 3]
    solucao = [0, 2]

    buscaEmLargura(estadoincial, capacidade, solucao)
    resolverBuscaEmProfundidade(estadoincial, capacidade, solucao)

def enche(baldes, capacidade, i):
    baldes[i] = capacidade[i]
    return baldes

def esvazia(baldes, i):
    baldes[i] = 0
    return baldes


def transpor(baldes, capacidade, i, j):

    baldes[j] = baldes[j] + baldes[i]
    baldes[i] = 0
    if(baldes[j] > capacidade[j]):
        baldes[i] = baldes[j] - capacidade[j]
        baldes[j] = capacidade[j]
    return baldes


def buscaEmLargura(estadoincial, capacidade, solucao):
    estadoincial = estadoincial
    capacidade = capacidade
    solucao = solucao

    historico = []
    opcoes = []

    historico.append(estadoincial)
    opcoes.append(estadoincial)

    while 1:
        novasOpcoes = []
        for n in range(len(opcoes)):
            estado = opcoes[n]

            for i in range(len(capacidade)):
                novasOpcoes.append(enche(estado.copy(), capacidade, i))
                novasOpcoes.append(esvazia(estado.copy(), i))
                for j in range(len(capacidade)):
                    if j != i and estado != [0, 0]:
                        novasOpcoes.append(transpor(estado.copy(), capacidade, i, j))
                        novasOpcoes.append(transpor(estado.copy(), capacidade, j, i))

        # novo estado
        opcoes = []
        for op in novasOpcoes:
            if op not in historico:
                historico.append(op)
                opcoes.append(op)

        for option in opcoes:
            if option[solucao[0]] == solucao[1]:
                print("achou")
                return

def buscaEmProfundidade(estado_atual, capacidade, solucao, historico):
    if estado_atual[solucao[0]] == solucao[1]:
        print("achou")
        return True

    print(historico)
    historico.append(estado_atual)

    for i in range(len(capacidade)):
        novo_estado = enche(estado_atual.copy(), capacidade, i)
        if novo_estado not in historico:
            print("enche ", novo_estado)
            if buscaEmProfundidade(novo_estado, capacidade, solucao, historico):
                return True

        novo_estado = esvazia(estado_atual.copy(), i)
        if novo_estado not in historico:
            print("esvazia ", novo_estado)
            if buscaEmProfundidade(novo_estado, capacidade, solucao, historico):
                return True

        for j in range(len(capacidade)):
            if j != i and estado_atual != [0, 0]:
                novo_estado = transpor(estado_atual.copy(), capacidade, i, j)
                if novo_estado not in historico:
                    print("transpor ", novo_estado)
                    if buscaEmProfundidade(novo_estado, capacidade, solucao, historico):
                        return True
    return False

def resolverBuscaEmProfundidade(estadoincial, capacidade, solucao):
    estado_inicial = estadoincial
    capacidade = capacidade
    solucao = solucao

    historico = []

    buscaEmProfundidade(estado_inicial, capacidade, solucao, historico)


if __name__ == '__main__':
    main()



## Implentar busca iterava


## Implementar busca bidirecional