def encontrar_ruta(C):
    matriz = encontrar_ruta_aux(C, 0, 0)
    if matriz == []:
        return []
    else: 
        for i in range(0, len(matriz)):
            for j in range (0, len(matriz[0])):
                if matriz[i][j] == 'b':
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0
    return matriz

def encontrar_ruta_aux(C,i,j):

    if i == len(C)-1 and j == len(C[i])-1:
        C[len(C)-1][len(C[i])-1]='b'
        return C
    elif C[0][1] == 1 and C[1][0] == 1:
        return []
    elif C[len(C)-1][len(C[len(C)-1])-1]==1:
        return []

    elif (C[len(C)-2][len(C[len(C)-1])-1] == 1) and (C[len(C)-1][len(C[len(C)-1])-2] == 1):
        return []

    else:
        if i == len(C)-1:
            if C[i][j+1] == 0:
                C[i][j] ='b'
                return encontrar_ruta_aux(C,i,j+1)
            else:
                return []

        elif j == len(C[i])-1:
            if C[i+1][j] == 0:
                C[i][j] = 'b'
                return encontrar_ruta_aux(C,i+1,j)
            else:
                if C[i][j-1] == 0:
                    C[i][j] = 'b'
                    return encontrar_ruta_aux(C,i,j-1)
                C[i][j] = 1
                return encontrar_ruta_aux(C,i,j-1)
        elif C[i][j+1] == 0:
            C[i][j] = 'b'
            return encontrar_ruta_aux(C,i,j+1)
        elif C[i+1][j] == 0:
            C[i][j] = 'b'
            return encontrar_ruta_aux(C,i+1,j)

        elif C[i][j+1] == 1:
            if C[i+1][j] == 0:
                C[i][j] = 'b'
                return encontrar_ruta_aux(C,i+1,j)
            else:
                if C[i][j-1] == 0:
                    C[i][j] = 'b'
                    return encontrar_ruta_aux(C,i,j-1)
                C[i][j] = 1
                return encontrar_ruta_aux(C,i,j-1)
        elif C[i][j+1] == 'b':
            if C[i][j-1] == 0:
                C[i][j] = 'b'
                return encontrar_ruta_aux(C,i,j-1)

            return []
