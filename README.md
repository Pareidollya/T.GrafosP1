# T.GrafosP1
 
Componentes:
* João Pedro Nimuendaju Santana Santos
* José Davi Correia Passos
* Gabriel Costa Rezende





Tutorial:

Para executar o código
1. arestas: 
   para executar os proximos passos é nescessário criar uma váriavel que será lida como as arestas do grafo
   nos seguintes formatos:
   * Digrafos: [('A','B',1),('B','A',1),('B','C',4),('C','B',2),('C','A',1)] #Exemplo
   
   - Obs1: ('A','B',1) segmento orientado de 'A' para 'B'
   - Obs2: A ordem dos vertices influencia, ('A','B',1) != ('B','A',1). Porém a ordem das Tuplas não.


   * Grafos:[('A','B',1),('B','C',1),('C','A',1)] #Exemplo
   - Obs1: Não passar a ordem inversa dos vertices o programa já faz a leitura considerando que possui inversa.
   - Obs2: A Ordem dos vertices e das tuplas não influencia ('A','B',1) = ('B','A',1)

   - Obs Geral 1: O 3° valor em cada lista é o peso, caso não haja peso, colocar 1
   - Obs Geral 2: O 3° valor é sempre o peso, não colocar ele em outros indices da lista.
   - Obs Geral 2: Para ambos os casos, o loop é lido na forma: ('A','A',1) #loop em 'A'
   - Obs Geral 3: O programa consegue ler grafos que sejam desconexo, desde que sejam
                  arestas desconexas, Um vertice solto sem conexão com mais nenhum o 
                  programa não lê.
                  
2. Instanciar a classe grafos com os seguintes parametros: arestas ,digrafo(bool).

3. Os Métodos:
   * matrizAdj() 
    > não precisa passar parametros.
    > retorna duas estruturas: A matrix, e um dicionario.
    > A matrix está no formato de listas dentro de listas.
    > O dicionario possui os vertices como chaves, e os indices como valores.
    > Caso no dicionario o vertice 'A' esteja com valor 0 ('A':0), a matrix no indice 0 representa 'A'.


   * getAdjacente()
    > Precisa de um parametro: O vertice.          
    > Passar um vertice valido no formato: 'A', somente o character. 
    > Não passar listas ou qualquer outro tipo de estrutura, o programa só aceita um vertice por vez.
    > O método retorna uma lista dos vertices adjacentes ao vertice passado como parametro.


   * ehRegular():
    > O método não precisa de parametros:
    > O método retorna um valor booleano, para os seguintes casos: True = Regular, False = Não Regular

   * ehcompleto():
   > O método não precisa de parametros:
   > O método da o resultado corretamente em grafos simples. Caso não seja simples não tem garantia
   > O método retorna um valor booleano, para os seguintes casos: True = Completo, False = Não Completo

   * conexo():
   > O método precisa de um parametro: O vertice
   > O vertice só é nescessario por conta do tipo de busca que é em largura, 
     nesse caso tanto faz o vertice desde que ele seja valido(está na matrix)
   > O método retorna um valor booleano, para os seguintes casos: True = conexo, False = Não conexo
