import lists_generator

a = lists_generator.generate()

b = a

a.pop()
print(b)

print(a is b)
print(id(a))
print(id(b))
