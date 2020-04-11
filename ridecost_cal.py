#ride cost calculator

Distance = int(input("How many km are you going Travel :"))

Avg = int(input("Your vehicle Fuel Average is :"))

Cost = float(input(" Cost of Diesel is :"))

fuelCost= (Distance/Avg)

totalCost = fuelCost * Cost

print("The cost of driving per day to office :", totalCost)
