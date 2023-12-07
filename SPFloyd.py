INF = 9999
def printA(A):
    vsize = len(A)
    print("=======================")
    for i in range(vsize):
        for j in range(vsize):
            if(A[i][j] == INF) : print(" INF ", end='')
            else : print("%4d "%A[i][j], end='')
        print("")

def shortest_path_floyd(vertex, adj) :
    vsize = len(vertex)
    A = list(adj)
    for i in range(vsize):
        A[i] = list(adj[i])

        for k in range(vsize) :
            for j in range(vsize) :
                if (A[i][k] + A[k][j] < A[i][j]) :
                    A[i][j] = A[i][k] + A[k][j]
            printA(A)