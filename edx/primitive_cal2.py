
# TIME LIMIT exceeded
def optimal_sequence(target):
    start_node = 1
    if start_node == target:
        return [0]

    tree = {}
    min_steps = {}
    min_steps[start_node] = 0
    tree[1] = 0
    
    to_visit_queue = []
    to_visit_queue.append(start_node)

    while len(to_visit_queue) > 0:
        current_node = to_visit_queue.pop(0)

        # generate the child nodes
        child_nodes = [current_node * 2, current_node * 3, current_node + 1]
        for child_node in child_nodes:
            if child_node not in min_steps:
                min_steps[child_node] = min_steps[current_node] + 1
                to_visit_queue.append(child_node)
                tree[child_node] = current_node
        
        if target in child_nodes:
            break

    result_seq = []
    start_node = target
    while start_node != 0:
        result_seq.append(start_node)
        start_node = tree[start_node]

    result_seq.reverse()
    return result_seq


sequence = list(optimal_sequence(1))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

