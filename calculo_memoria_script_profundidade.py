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

# Função de busca em profundidade
def busca_em_profundidade(no_inicial, valor_procurado):
    # Verifica se o nó atual contém o valor procurado
    if no_inicial.valor == valor_procurado:
        return no_inicial

    # Recursivamente busca o valor em cada filho do nó atual
    for filho in no_inicial.filhos:
        resultado = busca_em_profundidade(filho, valor_procurado)
        if resultado is not None:
            return resultado

    # Retorna None se o valor não foi encontrado
    return None

tempo_inicial = time.time()
# Executa a busca em profundidade a partir da raiz
no_encontrado = busca_em_profundidade(raiz, 'Gabriel')
# Calcula o tempo gasto na busca
tempo_final = time.time()
tempo_gasto_profundidade = tempo_final - tempo_inicial
print("**********BUSCA EM PROFUNDIDADE**********")
print("Tempo Busca Profundidade: %.7f segundos" % tempo_gasto_profundidade)
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
