def get_path(graph, start_node, end_node):
  visited = [start_node]
  queue = [start_node]

  distance = {}
  predecessor = {}
  
  dist_count = 0
  distance[start_node] = dist_count
  dist_count += 1

  while len(queue) > 0:
    current_node = queue.pop(0)

    if current_node in graph.keys():
      for neighbour_node in graph[current_node]:
        if neighbour_node not in visited:
          visited.append(neighbour_node)
          queue.append(neighbour_node)

          # populate distance and predecessor
          distance[neighbour_node] = dist_count
          predecessor[neighbour_node] = current_node

          if neighbour_node == end_node:
            break

      dist_count += 1

  # loop over the predecessors' values from end node to find parent
  shortest_path = []
  parent_node = predecessor[end_node]
  shortest_path.append(parent_node)

  while parent_node in predecessor.keys():
    parent_node = predecessor[parent_node]
    shortest_path.append(parent_node)

  shortest_path = list(reversed(shortest_path))
  shortest_path.append(end_node)
  print(shortest_path)

graph_input = {
  'j': ['m', 'b', 'r', 'n'],
  'm': ['w', 'o']
}

network = {
  'Min'     : ['William', 'Jayden', 'Omar'],
  'William' : ['Min', 'Noam'],
  'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
  'Ren'     : ['Jayden', 'Omar'],
  'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
  'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
  'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
  'Noam'    : ['Nathan', 'Jayden', 'William'],
  'Omar'    : ['Ren', 'Min', 'Scott'],
}

get_path(network, 'Jayden', 'Adam')

  
