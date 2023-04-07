# Waterloo CCC 2023 Junior 2 Chili Peppers

spice = 0

#num of peppers
peprs = int(input())

for i in range(peprs):
    currpepr = input()
    if currpepr == 'Poblano':
        spice += 1500
    elif currpepr == 'Mirasol':
        spice += 6000
    elif currpepr == 'Serrano':
        spice += 15500
    elif currpepr == 'Cayenne':
        spice += 40000
    elif currpepr == 'Thai':
        spice += 75000
    elif currpepr == 'Habanero':
        spice += 125000

print(spice)