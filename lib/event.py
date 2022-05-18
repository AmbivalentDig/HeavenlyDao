class Event:
    def __init__(self, cnt_args):
        self.subscriptions = []
        self.cnt_args = cnt_args
    
    def subscribe(self, method):
        self.subscriptions.append(method)

    def invoke(self, *args):
        for subscription in self.subscriptions:
            if args == ():
                subscription()
            else:
                subscription(*args)
