class grafos():

    def __init__(self,arestas,nroVertices,pesos=False,digrafo=True):
        self.arestas = arestas
        self.nroVertices = nroVertices
        self.pesos = pesos
        self.digrafo = digrafo
    def matrixAdj(self):
        matrix = []
        vertices = []
        dict = {}
        

        for v,k in self.arestas:
            if v not in vertices:
                vertices.append(v)
            if k not in vertices:
                vertices.append(k)
        
        for i in range(len(vertices)):
            matrix.append([])
            for j in range(len(vertices)):
                matrix[i].append(0)

        for e in range(len(vertices)):
            dict[vertices[e]] = e

        if self.digrafo == True:
            for v,k in self.arestas:
                matrix[dict[k]][dict[v]] = 1
        else:
            for v,k in self.arestas:
                matrix[dict[v]][dict[k]] = 1
                matrix[dict[k]][dict[v]] = 1
        return matrix,dict

    def getAdjacente(self,matrix,dict,vertice):
        adjacentes = []
        vertices = list(dict.keys())
        aux = list(dict.keys())
        if self.digrafo == True:
            for c in range(len(vertices)):
                if matrix[c][dict[vertice]] != 0:
                    adjacentes.append(aux[c])
        else:
            for c in range(len(vertices)):
                if matrix[dict[vertice]][c] != 0 or matrix[c][dict[vertice]] != 0:
                    adjacentes.append(aux[c])
        return adjacentes
    def ehRegular(self,matrix,dict):
        vertices = list(dict.keys())
        if self.digrafo == True:
            grauE = []
            grauS = []
            regular = []
            nroVertices = len(vertices)
            #aux = list(dict.keys())

            for c in range(nroVertices):
                auxE = 0
                auxS = 0
                for j in range(nroVertices):
                    if matrix[dict[vertices[c]]][j] != 0:
                        auxS += 1
                        if c == j:
                            auxE += 1
                    elif matrix[j][dict[vertices[c]]] != 0:
                        auxE += 1
                grauE.append(auxE)
                grauS.append(auxS)
                for c in range(len(grauE)):
                    if grauE[0] == grauE[c]:
                        regular.append(True)
                    else:
                        regular.append(False)
                for c in range(len(grauS)):
                    if grauS[0] == grauS[c]:
                        regular.append(True)
                    else:
                        regular.append(False)
            return all(regular)
        else:
            grau = []
            regular = []
            for c in range(len(vertices)):
                aux2 = 0
                for j in range(len(vertices)):
                    if matrix[dict[vertices[c]]][j] != 0 or matrix[j][dict[vertices[c]]] != 0:
                        aux2 += 1
                        if c == j:
                            aux2 += 1
                grau.append(aux2)
            for c in range(len(grau)):
                if grau[0] == grau[c]:
                    regular.append(True)
                else:
                    regular.append(False)
            return all(grau)

