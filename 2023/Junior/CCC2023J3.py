# Waterloo CCC 2023 Junior 3 Special Event

guests = int(input()) #num of guests
alist = [] #input to be formatted into list of strings

d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0

for i in range(guests):
    availability = input() #availability of the individual
    alist.append(availability)

    if availability[0] == 'Y':
        d1 += 1
    if availability[1] == 'Y':
        d2 += 1
    if availability[2] == 'Y':
        d3 += 1
    if availability[3] == 'Y':
        d4 += 1
    if availability[4] == 'Y':
        d5 += 1

days = [d1,d2,d3,d4,d5]
highest = max(days)


output = ""

if d1 == highest:
    output = output + "1"

if d2 == highest and output == "":
    output = output + "2"
elif d2 == highest:
    output = output + ",2"

if d3 == highest and output == "":
    output = output + "3"
elif d3 == highest:
    output = output + ",3"

if d4 == highest and output == "":
    output = output + "4"
elif d4 == highest:
    output = output + ",4"

if d5 == highest and output == "":
    output = output + "5"
elif d5 == highest:
    output = output + ",5"

print(output)
