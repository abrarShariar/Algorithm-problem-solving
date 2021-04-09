def topologicalSort(jobs, deps):
    # create the graph here
    graph = {}
    for job in jobs:
        graph[job] = []
    
    for dep in deps:
        pre_req_job, dependency_job = dep[0], dep[1]
        
