class stu:
    sch = 'Vision'

    def _init_(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    #accessor method
    def get_m1(self):
        return self.m1

    #mutator method
    def set_m1(self,value):
        self.m1 = value

    #class method
    @classmethod             #decorator
    def getsch(cls):
        return cls.sch

    #static method
    @staticmethod           #decorator
    def info():
        print("HI Tirth")



s1 = stu()
s2 = stu()

s1 = stu._init_(s1,77,89,45)
s2 = stu._init_(s2,34,67,44)

print(s1.avg)
print(stu.getsch)
student.info()
