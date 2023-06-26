def mygenerator(x):
    for i in range(x):
        yield i ** 3

values = mygenerator(100)

# to print single value from generator
print(next(values))

# to print all values from generator
for i in values:
    print(i)