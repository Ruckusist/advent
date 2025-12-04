from utils import *

data = opener(3)
if False:
    data = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    data = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

def checker(line):
    proper = []
    sub = []
    for i in range(len(line)):
        if line[i:i+4] == "mul(":
            sub = []
            j = i + 4
            while j < len(line) and line[j] != ')':
                sub.append(line[j])
                j += 1
            if j < len(line) and line[j] == ')':
                args = ''.join(sub).split(',')
                if len(args) == 2 and args[0].isdigit() and args[1].isdigit():
                    a = int(args[0])
                    b = int(args[1])
                    proper.append((a, b))
    return proper

def p2_checker(line):
    proper = []
    bads = []
    sub = []
    flag = True
    for i in range(len(line)):
        if i < len(line) - 7:
            if line[i:i+7] == "don't()":
                # print("Found don't()")
                flag = False
        if i < len(line) - 4:
            if line[i:i+4] == "do()":
                # print("Found do()")
                flag = True
        # if not flag:
        #     continue
        if line[i:i+4] == "mul(":
            sub = []
            j = i + 4
            while j < len(line) and line[j] != ')':
                sub.append(line[j])
                j += 1
            if j < len(line) and line[j] == ')':
                args = ''.join(sub).split(',')
                if len(args) == 2 and args[0].isdigit() and args[1].isdigit():
                    a = int(args[0])
                    b = int(args[1])
                    if not flag:
                        bads.append((a, b))
                    else:
                        proper.append((a, b))
                    
    return proper, bads


proper = []
bads = []
for line in data:
    p, b = p2_checker(line)
    proper += p
    bads += b

print(f"Proper muls")
print(proper)
print(f"Bad muls")
print(bads)

# for pair in proper:
#     print(f"{pair[0]} * {pair[1]} = {pair[0] * pair[1]}")
print(f"Sum of all products: {sum(a * b for a, b in proper)}")

# first guess  168539636
# second guess 102631226     -- too high