# #!/usr/bin/env python3
# from multiprocessing import Pool
# def run(task):
#     # Do something with task here
#     print("Handling {}".format(task))


# if __name__ == "__main__":
#     tasks = ['task1', 'task2', 'task3']
#     # Create a pool of specific number of CPUs
#     p = Pool(len(tasks))
#     # Start each task within the pool	
#     p.map(run, tasks)

import os
import subprocess

src = "./data"
dest = "./data-backup"

for root, dirs, files in os.walk(src, topdown = True):
    for name in dirs:
        # print(os.path.join(root, name))
        subprocess.call(["rsync", "-arq", os.path.join(name), os.path.join(dest)])
