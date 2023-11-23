class Test:
    def __init__(self):
        self.a = 10

    def fun(self):
        self.b = 20

t1 = Test()
print(dir(t1))

t1.fun()
print(dir(t1))

t1.c = 30
print(dir(t1))