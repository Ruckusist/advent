from utils import *

data = opener(1).splitlines()
if False:
    example = """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""
    data = example.strip().splitlines()
x = []
y = []
for line in data:
    a, b = map(int, line.split())
    x.append(a)
    y.append(b)

z = []
for a, b in zip(sorted(x), sorted(y)):
    z.append(abs(a - b))


# print(sum(z))
## Answer to part 1 is 1319616  | Time was 8 mins.
 
# part 2
z = []
for a in x:
    b = y.count(a)
    z.append(a * b)
print(sum(z))

# Answer to part 2 is 27267728 | time was total of 15 mins.