class Parent:
    def __init__(self, p1, p2):
        '''super()를 사용하지 않으면 overriding 됩니다.'''
        self.p1 = p1
        self.p2 = p2
        
class Child(Parent):
    def __init__(self, c1, **kwargs):
        super(Child, self).__init__(**kwargs)
        self.c1 = c1
        self.c2 = "This is Child's c2"
        self.c3 = "This is Child's c3"

child = Child(p1="This is Parent's p1", 
              p2="This is Parent's p1", 
              c1="This is Child's c1")

print(child.p1)
print(child.p2)
print(child.c1)
print(child.c2)
print(child.c3)