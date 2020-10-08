from Busca import Buscas
class grafos():

    def __init__(self, arestas, digrafo=True):
        self.arestas = arestas
        self.digrafo = digrafo

    def matrixAdj(self):
        matrix = []
        vertices = []
        dicionario = {}


        for v, k,l in self.arestas:
            if v not in vertices:
                vertices.append(v)

            if k not in vertices:
                vertices.append(k)

        for i in range(len(vertices)):
            matrix.append([])
            for j in range(len(vertices)):
                matrix[i].append(0)

        for e in range(len(vertices)):
            dicionario[vertices[e]] = e

        if self.digrafo == True:
            for v, k,l in self.arestas:
                matrix[dicionario[k]][dicionario[v]] = l
        else:
            for v, k,l in self.arestas:
                matrix[dicionario[v]][dicionario[k]] = l
                matrix[dicionario[k]][dicionario[v]] = l
        return matrix, dicionario

    def getAdjacente(self, vertice):
        matrix,dicionario = grafos.matrixAdj(self)
        adjacentes = {}
        vertices = list(dicionario.keys())

        if self.digrafo == True:
            for c in range(len(vertices)):
                if matrix[c][dicionario[vertice]] != 0:
                    adjacentes[vertices[c]] = matrix[c][dicionario[vertice]]
        else:
            for c in range(len(vertices)):
                if matrix[dicionario[vertice]][c] != 0: 
                    adjacentes[vertices[c]] = matrix[dicionario[vertice]][c]
                elif matrix[c][dicionario[vertice]] != 0:
                    adjacentes[vertices[c]] = matrix[c][dicionario[vertice]]
        return adjacentes

    def listaAdjacente(self):
        matrix, dicionario = grafos.matrixAdj(self)
        vertices = list(dicionario.keys())
        nroVertices = len(vertices)
        listaAdj = {}
        for c in range(nroVertices):
            vertice = vertices[c]
            listaAdj[vertices[c]] = grafos.getAdjacente(self, vertice)
        return listaAdj

    def ehRegular(self):
        matrix,dicionario = grafos.matrixAdj(self)
        vertices = list(dicionario.keys())
        if self.digrafo == True:
            grauE = []
            grauS = []
            regular = []
            nroVertices = len(vertices)
            # aux = list(dict.keys())

            for c in range(nroVertices):
                auxE = 0
                auxS = 0
                for j in range(nroVertices):
                    if matrix[dicionario[vertices[c]]][j] != 0:
                        auxS += 1
                        if c == j:
                            auxE += 1
                    elif matrix[j][dicionario[vertices[c]]] != 0:
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
                    if matrix[dicionario[vertices[c]]][j] != 0 or matrix[j][dicionario[vertices[c]]] != 0:
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
    def ehcompleto(self):
        listaAdj = grafos.listaAdjacente(self)
        vertices = list(listaAdj.keys())
        completo = []

        for v in listaAdj:
            if len(listaAdj[v]) == len(vertices)-1:
                completo.append(True)
            else:
                completo.append(False)
        return all(completo)
    def conexo(self,verticeInicial):
        vertice = verticeInicial
        listaAdj = self.listaAdjacente()
        instance = Buscas(listaAdj,vertice)
        arvore = instance.buscaLargura()
        vertices = list(listaAdj.keys())
        if len(vertices) != len(arvore):
            return False
        else:
            return True

