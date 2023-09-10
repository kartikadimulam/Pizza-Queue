from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

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

def test_getPrice():
    assert cp1.getPrice() == 14.0
    assert cp2.getPrice()==11.5
    assert sp1.getPrice()==12.0

def test_getSize():
    assert cp1.getSize()=='L'
    assert cp2.getSize()=='M'
    assert sp1.getSize()=='S'

def test_getPizzaDetails():
    assert cp1.getPizzaDetails() == \
'CUSTOM PIZZA\n\
\Size: L\n\\Toppings:\n\\ \t+ extra cheese\n\\ \t+ sausage\n\\ Price: $14.00\n'
    assert cp2.getPizzaDetails()=='CUSTOM PIZZA\n\\Size: M\n\\Toppings:\n\\ \t+ pepperoni\n\\ \t+ chicken\n\\ Price: $11.50\n'

    assert sp1.getPizzaDetails()=='SPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n'

    
def test_getTime():
    assert order.getTime()==123000

