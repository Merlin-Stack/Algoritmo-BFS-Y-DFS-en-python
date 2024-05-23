#IMPORTANTE
#Este codigo fue diseñado en base a lo que se enseño en la materia de matematicas discretas 2.
#Este algoritmo BFS funciona con unas reglas que desconcco si son aplicables para todos, las reglas son las siguientes
#El algortimo funciona de manera que nosotros al introducir el grafo, debemos introducir ya ordenado de manera horaria del reloj
#las conexiones entre un vertice a otro, ya que fue la manera que se nos enseño para solucionarlo


from collections import deque

def bfs(graph, start):
    visited = set()  # Para rastrear los nodos visitados
    queue = deque([start])  # Cola inicializada con el nodo de inicio
    bfs_order = []  # Lista para mantener el orden de visita de los nodos
    
    print(f"{'Paso':<5}{'Nodos Visitados':<20}{'Cola':<20}")
    step = 0

    while queue:
        node = queue.popleft()  # Saca el primer nodo de la cola
        if node not in visited:
            visited.add(node)  # Marca el nodo como visitado
            bfs_order.append(node)  # Añade el nodo al orden de BFS
            # Añade los vecinos no visitados a la cola en el orden adecuado
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
            
            # Imprime el estado actual
            print(f"P{step:<5}{' '.join(bfs_order):<20}{' '.join(queue):<20}")
            step += 1
    
    return bfs_order

# Definimos el grafo y sus conexiones con orden horario 
graph = {
#Aclaro, si se va a trabajar con numeros, el numero del primer grafo debe ser 0, de lo contrario no funciona#
    '0': ['3','2','1'],
    '1': ['0', '2', '7', '5'],
    '2': ['0', '3', '4', '7', '1'],
    '3': ['0', '4', '2'],
    '4': ['2', '3', '6', '7'],
    '5': ['1', '7', '6'],
    '6': ['7', '4', '5'],
    '7': ['1', '2', '4', '6', '5'],
}

start_node = '1'
result_bfs = bfs(graph, start_node)
print("\nOrden de visita en BFS:", result_bfs)
