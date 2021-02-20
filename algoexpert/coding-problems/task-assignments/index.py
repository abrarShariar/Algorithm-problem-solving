# SOLved

from collections import defaultdict

def taskAssignment(k, tasks):
    # Write your code here.
    result_tasks = []
    # sort the tasks
    sorted_tasks = sorted(tasks)
    # map the task time to the index
    tasks_dict = defaultdict(list)
    for i in range(len(tasks)):
        tasks_dict[tasks[i]].append(i)

    start_task_index, end_task_index = 0, len(sorted_tasks) - 1
    
    while start_task_index < end_task_index:
        # find the task's index
        task1_index = tasks_dict[sorted_tasks[start_task_index]].pop(0)
        task2_index = tasks_dict[sorted_tasks[end_task_index]].pop(0)
        result_tasks.append([task1_index, task2_index])

        start_task_index += 1
        end_task_index -= 1

    return result_tasks


print(taskAssignment(3, [1,3,5,3,1,4]))