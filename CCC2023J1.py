# Waterloo CCC 2023 Junior 1 Deliv-e-droid
pack = int(input())
coll = int(input())
points = pack * 50 - coll * 10
if pack > coll:
    points+=500
print(points)
