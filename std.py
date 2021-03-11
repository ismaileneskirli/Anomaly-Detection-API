import statistics

# takes dict as a parameter returns array, crazy simple std oriented anomaly detection func.
def std_anomaly_detect(sample):
    numberArray = []
    for key in sample.keys():
        numberArray.append(sample[key])
    resultArray = []
    std=statistics.stdev(numberArray)
    upperBoundry = statistics.mean(numberArray) + 2*std
    lowerBoundry = statistics.mean(numberArray) - 2*std

    for number in numberArray:
        if number<upperBoundry and number>lowerBoundry:
            resultArray.append(1) #not anomaly
        else:
            resultArray.append(-1) # anomaly

    return resultArray

# same function but returns a dictionary
def detect_anomalies(sample):
    numberArray = []
    for key in sample.keys():
        numberArray.append(sample[key])
    std=statistics.stdev(numberArray)
    upperBoundry = statistics.mean(numberArray) + 2*std
    lowerBoundry = statistics.mean(numberArray) - 2*std
    resultDict = {}
    i = 0
    for number in numberArray:
        if number<upperBoundry and number>lowerBoundry:
            resultDict[i] = 1
        else:
            resultDict[i] = -1 # anomaly
        i += 1
    return resultDict