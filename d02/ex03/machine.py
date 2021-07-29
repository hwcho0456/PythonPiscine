#!/usr/bin/env python3

import random
from beverages import *

class CoffeeMachine:
    def __init__(self):
        self.durability = 10
    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(0.90, "empty cup")
        def description(self):
            return "An empty cup?! Gimme my money back!"
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    def repair(self):
        self.durability = 10
    def serve(self, beverage: HotBeverage = HotBeverage):
        if self.durability == 0:
            raise self.BrokenMachineException()
        self.durability -= 1
        if random.randrange(1,6) == 1:
            return self.EmptyCup()
        else:
            return beverage()
        
if __name__ == '__main__':
    coffeemachine = CoffeeMachine()
    for _ in range(20):
        try:
            choice = random.randrange(1, 6)
            if choice == 1:
                print(coffeemachine.serve())
            elif choice == 2:
                print(coffeemachine.serve(Coffee))
            elif choice == 3:
                print(coffeemachine.serve(Tea))
            elif choice == 4:
                print(coffeemachine.serve(Chocolate))
            else:
                print(coffeemachine.serve(Chocolate))
        except coffeemachine.BrokenMachineException as e:
            print(e)
            coffeemachine.repair()

        
        
        
