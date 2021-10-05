nome_x = 'versicolorX.txt'
nome_y = 'versicolorY.txt'


def leitor_x(x):
    aberto = open(x, encoding='utf-8')
    lista_final = []
    for linha in aberto:
        l = linha.split()
        lista_transicao = []
        for elemento in l:
            lista_transicao.append(float(elemento))
        lista_final.append(lista_transicao)
    return lista_final


def leitor_y(y):
    aberto = open(y, encoding='utf-8')
    lista_final = []
    for linha in aberto:
        l = linha.split()
        lista_transicao = []
        for elemento in l:
            lista_transicao.append(float(elemento))
        lista_final.append(lista_transicao)
    return lista_final


leitor_x(nome_x)
leitor_y(nome_y)
