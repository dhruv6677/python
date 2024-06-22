input = int(input("enter your number"))
def fibonacci(input):
    if input <= 0:
        print("Input should be positive integer")
    if input == 1:
        return []
    if input == 1:
        return [0]
    series = [0,1]
    for i in range(2,input):
        num = series[-1] + series[-2]
        series.append(num)
    return series
result = fibonacci(input)
print(result)

