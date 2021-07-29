#!/usr/bin/env python3

class HotBeverage:
    def __init__(self, price = 0.30, name = "hot berverage"):
        self.price = price
        self.name = name
    def description(self):
        return "Just some hot water in a cup."
    def __str__(self):
        return ("name : {}\n".format(self.name) +
                "price : {:,.2f}\n".format(self.price) +
                "description : {}".format(self.description()))
class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(0.40, "coffee")
    def description(self):
        return "A coffee, to stay awake."
class Tea(HotBeverage):
    def __init__(self):
        super().__init__(0.30, "tea")
class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(0.50, "chocolate")
    def description(self):
        return "Chocolate, sweet chocolate..."
class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(0.45, "cappuccino")
    def description(self):
        return "Un po’ di Italia nella sua tazza!"

if __name__ == '__main__':
    hotbeverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()
    print(hotbeverage)
    print(coffee)
    print(tea)
    print(chocolate)
    print(cappuccino)