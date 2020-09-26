# T.GrafosP1
 
Componentes:
* João Pedro Nimuendaju Santana Santos
* José Davi Correia Passos
* Gabriel Costa Rezende 

Tutorial:

Para executar o código
1. arestas, para executar os proximos passos é nescessário criar uma váriavel que será lida como as arestas do grafo,
   nos seguintes formatos:
   * Digrafos: [('A','B'),('B','A'),('B','C'),('C','B'),('C','A')] #Exemplo
   - Obs1: ('A','B') segmento orientado de 'A' para 'B'
   - Obs2: A ordem dos vertices influencia, ('A','B') != ('B','A'). Porém a ordem das Tuplas não.


   * Grafos:[('A','B'),('B','C'),('C','A')] #Exemplo
   - Obs2: Não passar a ordem inversa dos vertices o programa já faz a leitura considerando que possui inversa.
           A Ordem dos vertices e das tuplas não influencia ('A','B') = ('B','A')

   - Obs3: Para ambos os casos, não passar somente um vertice, ou mais de dois no formato: ('A') ou ('A','B','C') #Erro
   - Obs4: Para ambos os casos, o loop é lido na forma: ('A','A') #loop em 'A'

2. Instanciar a classe grafos com os seguintes parametros: arestas,numero de vertices(int),pesos(bool),digrafo(bool).

3. Os Métodos:
   * matrizAdj() 
    - não precisa passar parametros.
    - retorna duas estruturas: A matrix, e um dicionario.
    - A matrix está no formato de listas dentro de listas.
    - O dicionario possui os vertices como chaves, e os indices como valores.
    - Caso no dicionario o vertice 'A' esteja com valor 0 ('A':0), a matrix no indice 0 representa 'A'.


   * getAdjacente()
    - Precisa de três parametros: Matriz, Dicionario e um Vertice.          
    - Passar nos dois primerios parametros a matriz e o dicionario retornado no metodo matrizAdj().
    - Passar um vertice valido no formato: 'A', somente o character. 
    - Não passar listas ou qualquer outro tipo de estrutura, o programa só aceita um vertice por vez.
    - O método retorna uma lista dos vertices adjacentes ao vertice passado como parametro.


   * ehRegular():
    - O método precisa de dois parametros: Matrix e o Dicionario
    - Passar para os dois parametros, os valores retornado do metodo matrxAdj().
    - O método retorna um valor booleano, para os seguintes casos: True = Regular, False = Não Regular