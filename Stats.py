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
def calculateStandardErrorMean(data):
    return np.std(data)/np.sqrt(len(data))

## Confidence interval for population mean (95%) ##
def calculateConfidenceIntervalMean(data):
    return f"{np.mean(data)} +/- {1.96*(np.std(data)/np.sqrt(len(data)))}"

## Standard Error of proportion ##
# p = proportion
def calculateStandardErrorProportion(data,p):
    return np.sqrt(p*(1-p)/len(data))

## Confidence interval for proportion (95%) ##
# p = proportion
# n = sample size
def calculateConfidenceIntervalProportion(p,n):
    return f"{p} +/- {1.96*np.sqrt(p*(1-p)/n)}"

## Agresti-Coull interval for proportion (95%) ##
# p = proportion
# n = sample size
def calculateAgrestiCoullInterval(p,n):
    p2 = (p*n+2)/(n+4)
    n2 = n+4
    x = (1.96*np.sqrt(p2*(1-p2)/n2))
    return f"{p2} +/- {x}"

## Sample size for mean (95%) ##
# s = Expected sample variance
# e = Desired margin of error (eg. 0.05 as 5% margin of error)
def calculateSampleSizeMean(s,e):
    return (1.96**2)*(s**2/e**2)

## Sample size for proportion (95%) ##
# p = Expected proportion (Worst case scenaria: 0.5)
# e = Desired margin of error (eg. 0.05 as 5% margin of error)
def calculateSampleSizeProportion(p,e):
    return (1.96**2)*(p*(1-p)/e**2)

## Covariance ##
data = np.array([])
cov = np.cov(data)