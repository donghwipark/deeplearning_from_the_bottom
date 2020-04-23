from perceptron_AND import AND
from perceptron_OR import OR
from perceptron_NAND import NAND

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print("1.", XOR(0, 0))
print("2.",XOR(0, 1))
print("3.",XOR(1, 0))
print("4.",XOR(1, 1))