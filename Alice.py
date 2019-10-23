import math

g = 0
x = 0
p = 0
gxp = 0
decimal_g = 0
decimal_x = 0
pow_of_g_with_x = 0

def Alice():
    inputdata = input(">>> Input g x p: ")
    gxp = inputdata.split()
    decimal_g = Transfer_to_decimal(gxp, 0)
    decimal_x = Transfer_to_decimal(gxp, 1)
    pow_of_g_with_x = Pow(decimal_g, decimal_x)
    binary_pow_of_g_with_x = Transfer_to_binary(pow_of_g_with_x)
    print (binary_pow_of_g_with_x)

def Transfer_to_decimal(gxp, num):
    decimal = int(gxp[num], 2)
    return decimal

def Pow(decimal_g, decimal_x):
    pow_of_g_with_x = pow(decimal_g, decimal_x)
    return pow_of_g_with_x

def Transfer_to_binary(pow_of_g_with_x):
    binary_pow_of_g_with_x = bin(pow_of_g_with_x)
    binary_pow_of_g_with_x = binary_pow_of_g_with_x.lstrip("0b")
    return binary_pow_of_g_with_x

Alice()