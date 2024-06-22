# f[0] = [] empty list
# f[1] = [0] list

# Fn = Fn-1 + Fn-2

input = int(input("enter your number"))

def fibonacii(input):
    if input < 0 :
        print("enter postive number")
    if input == 0:
        return []
    if input == 1:
        return [0]
    series = [0,1]
    for i in range(0,input):
        nums = series[-1] + series[-2]
        series.append(nums)
    return series
result = fibonacii(input)
print(result)



