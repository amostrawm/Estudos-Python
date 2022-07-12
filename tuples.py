import math

p1 = (23, -88)
p2 = (6, 42)

#your code goes here
xd = (p1[0] - p2[0])
xdistance = xd

yd = (p1[1] - p2[1])
ydistance = yd

linear_distance = math.sqrt((xd**2)+(yd**2))
print(linear_distance)