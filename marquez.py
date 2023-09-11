import math
coins = float(input("Please Enter "))
Quarters = 25
Dimes = 10
Nickels = 5
Pennies = 1
MaxQuarters = math.floor(coins/Quarters)
Total_Amount = coins - MaxQuarters*25
MaxDimes = math.floor(Total_Amount/Dimes)
Total_Amount2 = Total_Amount - MaxDimes*10
MaxNickels = math.floor(Total_Amount2/Nickels)
Total_Amount3 = Total_Amount2 - MaxNickels*5
MaxPennies = math.floor(Total_Amount3/Pennies)
Total_Amount4 = Total_Amount3 - MaxPennies*1

print(f'Coins: , {MaxQuarters} quarters, {MaxDimes} dimes ,{MaxNickels} Nickels,{MaxPennies} pennies')