class Job:
    def __init__(self, number_of_pages):
        self.number_of_pages = number_of_pages
        
    def print_pages(self):
        if self.number_of_pages == 0:
            print('Finished printing all the pages')
        
        print("Printing page")
        self.number_of_pages -= 1
    
    def is_completed(self):
        return self.number_of_pages == 0
    
