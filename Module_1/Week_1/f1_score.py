
def calc_f1score(tp, fp, fn):

    #Check the data type of input
    if type(tp) != int:
        print('tp must be int')
        return
    
    if type(fp) != int:
        print('fp must be int')
        return
    
    if type(fn) != int:
        print('fn must be int')
        return

    #Check inputs are greater than zero

    if tp <= 0 or fp <= 0 or fn <=0:
        print('tp and fp and fn must be greater than zero')
        return

    #calc f1 score

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall / (precision + recall)) 

    print (f"Precision =  {precision}")
    print (f"Recall = {recall}")
    print (f"F1 Score = {f1_score}")

    
#Test 

calc_f1score(tp=2, fp=3, fn=4)
    
