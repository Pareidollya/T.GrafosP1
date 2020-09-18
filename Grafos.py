def matriz(linha_coluna): #criar matriz
    matriz = []
    for i in range(linha_coluna):
        matriz = matriz + [[0]*linha_coluna]
    return matriz

n = int(input("Numero de vértices: "))
A = matriz(n)

print("Relacionar Vértices\n")

def Grafo(matriz):
    for j in range(len(matriz)):
        i = 0
        while i < (len(matriz)):
            v = int(input(f"Vertice {j} relaciona com quais? (-1 prox vertice): "))

            if v == -1:
                i = len(matriz) + 1
                print("\n")
            if v > -1 and v <= len(matriz):
                matriz[j][v] = 1
                #matriz[v][j] = 1 caso nao seja um digrafo
            i += 1
    return matriz

def printGrafo(grafo):
    for j in range(len(grafo)):
        print(grafo[j])
    #imprimir grafo (adicionar arestas)

printGrafo(Grafo(A))
