#IMPORTANTE
#Este codigo fue diseñado en base a lo que se enseño en la materia de matematicas discretas 2.
#Este algoritmo BFS funciona con unas reglas que desconcco si son aplicables para todos, las reglas son las siguientes
#El algortimo funciona de manera que nosotros al introducir el grafo, debemos introducir ya ordenado de manera antihoraria del reloj
#las conexiones entre un vertice a otro, ya que fue la manera que se nos enseño para solucionarlo



from collections import deque

def dfs(graph, start):
    visited = set()  # Para rastrear los nodos visitados
    stack = deque([start])  # Pila inicializada con el nodo de inicio
    dfs_order = []  # Lista para mantener el orden de visita de los nodos

    # Imprime la cabecera de las pilas
    print(f"{'Pila':<20}{'1':<3}{'2':<3}{'3':<3}{'4':<3}{'5':<3}{'6':<3}{'7':<3}{'8':<3}{'9':<3}{'10':<3}{'11':<3}{'12':<3}")

    step = 1

    while stack:
        node = stack.pop()  # Saca el último nodo de la pila
        if node not in visited:
            visited.add(node)  # Marca el nodo como visitado
            dfs_order.append(node)  # Añade el nodo al orden de DFS

            # Añade los vecinos no visitados a la pila en el orden adecuado
            temp_stack = []
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    temp_stack.append(neighbor)
            stack.extend(temp_stack)

            # Construye la línea de la pila para imprimir
            stack_print = []
            for i in range(1, 13):
                if i <= len(stack):
                    stack_print.append(stack[-i])
                else:
                    stack_print.append('-')

            # Imprime el estado actual de la pila
            print(f"Pila {step:<2} {' '.join(map(str, stack_print))}")

            step += 1

    # Imprime la última pila cuando la pila está vacía
    if not stack:
        stack_print = ['-'] * 12
        print(f"Pila {step:<2} {' '.join(stack_print)}")

    return dfs_order

# Definimos la conexion con de cada vertice de manera antihoraria
graph = {
#Aclaro, si se va a trabajar con numeros, el numero del primer grafo debe ser 0, de lo contrario no funciona#
'a': ['b', 'c', 'd'], 
'b': ['g', 'e', 'c', 'a'],
'c': ['b', 'e', 'f', 'd', 'a'],
'd': ['a', 'f'],
'e': ['b', 'g', 'f', 'c'],
'f': ['c', 'e', 'h', 'd'],
'g': ['j', 'h', 'e', 'b'],
'h': ['f', 'g', 'i'],
'i': ['h', 'j'],
'j': ['g', 'i']
}
start_node = 'a'
result_dfs = dfs(graph, start_node)
print("\nOrden de visita en DFS:", result_dfs)
