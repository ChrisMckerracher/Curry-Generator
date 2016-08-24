class curryable(type):
    def __new__(mcs, **kwargs):
        return super().__new__(mcs, 'cFunction', (kwargs['base'],), {})
    def __init__(self, value=None, **kwargs):
        self.func = kwargs['func']
        self.__call__ = self.call()
    def call(cls):
        def __call__(self, x):
            tmp=self.__class__(self.func(x) or self)
            a.__init__()
            return tmp
        return __call__
    
b = curryable(base=int, func=(lambda self,y: self+y))
a = b()

#bound methods dont get double instantiated
