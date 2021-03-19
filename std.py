import statistics


array = [1,2,1,3,2,3,4,1,2,20]
# takes array as a parameter returns array, crazy simple std oriented anomaly detection func.
def anomaly_detector(numberArray):
    resultArray = []
    std=statistics.stdev(numberArray)
    upperBoundry = statistics.mean(numberArray) + (2*std)
    lowerBoundry = statistics.mean(numberArray) - (2*std)
    print(std,upperBoundry,lowerBoundry)
    for number in numberArray:
        if number<upperBoundry and number>lowerBoundry:
            resultArray.append(1) #not anomaly
        else:
            resultArray.append(-1) # anomaly

    return resultArray

print(anomaly_detector(array))
