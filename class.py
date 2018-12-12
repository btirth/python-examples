class comp:
    def _init_(self):
        self.name = 'tirth'
        self.age = 18

    def update(self):
        self.age = 28

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1 = comp()
c2 = comp()

c1.update()
print('updated age is ',c1.age)

c1.age = 28
c2.age = 49


if c1.compare(c2)==True:
    print('SAME')
else :
    print('DIFFERENT')
