import math


def calc_sigmoid (x):
    y = 1 / (1 + math.exp(-x))
    return y

def calc_relu (x):
    if x <= 0:
        return 0
    return x

def calc_elu (x, alpha = 0.001):
    if x <= 0:
        y  = alpha * (math.exp(x) - 1)
        return y
    return x


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def compute_activation_func (x, name_actfunc):
    
    #check input value
    if (is_number(x) == False):
        print ("x must be number")
        return

    if name_actfunc == 'sigmoid':
        print (f"Sigmoid f(x) = {calc_sigmoid(x)}")
    elif name_actfunc == 'relu':
        print (f"Relu f(x) = {calc_relu(x)}")
    elif name_actfunc == 'elu':
        print (f"Elu f(x) = {calc_elu(x)}")
    else: print ("This activation function is not supported")

#Test

compute_activation_func(5,'elu')
