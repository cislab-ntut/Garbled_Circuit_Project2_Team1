class Wire:
    def __init__(self, number):
        self.number = number
        self.value = 0


class Gate:
    def __init__(self, inWire0, inWire1, outWire2, truthTable):
        self.inputWire0 = inWire0
        self.inputWire1 = inWire1
        self.outputWire = outWire2
        self.truthTable = truthTable

    def compute(self, input0, input1):
        for i in self.truthTable.truthTable:
            if input0 == i[0] and input1 == i[1]:
                return i[2]


class TruthTable:
    def __init__(self, row0, row1, row2, row3):
        self.truthTable = [row0, row1, row2, row3]


# ----- Implement garbled truth table here ------
truthTable0 = TruthTable([0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 0])  # Example Truth Table

wire0 = Wire('w0')
wire1 = Wire('w1')
wire2 = Wire('w2')
wire3 = Wire('w3')
wire4 = Wire('w4')
wire5 = Wire('w5')
wire6 = Wire('w6')
wire7 = Wire('w7')
wire8 = Wire('w8')
wire9 = Wire('w9')
wire10 = Wire('w10')
wire11 = Wire('w11')
gate0 = Gate('w0', 'w1', 'w4', truthTable0)
gate1 = Gate('w1', 'w2', 'w5', truthTable0)
gate2 = Gate('w0', 'w1', 'w6', truthTable0)
gate3 = Gate('w4', 'w3', 'w7', truthTable0)
gate4 = Gate('w5', 'w3', 'w8', truthTable0)
gate5 = Gate('w4', 'w3', 'w9', truthTable0)
gate6 = Gate('w9', 'w6', 'w10', truthTable0)
gate7 = Gate('w8', 'w10', 'w11', truthTable0)

g0, g1, x1, x2 = 1, 1, 1, 1  # Set input value
wire0.value = g0
wire1.value = g1
wire2.value = x1
wire3.value = x2


wire4.value = gate0.compute(wire0.value, wire1.value)
wire5.value = gate1.compute(wire1.value, wire2.value)
wire6.value = gate2.compute(wire0.value, wire1.value)
wire7.value = gate3.compute(wire4.value, wire3.value)  # Output 2^1 bit
wire8.value = gate4.compute(wire5.value, wire3.value)
wire9.value = gate5.compute(wire4.value, wire3.value)
wire10.value = gate6.compute(wire9.value, wire6.value)
wire11.value = gate7.compute(wire8.value, wire10.value)  # Output 2^0 bit

print(wire7.value,wire11.value)
