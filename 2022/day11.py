import os
from collections import namedtuple

Operation = namedtuple('Operation', ['arg1', 'arg2', 'operator'])

def add(a: int, b: int) -> int:
    return a + b
def subtract(a: int, b: int) -> int:
    return a - b
def multiply(a: int, b: int) -> int:
    return a * b
def divide(a: int, b: int) -> int:
    return a / b
    
def getOpArg(arg: str) -> str | int:
    return 'worry' if arg == 'old' else int(arg)
def getOpObj(operation: str) -> Operation:
    opSplit = operation.split(' ')
    operation = None
    if opSplit[1] == '+':
        operation = add
    elif opSplit[1] == '-':
        operation = subtract
    elif opSplit[1] == '*':
        operation = multiply
    else: # opSplit[1] == '/'
        operation = divide
    return Operation(
        arg1=getOpArg(opSplit[0]),
        operator=operation,
        arg2=getOpArg(opSplit[2]))

class Monkey:
    items = []
    operation = namedtuple
    divisor = None
    testTrue = None
    testFalse = None
    inspectionCount = 0

    def inspectItem(self, item: int, reduceWorry: bool=True) -> int:
        """
        does nothing if the monkey has no items
        does the monkey's operation on the first item in its list,
        whatever that entails.
        this operation removes the item from the monkey's list and
        does the worry-reduction at the end, finally returning the
        item's final worry value
        """
        self.inspectionCount += 1
        item = self.operation.operator(
            item if self.operation.arg1 == 'worry' else self.operation.arg1,
            item if self.operation.arg2 == 'worry' else self.operation.arg2)
        return item//3 if reduceWorry else item
    
    def clearItems(self):
        self.items = []
    
    def getRecipient(self, item: int) -> int:
        """
        gets the monkey recipient for the item based on this
        monkey's divisibility test and stated test results
        """
        return self.testTrue if item%self.divisor == 0 else self.testFalse

    def receiveItem(self, item: int):
        """add the item to the monkey's list of items"""
        self.items.append(item)        
    
    def __repr__(self):
        return "Monkey()"
    
    def __str__(self):
        return f'Items: {", ".join(list(map(str, self.items)))}\n' + \
            f'Operation: {self.operation}\n' + \
            f'Test: divisible by {self.divisor}\n' + \
            f'Throw to {self.testTrue} if test returns true, else throw to {self.testFalse}'

def calcMonkeyBusiness(monkeys: [Monkey]) -> int:
    monkeys.sort(reverse=True, key=lambda monkey: monkey.inspectionCount)
    return monkeys[0].inspectionCount * monkeys[1].inspectionCount

monkeys = []
input = open(os.path.join(os.getcwd(), "inputs/input11.txt"))
for monkey in input.read().split('\n\n'):
    monkeyLines = monkey.split('\n')
    currMonkey = Monkey()
    # ok this looks DISGUSTING
    # but it works and i don't want to write 5098240 functions
    currMonkey.items = list(map(int, monkeyLines[1].strip().split(': ')[1].split(',')))
    currMonkey.operation = getOpObj(monkeyLines[2].strip().split(' = ')[1])
    currMonkey.divisor = int(monkeyLines[3].strip().split(' ')[-1])
    currMonkey.testTrue = int(monkeyLines[4].strip().split(' ')[-1])
    currMonkey.testFalse = int(monkeyLines[5].strip().split(' ')[-1])
    monkeys.append(currMonkey)
input.close()

pt1Monkeys = monkeys.copy()
for i in range(20):
    for monkey in pt1Monkeys:
        for item in monkey.items:
            itemVal = monkey.inspectItem(item)
            recipient = monkey.getRecipient(itemVal)
            pt1Monkeys[recipient].receiveItem(itemVal)
        monkey.clearItems()

for i in range(10000):
    if i%100:
        print(f'{i} of 9999')
    for monkey in monkeys:
        for item in monkey.items:
            itemVal = monkey.inspectItem(item, reduceWorry=False)
            recipient = monkey.getRecipient(itemVal)
            monkeys[recipient].receiveItem(itemVal)
        monkey.clearItems()
part1, part2 = calcMonkeyBusiness(pt1Monkeys), calcMonkeyBusiness(monkeys)
assert part1 == 120756, f'Part 1: expected 120756 but got {part1}'
# assert part2 == 0, f'Part 2: expected 0 \n but got \n {part2}'
print("part 1: ", part1)
print("part 2: ", part2)