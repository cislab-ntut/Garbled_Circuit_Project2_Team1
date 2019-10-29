import random
import Circuit

# Generate garbled truth tables
truthTable0 = [[0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 0]]
gate0Input0 = bin(random.randint(0, 9999))
gate0Input1 = bin(random.randint(0, 9999))
gate0Output0 = bin(random.randint(0, 9999))
gate0Output1 = bin(random.randint(0, 9999))
garbledTruthTable0 = [[gate0Input0, gate0Input0, gate0Output0], [gate0Input0, gate0Input1, gate0Output0],
                      [gate0Input1, gate0Input0, gate0Output1], [gate0Input1, gate0Input1, gate0Output0]]

truthTable1 = [[0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 0]]
garbledTruthTable1 = [[gate0Input0, gate0Input0, gate0Output0], [gate0Input0, gate0Input1, gate0Output0],
                      [gate0Input1, gate0Input0, gate0Output1], [gate0Input1, gate0Input1, gate0Output0]]

truthTable2 = [[0, 0, 0], [1, 0, 0], [0, 1, 1], [1, 1, 0]]
gate2Output0 = bin(random.randint(0, 9999))
gate2Output1 = bin(random.randint(0, 9999))
garbledTruthTable2 = [[gate0Input0, gate0Input0, gate2Output0], [gate0Input0, gate0Input1, gate2Output1],
                      [gate0Input1, gate0Input0, gate2Output0], [gate0Input1, gate0Input1, gate2Output0]]

truthTable3 = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]]
gate3Output0 = bin(random.randint(0, 9999))
gate3Output1 = bin(random.randint(0, 9999))
garbledTruthTable3 = [[gate0Output0, gate0Output0, gate3Output0], [gate0Output0, gate0Output1, gate3Output0],
                      [gate0Output1, gate0Output0, gate3Output0], [gate0Output1, gate0Output1, gate3Output1]]

truthTable4 = [[0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 0]]
gate4Output0 = bin(random.randint(0, 9999))
gate4Output1 = bin(random.randint(0, 9999))
garbledTruthTable4 = [[gate0Output0, gate0Output0, gate4Output0], [gate0Output0, gate0Output1, gate4Output0],
                      [gate0Output1, gate0Output0, gate4Output1], [gate0Output1, gate0Output1, gate4Output0]]

truthTable5 = [[0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 0]]
garbledTruthTable5 = [[gate0Output0, gate0Output0, gate2Output0], [gate0Output0, gate0Output1, gate2Output0],
                      [gate0Output1, gate0Output0, gate2Output1], [gate0Output1, gate0Output1, gate2Output0]]

truthTable6 = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
garbledTruthTable6 = [[gate2Output0, gate2Output0, gate4Output0], [gate2Output0, gate2Output1, gate4Output1],
                      [gate2Output1, gate2Output0, gate4Output1], [gate2Output1, gate2Output1, gate4Output1]]

truthTable7 = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
gate7Output0 = bin(random.randint(0, 9999))
gate7Output1 = bin(random.randint(0, 9999))
garbledTruthTable7 = [[gate4Output0, gate4Output0, gate7Output0], [gate4Output0, gate4Output1, gate7Output1],
                      [gate4Output1, gate4Output0, gate7Output1], [gate4Output1, gate4Output1, gate7Output1]]

garbledTruthTableList = [garbledTruthTable0, garbledTruthTable1, garbledTruthTable2, garbledTruthTable3,
                         garbledTruthTable4, garbledTruthTable5, garbledTruthTable6, garbledTruthTable7]

g0 = int(input("Input g0: "))
g1 = int(input("Input g1: "))
x0 = int(input("Input x0: "))
x1 = int(input("Input x1: "))

# Garble input numbers
if g0 == 0:
    g0 = gate0Input0
elif g0 == 1:
    g0 = gate0Input1

if g1 == 0:
    g1 = gate0Input0
elif g1 == 1:
    g1 = gate0Input1

if x0 == 0:
    x0 = gate0Input0
elif x0 == 1:
    x0 = gate0Input1

if x1 == 0:
    x1 = gate0Output0
elif x1 == 1:
    x1 = gate0Output1

# Send the GTTs & garbled inputs to server and get result
result = Circuit.createGarbledCircuit(garbledTruthTableList, g0, g1, x0, x1)

# Transform the garbled outputs into normal outputs
print "\nResult:"
if result[0] == gate3Output0:
    print('2^1: 0')
elif result[0] == gate3Output1:
    print('2^1: 1')

if result[1] == gate7Output0:
    print('2^0: 0')
elif result[1] == gate7Output1:
    print('2^0: 1')
