def squares():
    n = 1
    while n <= 5:
        yield n
        n = n+1


values = squares()

print(values)
print(next(values))
print(next(values))
