def set_operations(a, b):
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference:", a - b)
    print("Difference:", b - a)
    print("Symmetric Difference:", a ^ b)


s1 = eval(input("Enter first set: "))
s2 = eval(input("Enter second set: "))

set_operations(s1, s2)