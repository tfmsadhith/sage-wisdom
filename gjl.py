from numpy import random

for j in range(10000):
    y = list(map(lambda x : [float(x), float(1-x)], random.uniform(0,1, (1,10))[0]))
    
    sum_above = 0
    sum_below = 0
    
    for i in range(len(y)):
        if (sum_above + y[i][0]) < (sum_below + y[i][1]):
            sum_above += y[i][0]
        else:
            sum_below += y[i][1]
            
    print(sum_above, sum_below, (len(y) + 1) / 4)
            
    if (sum_above < ((len(y) + 1) / 4) and sum_below < ((len(y) + 1))):
        print("Passed")
    else:
        print("FAIL")
        break
            
    
  
        
