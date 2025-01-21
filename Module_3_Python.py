checkTotal = float(input('Enter the charge for the food.'))
#Any gratuity that is automatically imposed is considered a service fee and is subject to sales tax.
gratuityAdded = checkTotal * 1.18
salesTaxAdded = gratuityAdded * 1.07
print('The total with gratuity added is $' + str(round(gratuityAdded,2)))
print('The total with gratuity and sales tax added is $' + str(round(salesTaxAdded,2)))

currentTime = float(input('Enter the current time in hours. '))
waitTime = float(input('Enter how long the alarm should wait. '))

if (currentTime + waitTime) < 24:
    timeToSound = currentTime + waitTime
else:
    timeToSound = (currentTime + waitTime) % 24

if timeToSound < 12:
    timeOfDay = 'AM'
else:
    timeOfDay = 'PM'

print('The alarm will sound at ' + str(int(timeToSound)) + timeOfDay)

