class A:
    def _init_(self):
        print('Init A')

    def feature1(self):
        print('feature1 in A')

    def feature2(self):
        print('feature2')


class B(A):
    def _init_(self):
        super()._init_()    #to access init of A
        print('Init B')

    def feature1(self):
        print('feature1 in B')

    def feature4(self):
        print('feature4')


class C(A,B):
    def _init_(self):
        super()._init_()    #it will go into init of A not init of B
        print('Init C')


a1 = A()
print('Object of classA')
a1._init_()

a2 = B()
print()
print()
print('Object of classB')


a2._init_()
print()
print('use feature of A through object of B')
a2.feature1()



a3 = C()
a3._init_()
