checkList = []
checkList.append(float(input('Enter the charge for the food.')))
#Any gratuity that is automatically imposed is considered a service fee and is subject to sales tax.
checkList.append(checkList[0] * 0.18)
checkList.append((checkList[0] + checkList[1]) * 0.07)
print('The amount of gratuity is ' + str(checkList[1]))
print('The amount of sales tax is ' + str(checkList[2]))
checkTotal = 0
counter = 0
while counter < len(checkList):
    checkTotal = checkTotal + checkList[counter]
    counter += 1
print('The total with gratuity and sales tax added is $' + str(round(checkTotal,2)))

timeList = []
timeList.append(float(input('Enter the current time in hours. ')))
timeList.append(float(input('Enter how long the alarm should wait. ')))

counter = 0 
while counter <= timeList[1]:
    timeList[0]+=1
    if timeList[0] == 25:
        timeList[0] = 0
    counter += 1

print('The alarm will sound at ' + str(int(timeList[0])))

