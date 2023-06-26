course = "Python for Beginners"
print(course.casefold())
print(course.split(' '))

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[-5] == names[0])
print(names[0:3])
names.append("Zaib")
names.insert(2, "Moeen")
print(names)
print(len(names))

for name in names:
    print(name)

numbers = range(5)
for num in numbers:
    print(num)