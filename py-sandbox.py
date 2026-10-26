'''

- Listcomps vs map and filter functions -

symbols = '@#$%&'

beyond_ascii = [ord(s) for s in symbols if ord(s) > 30]

beyond_ascii = list(filter(lambda c: c > 30, map(ord, symbols)))

print(beyond_ascii)



- Cartesian product using a list comprehension -

colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color, size) for color in colors for size in sizes] <-- approach 1

for color in colors:                        
    for size in sizes:                   <-- approach 2
        print((color, size))                

print(tshirts)


'''

class sophomore:
    
    minAge = 19
    maxAge = 20
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

stud1 = sophomore("Anant", 19)
print(stud1.name, stud1.age, stud1.minAge, stud1.maxAge, sophomore.minAge)





