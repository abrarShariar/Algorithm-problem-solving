# from typing import DefaultDict

# def topologicalSort(jobs, deps):
#     # create the dependency dictionary
#     dep_dict = DefaultDict(list)
#     for item in deps:
#         main_num = item[1]
#         dependency = item[0]
#         dep_dict[main_num].append(dependency)

#     # Write your code here.
#     result_list = set()
#     for current_job in jobs:
#         if current_job not in result_list:
#             result_list = topologicalSortHelper(current_job, dep_dict, result_list)
    
#     return result_list

# def topologicalSortHelper(current_job, dep_dict, result_list):
#     # this means the current_job does not have any dependency
#     if len(dep_dict[current_job]) == 0:
#         result_list.add(current_job)
#         return result_list
    
#     for dependency in dep_dict[current_job]:
#         if dependency not in result_list:
#             result_list = topologicalSortHelper(dependency, dep_dict, result_list)

#     return result_list
    
# print(topologicalSort([1,2,3,4], [[1,2], [1,3], [3,2], [4,2], [4, 3]]))


from typing import DefaultDict

task_list = set()

def topologicalSort(jobs, deps):
    # create the adjacency list of nodes here
    graph = DefaultDict(list)
    for dep in deps:
        graph[dep[1]].append(dep[0])
    
    #  run dfs on each of the jobs (as stored as the node of the graph)
    for job in jobs:
        if job not in task_list:
            dfs(job, graph)

    return task_list


def dfs(job, graph):
    for neighbour in graph[job]:
        if neighbour not in task_list:
            dfs(neighbour, graph)
    
    print(job)
    task_list.add(job)

jobs = [1,2,3,4]
deps = [[1,2], [1,3], [3,2], [4,2], [4,3]]
result_task_list = topologicalSort(jobs, deps)
print(result_task_list)

