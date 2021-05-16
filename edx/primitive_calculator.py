def primitive_calc(target):
    to_visit_queue = []
    to_visit_queue.append(1)
    node_dict = {}

    is_visited = set()

    while len(to_visit_queue) > 0:
        current_node = to_visit_queue.pop(0)
        if current_node in is_visited:
            continue
        # mulyipy by 2
        mul_2 = current_node * 2
        mul_3 = current_node * 3
        add_1 = current_node + 1
        # generate the child nodes
        child_nodes = [mul_2, mul_3, add_1]
        node_dict[current_node] = child_nodes

        if target in child_nodes:
            break

        # add the child nodes in the queue to visit
        for child_node in child_nodes:
            if child_node not in to_visit_queue:
                to_visit_queue.append(child_node)

        is_visited.add(current_node)

    keys = node_dict.keys()
    return len(keys) - 1, list(keys)

print(primitive_calc(5))
print(primitive_calc(99999))
# 96234O