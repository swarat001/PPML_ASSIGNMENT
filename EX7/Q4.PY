#WAP TO CONVERT ALL THE CHARACTERS INTO UPPERCASE AND LOWERCASE AND ELIMINATE DUPLICATE LETTERS FROM A GIVEN SEQUENCE USE MAP() FUNCTION 
sequence = "HelloWorld"

unique = list(dict.fromkeys(sequence))

uppercase = list(map(str.upper, unique))
lowercase = list(map(str.lower, unique))

print("Original sequence:", sequence)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
