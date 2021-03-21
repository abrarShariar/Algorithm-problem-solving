class MyRouter(object):
    def __init__(self, routerName, mode, ios):
        self.routerName = routerName
        self.mode = mode
        self.ios = ios
    
    def print_router(self, manuf_date):
        print("Name of the router ",self.routerName)
        print("Mode of the router ", self.mode)


class miniRouter(MyRouter):
    def __init__(self, router_name, mode, ios):
        super().__init__(router_name, mode, ios)
        self.print_router("12/23/23")

    
# router = MyRouter("My Router", "Test mode", 123, "123123")
# print(router.print_router("01/01/03"))
# print(getattr(router, 'mode'))

m = miniRouter("Abrar", "test router", "mode")