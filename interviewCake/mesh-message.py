graph = {
  'j': ['m', 'b', 'r', 'n'],
  'm': ['w', 'o']
}

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

    for neighbour_node in graph[current_node]:
      if neighbour_node not in visited:
        visited.append(neighbour_node)
        queue.append(neighbour_node)
        distance[neighbour_node] = dist_count

    dist_count += 1
    
  print(distance)

get_path(graph, 'j', 'o')

  
