def maximum(d):
    key = max(d, key=d.get)
    return key

d = eval(input("Enter a dictionary: "))

result = maximum(d)

print("Key having maximum value is:", result)
