def raise_to_power(base,power)
    result=1
    for index in range(power)
        result*=base
    return result
base=int(iput("Enter the Base:"))
power=int(input("Enter the Power:"))
print(raise_to_power(base,power))
