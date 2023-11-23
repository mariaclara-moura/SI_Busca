
def calcular_tempo(distancia):
    tempo_horas = distancia/30   # Calcula o tempo em horas
    tempo_minutos = tempo_horas * 60  # Converte o tempo para minutos
    return round(tempo_minutos,1)  # Arredonda o tempo para uma casa decimal

distancia = [
    [0.0, 10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8],  # Estação E1 
    [10.0, 0.0, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8],  # Estação E2 
    [18.5, 8.5, 0.0, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6],  # Estação E3 
    [24.8, 14.8, 6.3, 0.0, 12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],  # Estação E4 
    [36.4, 26.6, 18.2, 12, 0.0, 3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],  # Estação E5 
    [38.8, 29.1, 20.6, 14.4, 3, 0.0, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],  # Estação E6
    [35.8, 26.1, 17.6, 11.5, 2.4, 3.3, 0.0, 20, 23, 27.3, 34.2, 25.7, 12.4, 15.6],  # Estação E7
    [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20, 0.0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6],  # Estação E8 
    [17.6, 10, 9.4, 12.6, 23.3, 25.7, 23, 8.2, 0.0, 13.5, 11.2, 10.9, 21.2, 26.6],  # Estação E9 
    [9.1, 3.5, 10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0.0, 17.6, 24.2, 18.7, 21.2],  # Estação E10 
    [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0.0, 14.2, 31.5, 35,5],  # Estação E11 
    [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4, 10.9, 24.2, 14.2, 0.0, 28.8, 33.6],  # Estação E12 
    [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0.0, 5.1],  # Estação E13 
    [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35,5, 33.6, 5.1, 0.0],  # Estação E14 
]

tempos = []

for linha in distancia:
    estacao = []
    for elemento in linha:
        tempo = calcular_tempo(elemento)
        estacao.append(tempo)
    tempos.append(estacao)

dados_reais = {
    1 : [(2, calcular_tempo(10), 'azul')], 
    2 : [(3, calcular_tempo(8.5), 'azul'), (1, calcular_tempo(10), 'azul'), (9, calcular_tempo(10), 'amarela'), (10, calcular_tempo(3.5), 'amarela')], 
    3 : [(2, calcular_tempo(8.5), 'azul'), (4, calcular_tempo(6.3), 'azul'), (9, calcular_tempo(9.4), 'vermelha'), (13,calcular_tempo(18.7), 'vermelha')],
    4 : [(3, calcular_tempo(6.3), 'azul'), (5, calcular_tempo(13), 'azul'), (8, calcular_tempo(15.3), 'verde'), (13, calcular_tempo(12.8), 'verde')],
    5 : [(4, calcular_tempo(13), 'azul'), (6, calcular_tempo(3), 'azul'), (7, calcular_tempo(2.4), 'amarela'), (8, calcular_tempo(30), 'amarela')],
    6 : [(5, calcular_tempo(3), 'azul')],
    7 : [(5, calcular_tempo(2.4), 'amarela')],
    8 : [(5, calcular_tempo(30), 'amarela'), (4, calcular_tempo(15.3), 'verde'), (9, calcular_tempo(9.6), 'amarela'), (12, calcular_tempo(6.4), 'verde')],
    9 : [(8, calcular_tempo(9.6), 'amarela'), (2, calcular_tempo(10), 'amarela'), (3, calcular_tempo(9.4), 'vermelha'), (11, calcular_tempo(12.2), 'vermelha')],
    10: [(2, calcular_tempo(3.5), 'amarela')],
    11: [(9, calcular_tempo(12.2), 'vermelha')],
    12: [(8, calcular_tempo(6.4), 'verde')],
    13: [(3, calcular_tempo(18.7), 'vermelha'), (4, calcular_tempo(12.8), 'verde'), (14, calcular_tempo(5.1), 'verde')],
    14: [(13, calcular_tempo(5.1), 'verde')]
}

# Função que retorna os vizinhos de um estado  
def vizinhos(estado):
    if estado in dados_reais:
        return dados_reais[estado]

# Função que implementa o algoritmo A*
def AStar(inicio, fim):
    caminho = []               
    # adiciona o estado inicial na fronteira         
    caminho.append(inicio)          
    caminho_final = []
    # dicionário que armazena o custo de cada estado
    g = {}                             
    # dicionário que armazena o pai de cada estado
    pai = {}                           
    # custo do estado inicial é zero
    g[inicio] = 0                  
    # pai do estado inicial é ele mesmo
    pai[inicio] = inicio
    # enquanto a fronteira não estiver vazia
    while len(caminho) != 0: 
        aux = 0
        for estado in caminho:
            # se o estado auxiliar for igual a zero, ele recebe o estado atual
            if aux == 0:
                aux = estado 
            # se o custo do estado atual for menor que o custo do estado auxiliar, o estado auxiliar recebe o estado atual
            if g[estado] + tempos[estado[0] - 1][fim[0] - 1] < g[aux] + tempos[aux[0] - 1][fim[0] - 1]:
                aux = estado 
        # se o estado auxiliar for diferente do estado final
        if aux != fim: 
            # para cada vizinho do estado auxiliar
            for (number, distance, line) in vizinhos(aux[0]): 
                est = (number, line) 
                # se o vizinho não estiver na fronteira e não estiver no caminho final
                if est not in caminho and est not in caminho_final:
                    # adiciona o vizinho na fronteira
                    caminho.append(est)                
                    print(f'Fronteira: {caminho}')
                    # o pai do vizinho recebe o estado auxiliar
                    pai[est] = aux                  
                    # o custo do vizinho recebe o custo do estado auxiliar mais a distância entre o vizinho e o estado auxiliar
                    g[est] = g[aux] + distance 
                # se o vizinho estiver na fronteira, mas em uma linha diferente, fazemos a baldeação
                    if aux[1] != est[1]: 
                        g[est] = g[est] + 4
                else:
                    # se o custo do vizinho for maior que o custo do estado auxiliar mais a distância entre o vizinho e o estado auxiliar
                    if g[est] > g[aux] + distance:
                        # o custo do vizinho recebe o custo do estado auxiliar mais a distância entre o vizinho e o estado auxiliar
                        g[est] = g[aux] + distance
                        # o pai do vizinho recebe o estado auxiliar
                        pai[est] = aux 
                        if number in caminho_final:
                            caminho_final.remove(est)
                            caminho.append(est)
        # se o estado auxiliar for igual ao estado final ou se o número do estado auxiliar for igual ao número do estado final        
        if (aux == fim) or (aux[0] == fim[0]):
            caminho = []
            while pai[aux] != aux:
                caminho.append(aux)
                aux = pai[aux]
            caminho.append(inicio) 
            caminho.reverse() 
            if (aux[1] != fim[1]):
                # caminho.append(fim)
                if fim not in g:
                    g[fim] = g[caminho[len(caminho)-2]] + 4
            print(f'O caminho a se seguir é {caminho}')
            print(f'O menor tempo é de: {g[fim]} minutos')       
            return caminho

        caminho.remove(aux)
        caminho_final.append(aux)

# recebendo informações
print("Qual é o número da estação de partida?")
estacao_partida = int(input())
print("Qual é a cor da linha de partida?")
linha_partida = input()
print("Qual é o número da estação de destino?")
estacao_destino = int(input())
print("Qual é a cor da linha de destino?")
linha_destino = input()

AStar((estacao_partida, linha_partida), (estacao_destino, linha_destino))