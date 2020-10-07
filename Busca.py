class Busca_em_Largura():
    def __init__(self,adj_lista,inicial):
        self.adj_lista = adj_lista
        self.inicial = inicial


    def buscaLargura(self):
        adj_lista = self.adj_lista
        visited = {}
        level = {}
        parent = {}
        output = []
        queue = []
        for vertice in adj_lista.keys():
            visited[vertice] = False
            parent[vertice] = None
            level[vertice] = -1

        s = self.inicial
        visited[s] = True
        level[s] = 0
        queue.append(s)
        t = 0
        vertices = list(adj_lista.keys())
        for c in range(len(vertices)):
            u = queue[t]
            queue.pop(t)
            output.append(u)
            for v in adj_lista[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    level[v] = level[u] + 1
                    queue.append(v)
            if not queue:
                break
        return output,level