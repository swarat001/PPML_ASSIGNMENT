#WAP TO CREATE A LIST CONTAINING THE POWER OF SAID NUMBER IN BASES RAISED TO THE CORRESPONDING NUMBER IN THE INDEX USING PYTHON MAP
numbers = [2, 3, 4, 5]

result = list(map(lambda x, i: x ** i, numbers, range(len(numbers))))

print("Result:", result)
