from Pizza import Pizza

class SpecialtyPizza(Pizza):

    def __init__(self, size, name):
        super().__init__(size)
        self.name = name

        if self.size.upper()=='S':
            self.price = 12.0
        elif self.size.upper()=='M':
            self.price= 14.0
        elif self.size.upper()=='L':
            self.price = 16.0

    def getPizzaDetails(self):

        s = 'SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n'.format(self.size, self.name, self.price)

        return s

sp1 = SpecialtyPizza("S", "Carne-more")
