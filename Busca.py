class Buscas():
    def __init__(self,adj_lista,inicial):
        self.adj_lista = adj_lista
        self.inicial = inicial


    def buscaLargura(self):
        adj_lista = self.adj_lista
        visitado = {}
        level = {}
        adjacente = {}
        arvore = []
        fila = []
        for vertice in adj_lista.keys():
            visitado[vertice] = False
            adjacente[vertice] = None
            level[vertice] = -1

        s = self.inicial
        visitado[s] = True
        level[s] = 0
        fila.append(s)
        t = 0

        vertices = list(adj_lista.keys())
        for c in range(len(vertices)):
            u = fila[t]
            fila.pop(t)
            arvore.append(u)
            for v, in adj_lista[u]:

                if not visitado[v]:
                    visitado[v] = True
                    adjacente[v] = u
                    level[v] = level[u] + adj_lista[u][v]
                    fila.append(v)

            if not fila:
                break

        return arvore