import numpy as np

## Mean ##
data = np.array([])
mean = np.mean(data)

## Standard Deviation ##
data = np.array([])
std = np.std(data)

## Variance ##
data = np.array([])
var = np.std(data)**2

## Sample estimator of standard deviation ##
data = np.array([])

def seStd(data):
    n = 0
    for e in data:
        n += (e-np.mean(data))**2
    n = n/(len(data)-1)
    n = np.sqrt(n)
    return n

samstd = seStd(data)



## Standard Error of mean ##

## Confidence interval for population mean (95%) ##

## Standard Error of proportion ##

## Confidence interval for proportion (95%) ##

## Agresti-Coull interval for proportion (95%) ##

## Sample size for mean (95%) ##

## Sample size for proportion (95%) ##

