import numpy as np

## Mean ##

## Standard Deviation ##

## Variance ##

## Sample estimator of standard deviation ##

## Standard Error of mean ##

## Confidence interval for population mean (95%) ##
def calculateConfidenceIntervalMean(data):
    return 1.96*(np.std(data)/np.sqrt(len(data)))

## Standard Error of proportion ##

## Confidence interval for proportion (95%) ##
# p = proportion
# n = sample size
def calculateConfidenceIntervalProportion(p,n):
    1.96*np.sqrt(p*(1-p)/n)

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
