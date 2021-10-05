import LerDados as lD
nome_x = lD.nome_x
nome_y = lD.nome_y
matriz_x = lD.leitor_x(nome_x)
matriz_y = lD.leitor_x(nome_y)


def mul_m(a, b):  # função que multiplica matrizes
    if len(a[0]) != len(b):
        return False
    numc_b = len(b[0])
    mf = []
    lf = []
    for linha in a:
        coluna2 = 0
        for i in range(numc_b):
            linha2 = 0
            soma_linha = 0
            for elemento in linha:
                soma_linha += elemento*b[linha2][coluna2]
                linha2 += 1
            lf.append(soma_linha)
            coluna2 += 1
        mf.append(lf)
        lf = []
    return mf


def gerador_identidade(a):  # Cria uma matriz identidade de tamanho de outra matriz a
    identidade = []
    for i in range(len(a)):
        identidade.append([])
        for j in range(len(a[0])):
            if i != j:
                identidade[i].append(0)
            else:
                identidade[i].append(1)
    return identidade


def gerador_p(m, x, y):  # gera matrizes de permutação
    p = gerador_identidade(m)
    for i in range(len(p)):
        for j in range(len(p[0])):
            if i == x and j == y:
                p[i][j] = 1
            elif i == y and j == x:
                p[i][j] = 1
            elif i == j and i != x and i != y:
                p[i][j] = 1
            else:
                p[i][j] = 0
    return p


def transpor_matriz(a):  # transpõe uma matriz
    transp = []
    for j in range(len(a[0])):
        transp.append([])
        for i in range(len(a)):
            transp[j].append(0)
    for i in range(len(a)):
        for j in range(len(a[0])):
            transp[j][i] = a[i][j]
    return transp


def plu(a, y):
    y = mul_m(transpor_matriz(a), y)
    a = mul_m(transpor_matriz(a), a)

    for num_coluna in range(len(a[0])):

        matriz_l = gerador_identidade(a)  # Primeiramente criamos uma matriz L igual a matriz identidade
        maior = 0   # Vejo o maior elemento da coluna para permutar a linha desse elemento com a linha do pivo
        l_maior = 0

        for num_linha in range(len(a)):
            if a[num_linha][num_coluna] > maior and num_linha >= num_coluna:
                maior = a[num_linha][num_coluna]
                l_maior = num_linha
        if l_maior != num_coluna:  # Se a linha do maior elemento for diferente da linha do pivo da coluna permutamos
            p = gerador_p(a, l_maior, num_coluna)
            a = mul_m(p, a)
            y = mul_m(p, y)

        for num_linha in range(len(a)):  # Se o elemento for diferente de zero e estiver abaixo da diagonal principal
            if num_linha > num_coluna:      # ele sera transformado em zero com a utilizacao da matriz L
                if a[num_linha][num_coluna] != 0:
                    matriz_l[num_linha][num_coluna] = -a[num_linha][num_coluna]/a[num_coluna][num_coluna]
        a = mul_m(matriz_l, a)
        y = mul_m(matriz_l, y)

    return a, y


def backsubstitution_3(x, y):  # faz o processo de backsubstitution em matrizes 3x3
    w = []
    for j in range(len(x[0])):
        w.append([0])
    w[-1] = [y[-1][0]/(x[-1][-1])]
    w[-2] = [(y[-2][0] - x[-2][-1] * w[-1][0]) / x[-2][-2]]
    w[-3] = [(y[-3][0] - x[-3][-2] * w[-2][0] - x[-3][-1] * w[-1][0]) / x[-3][-3]]
    return w


def backsubstitution_4(x, y):  # faz o processo de backsubstitution em matrizes 4x4
    print(x)
    w = []
    for j in range(len(x[0])):
        w.append([0])
    w[-1] = [y[-1][0]/(x[-1][-1])]
    w[-2] = [(y[-2][0] - x[-2][-1] * w[-1][0]) / x[-2][-2]]
    w[-3] = [(y[-3][0] - x[-3][-2] * w[-2][0] - x[-3][-1] * w[-1][0]) / x[-3][-3]]
    w[-4] = [(y[-4][0] - x[-4][-3] * w[-3][0] - x[-4][-2] * w[-2][0] - x[-4][-1] * w[-1][0]) / x[-4][-4]]
    return w


def classificador(x1, x2, x3, x4):

    estima_set = x1 * 0.12233731500858203 + x2 * -0.08307934509562764 + x3 * 0.11714255908031243 + -0.2751601959151389
    estima_ver = x1 * -0.0652848925605403 + x2 * 0.3093140157056862 + x3 * 0.3544548599753063 + -0.6719894006568884
    estima_vir = x1 * -0.11928415281339257 + x2 * 0.3428372761572133 + x3 * 0.21327332369667998 + 0.49260266786622786

    erro_setosa = abs(x4 - estima_set)
    erro_versicolor = abs(x4 - estima_ver)
    erro_virginica = abs(x4 - estima_vir)

    if erro_setosa < erro_versicolor and erro_setosa < erro_virginica:
        return "Setosa"
    elif erro_versicolor < erro_setosa and erro_versicolor < erro_virginica:
        return "Versicolor"
    elif erro_virginica < erro_setosa and erro_virginica < erro_versicolor:
        return "Virgínica"


x_final, y_final = plu(matriz_x, matriz_y)
print(backsubstitution_3(x_final, y_final))
# print(backsubstitution_4(matriz_x, matriz_y))
# print(backsubstitution_3(matriz_x, matriz_y))
# print(mul_m(transpor_matriz(matriz_x), matriz_x))


