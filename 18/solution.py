#!/usr/bin/env python3

f = open('SecretRecipe.txt', 'r')
lines = f.readlines()
f.close()


d = {}

flag = ''

for line in lines:
    # Ingredients.
    if line[0] >= '0' and line[0] <= '9':
        parts = line.split()
        ascii_code = int(parts[0])
        ingredient = ' '.join(parts[2:])
        d[ingredient] = ascii_code

    # Method.
    if line.startswith('Put'):
        ingredient = line.replace('Put ', '').split(' into')[0]
        flag += chr(d[ingredient])

# Liquefy contents of the mixing bowl.
# Pour contents of the mixing bowl into the baking dish.
print(flag[::-1])
