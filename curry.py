class curryable(type):
    #self note:bound methods dont get double instantiated unless manually set in instantiated class
    #and even then, it doesn't bind in a desirable way(at least in this context)
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
a(1)(2)(3)
#>> 6

b = curryable(base=list, func=(lambda self,y: self.append(y)))
a = b()
a(1)(2)(3)
#>>[1,2,3]
a(2)(3)(4)
#>>[2,3,4]
