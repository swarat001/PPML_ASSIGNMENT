def merge(d1, d2):
    d1.update(d2)
    return d1

d1 = eval(input("Enter first dictionary: "))
d2 = eval(input("Enter second dictionary: "))

d3 = merge(d1, d2)

print("Merged dictionary:", d3)
print("Values:", d3.values())
