def combine_sets(s1, s2):
    new_set = set()

    for i in s1:
        new_set.add(i)

    for i in s2:
        new_set.add(i)

    return new_set


s1 = eval(input("Enter first set: "))
s2 = eval(input("Enter second set: "))

result = combine_sets(s1, s2)

print("New set:", result)
