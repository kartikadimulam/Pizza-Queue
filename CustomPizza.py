

from Pizza import Pizza

class CustomPizza(Pizza):


    def __init__(self, size):
        
        super().__init__(size)
        if self.size.upper()=='S':
            self.price = 8.0
        elif self.size.upper()=='M':
            self.price = 10.0
        elif self.size.upper()=='L':
            self.price = 12.0
        self.toppingslist=[]

    def addTopping(self, topping):
        self.toppingslist.append(topping)

        if self.size.upper()=='S':
            self.price += 0.5
        elif self.size.upper()=='M':
            self.price += 0.75
        elif self.size.upper()=='L':
            self.price += 1.0

    def getPizzaDetails(self):

        s= 'CUSTOM PIZZA\n\Size: {}\n\Toppings:\n\ '.format(self.size)
        
        for topping in self.toppingslist:
            s += '\t+ {}\n\ '.format(topping)

        s+= 'Price: ${:.2f}\n'.format(self.price)
        return s

cp1 = CustomPizza('L')
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")

cp2 = CustomPizza('M')
cp2.addTopping('pepperoni')
cp2.addTopping('chicken')



    


    

    
