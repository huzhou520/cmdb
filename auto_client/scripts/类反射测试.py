class A(object):
    def __init__(self, name):
        self.name = name

    def func(self):
        print(self.name)

cls = setattr(A, "func")
