persons = [
    {'name': 'john', 'age': 19},
    {'name': 'pail', 'age': 21},
    {'name': 'haha', 'age': 22},
    {'name': 'kerl', 'age': 24},
    {'name': 'anna', 'age': 23}
]

print("name\tage")
for person in persons:
    print('%s\t%d' % (person["name"], person['age']))

age = input("Enter an age to find: ")
for person in persons:
    if person['age'] == int(age):
        print('%s\t%d' % (person["name"], person['age']))
