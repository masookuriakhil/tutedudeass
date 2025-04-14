
num = int(input("Enter your any factorical: "))

def my_factorial(num):
    if num < 2:
        return 1
    else:
        return num * my_factorial(num-1)
result = my_factorial(num)
print(result)