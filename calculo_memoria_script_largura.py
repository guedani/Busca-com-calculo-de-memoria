import graphviz
import time
import psutil

def get_memory_usage():
    # Obter o uso de memória em bytes
    memory_bytes = psutil.Process().memory_info().rss
    # Converter para kilobytes (KB) e megabytes (MB)
    memory_kb = memory_bytes / 1024
    memory_mb = memory_kb / 1024
    return memory_bytes, memory_kb, memory_mb
memoria_inicial_bytes, memoria_inicial_kb, memoria_inicial_mb = get_memory_usage()

class No:
    def __init__(self, valor):
        self.valor = valor #nó raiz
        self.filhos = [] #lista de filhos

    # Adiciona um filho a este nó
    def adicionar_filho(self, filho):
        # append adiciona um único elemento ao final de uma lista
        self.filhos.append(filho)

    # Retorna uma representação em string da árvore a partir deste nó
    def __str__(self):
        return f"{self.valor}{'[' + ', '.join(str(filho) for filho in self.filhos) + ']' if self.filhos else ''}"
    
# Cria uma árvore do exemplo
raiz = No('Nina')
no2_gustavo = No('Gustavo')
no3_fabiana = No('Fabiana')
no4_junior = No('Junior')
no5_alice = No('Alice')
no6_gabriel = No('Gabriel')

raiz.adicionar_filho(no2_gustavo)
raiz.adicionar_filho(no3_fabiana)
raiz.adicionar_filho(no4_junior)
no4_junior.adicionar_filho(no2_gustavo)
no4_junior.adicionar_filho(no3_fabiana)
no2_gustavo.adicionar_filho(no3_fabiana)
no2_gustavo.adicionar_filho(no5_alice)
no2_gustavo.adicionar_filho(no6_gabriel)
no3_fabiana.adicionar_filho(no5_alice)
no3_fabiana.adicionar_filho(no6_gabriel)

# print(raiz)

g = graphviz.Digraph('G', filename='arvore')

g.edge('Nina', 'Gustavo')
g.edge('Nina', 'Junior')
g.edge('Nina', 'Fabiana')
g.edge('Junior', 'Gustavo')
g.edge('Junior', 'Fabiana')
g.edge('Gustavo', 'Fabiana')
g.edge('Gustavo', 'Gabriel')
g.edge('Gustavo', 'Alice')
g.edge('Fabiana', 'Gabriel')
g.edge('Fabiana', 'Alice')
# g

# Função de busca em largura
def busca_em_largura(raiz, valor_procurado):
    # Cria uma fila vazia para a busca em largura
    fila = [raiz]

    # Percorre a fila enquanto ela não estiver vazia
    while fila:
        # Remove o primeiro elemento da fila e verifica se ele contém o valor procurado
        # Remove um item em uma dada posição na lista e o retorna.
        #Se nenhum índice é especificado, a.pop() remove e devolve o último item da lista.
        no_atual = fila.pop(0)
        if no_atual.valor == valor_procurado:
            return no_atual

        # Adiciona os filhos do nó atual à fila
        for filho in no_atual.filhos:
            fila.append(filho)

    # Retorna None se o valor não foi encontrado
    return None

tempo_inicial = time.time()
# Executa a busca em largura a partir da raiz
no_encontrado = busca_em_largura(raiz, 'Gabriel')
tempo_final = time.time()
# Calcula o tempo gasto na busca
print("**********BUSCA EM LARGURA**********")
tempo_gasto_largura = tempo_final - tempo_inicial
print("Tempo Largura: %.7f segundos" % tempo_gasto_largura)
# Imprime o resultado da busca
if no_encontrado is not None:
    a=1
    # print("Valor encontrado: ", no_encontrado.valor)
else:
    print("Valor não encontrado")
    

memoria_final_bytes, memoria_final_kb, memoria_final_mb = get_memory_usage()

# Calcular a diferença
uso_de_memoria_bytes = memoria_final_bytes - memoria_inicial_bytes
uso_de_memoria_kb = memoria_final_kb - memoria_inicial_kb
uso_de_memoria_mb = memoria_final_mb - memoria_inicial_mb

print(f"Uso de memória: {uso_de_memoria_bytes} bytes")
print(f"Uso de memória: {uso_de_memoria_kb:.2f} KB")
print(f"Uso de memória: {uso_de_memoria_mb:.2f} MB")
