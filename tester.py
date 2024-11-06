import geo.utils as utils

# calculate the length of hypothenuse(c) when a = 3, b = 4
a, b = 3, 4
c = utils.pythagoras(a, b) 
print(f'c = {c}')

# calculate the area of circle with radius r = 10
r = 10
area = utils.circle(r)
print(f'area = {area}')