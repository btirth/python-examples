class car:

    wheels=4    #class variables

    def _init_(self):
        self.mil = 10            #instance varibles
        self.comp = 'BMW'



c1 = car
c1._init_(c1)

c2 = car
#c2._init_(c2)


c1.mil = 30
c2.comp = 'AUDI'

car.wheels = 3


print(c1.comp,c1.mil,c1.wheels)

print(c2.comp,c2.mil,c2.wheels)
