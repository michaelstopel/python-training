from matrix import Matrix
a = Matrix(((1,2), (3,4)))
b = Matrix(((1,2), (3,5)))
print(a + b.ones(2))
print(b.ones(2)+a)
print(a+b)
print(a - b.ones(2))
print(b.ones(2)-a)
print(a-b)
print(10*a)
print(a/100)
print(a.unity(6))
if a == b:
    print(a.ones(6))

for line in a.tuples():
    print(line)
dictionary = {}
dictionary[Matrix(((1, 1), (2, 2)))] = 1
dictionary[Matrix(((1, 1), (2, 2)))] = 2
dictionary[Matrix(((1, 1), (2, 3)))] = 3
print(dictionary)