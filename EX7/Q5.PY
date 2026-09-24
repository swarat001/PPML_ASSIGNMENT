#WAP TO CONVERT A GIVEN LIST OF INTEGER AND A TUPLE OF INTEGER IN A LIST OF STRING USING MAP()

list1 = [1, 2, 3, 4, 5]
tuple1 = (6, 7, 8, 9, 10)

result1 = list(map(str, list1))
result2 = list(map(str, tuple1))

print("List of strings:", result1)
print("Tuple of strings:", result2)
