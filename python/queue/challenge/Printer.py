from PrintQueue import PrintQueue
from Job import Job

class Printer():
    def __init__(self):
        self.jobs_list = []
        self.printer_queue = None

    def print_job(self):
        for i in range(len(self.jobs_list)):
            print("Printing Job: ", i)
            current_job = self.jobs_list[i]
            while not current_job.is_completed():
                current_job.print_pages()
        
    def add_job(self, job):
        self.jobs_list.append(job)
    
    def add_printer_queue(self, printer_queue):
        self.printer_queue = printer_queue


printer = Printer()
printer_queue = PrintQueue()
job1 = Job(10)

printer.add_job(job1)
printer.add_printer_queue(printer_queue)

printer.print_job()

    

