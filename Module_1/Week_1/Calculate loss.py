import math
import random

def MAE(predict, target):
    return abs(predict - target)

def MSE(predict, target):
    return (predict - target)**2

def compute_lossfunction():
   
    num_samples = input("Input numbers of samples: ")

    if (num_samples.isnumeric == False):
        print("Number of samples must be int")
        return
    
    num_samples = int(num_samples)

    predicts = [random.uniform(0, 10) for _ in range(num_samples)]
    targets = [random.uniform(0, 10) for _ in range(num_samples)]

    loss_name = input('Input loss funtion name:')

    LOSS_FUNCTION = ['MAE', 'MSE', 'RMSE']
    if loss_name in LOSS_FUNCTION:
        
        sum_loss = 0
        for i in range(num_samples):
            output_str = f"loss name: {loss_name}, "
            predict = predicts[i]
            target = targets[i]
            
            if loss_name == 'MAE':
                loss = MAE(predict, target)
            elif loss_name == 'MSE':
                loss = MSE(predict, target)
            elif loss_name == 'RMSE':
                loss = math.sqrt(MSE(predict, target))

            output_str += f'sample: {i}, pred: {predict}, target: {target}, loss: {loss}'
            print(output_str)

            sum_loss += loss
        
        final_loss = sum_loss / num_samples
        print(f"final {loss_name}: {final_loss}")
    else:
        print('Loss funtion invalid')

compute_lossfunction()