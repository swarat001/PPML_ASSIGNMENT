def remove_duplicate(d):
    new = {}

    for key, value in d.items():
        if value not in new.values():
            new[key] = value

    return new


d = eval(input("Enter a dictionary: "))

result = remove_duplicate(d)

print("Dictionary after removing duplicate values:", result)