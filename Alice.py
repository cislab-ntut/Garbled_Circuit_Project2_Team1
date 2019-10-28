import math

C = 0
k_3 = 0
g = 0
x = 0
p = 0
i = 1 #CAS呼叫次數
j = 1 #XOR呼叫次數
gxp = 0
decimal_g = 0
decimal_x = 0
pow_of_g_with_x = 0

def Alice(i):
    k = input(">>> Input k: ")
    k_3 = 3 * k;
    inputdata = input(">>> Input g x p: ")
    gxp = inputdata.split()
    decimal_g = Transfer_to_decimal(gxp, 0)
    decimal_x = Transfer_to_decimal(gxp, 1)
    pow_of_g_with_x = Pow(decimal_g, decimal_x)
    binary_pow_of_g_with_x = Transfer_to_binary(pow_of_g_with_x)
    CAS(binary_pow_of_g_with_x, gxp[2], C)
    #print (binary_pow_of_g_with_x)
    
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


def CAS(A, B, C):
    i = i + 1
    if (i <= 9 * pow(k_3, 2)):
        return CAS(A, B, C)

    XOR(A, B)
    #if (i > 9 * pow(k_3, 2)):
     #   return 0
    #return CAS(A, B, C)




def XOR(A, B):
    buffer_i = i
    buffer_i = buffer_i - 1
    control = 0
    buffer1 = 0
    buffer2 = 0
    buffer = 0
    if (int(B[buffer_i]) == 0 or control - 1 == 0):
        buffer1 = 0
    else:
        buffer1 = 1
    if (int(B[buffer_i]) - 1 == 0 or control == 0):
        buffer2 = 0
    else:
        buffer2 = 1
    if (buffer1 == 1 or buffer2 == 1):
        buffer = 1
    else:
        buffer = 0

    j = j + 1
    if (j > 3):
        return buffer
    elif (j == 2):
        return XOR(A, bufer)
    elif (j == 3):
        return XOR(C, buffer)

def AND():
    pass

Alice()
