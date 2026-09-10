def copy_set(s):
    new_set = set()

    for i in s:
        new_set.add(i)

    return new_set


s = eval(input("Enter a set: "))

new_set = copy_set(s)

print("New set:", new_set)
