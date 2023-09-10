from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from Pizza import Pizza


class PizzaOrder:

    def __init__(self, time):
        self.pizzas = []
        self.time = time
        self.totalprice = 0.0

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):

        s = '******\n'
        s+= 'Order Time: {}\n'.format(self.time)
        for pizza in self.pizzas:
            self.totalprice += pizza.price
            s += pizza.getPizzaDetails()
            s += '\n'
            s+= '----\n'
        s+= 'TOTAL ORDER PRICE: {}\n'.format(self.totalprice)
        s+= '******\n'
        return s
        
cp1 = CustomPizza("L")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
cp2 = CustomPizza('M')
cp2.addTopping('pepperoni')
cp2.addTopping('chicken')
sp1 = SpecialtyPizza("S", "Carne-more")
order = PizzaOrder(123000) #12:30:00PM
order.addPizza(cp1)
order.addPizza(sp1)
