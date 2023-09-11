def sumDigits(sum):
    if sum < 10:
        return sum
    else:
        digit = sum % 10
        return digit + sumDigits(sum // 10)

Inputer= int(input("Enter an integer: "))
result = sumDigits(Inputer)
print(f"The sum of the digits in {Inputer} is {result}.")
enter = []
