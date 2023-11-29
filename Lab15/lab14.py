from math import sqrt


def computeMSE(observed, predicted):
    #TODO 1: Complete this function
    pass
    minus = []
    for i , j in zip(observed,predicted):
        value = i - j
        squared = value*value
        minus.append(squared)
        sumVAl = sum(minus)
        mse = sumVAl/len(observed)
    return mse

    

def computeRMSE(observed, predicted):
    #TODO 2: Complete this function
    pass
    minus = []
    for i , j in zip(observed,predicted):
        value = i - j
        squared = value*value
        minus.append(squared)
        sumVAl = sum(minus)
        mse = sumVAl/len(observed)
        rmse = sqrt(mse)
    return rmse
    

def computeMAE(observed, predicted):
    # TODO 3: Complete this function
    pass

    minus = []
    for i , j in zip(observed,predicted):
        value = i - j
        absoluteval = abs(value)
        minus.append(absoluteval)
        sumVAl = sum(minus)
        mae = sumVAl/len(observed)
    return mae


'''
TODO 4: Write driver code that calls the above methods and prints
the MSE, RMSE, and MAE for the following input. (Round
off the results to two decimal places)
    observed = 4,5,12,5,7
    predicted = 5,5,11,4,5
'''
observed = [4,5,12,5,7]
predicted = [5,5,11,4,5]
mse_result = computeMSE(observed, predicted)
rmse_result = computeRMSE(observed, predicted)
mae_result = computeMAE(observed, predicted)

print("MSE:", round(mse_result, 2))
print("RMSE:", round(rmse_result, 2))
print("MAE:", round(mae_result, 2))
#Driver code