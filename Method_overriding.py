class A:

    def show(self):
        print("in A show")

class B(A):

    def show(self):
        print("in B self")



a1 = B()
a1.show
