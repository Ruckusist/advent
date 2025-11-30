from utils import *

data = opener(2)

if False:
    data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    data = data.strip().split('\n')

if False:
    new = {}
    for ele, line in enumerate(data):
        nums = list(map(int, line.split()))
        crease = None
        safe = True
        for i in range(len(nums)-1):
            if not safe: break
            a, b = nums[i], nums[i+1]
            n_crease = None
            if not crease:
                if a < b: crease = 'up'
                elif a > b: crease = 'down'
                if abs(a - b) > 3:
                    print(f"#debug1 {ele}")
                    safe = False
                if a == b:
                    print(f"#debug2 {ele}")
                    safe = False
                continue
            if a < b: n_crease = 'up'
            elif a > b: n_crease = 'down'

            if n_crease != crease:
                print(f"#debug3 {ele}")
                safe = False
            if abs(a - b) > 3:
                print(f"#debug4 {ele}")
                safe = False
            if a == b:
                print(f"#debug5 {ele}")
                safe = False

        new[ele] = {'safe': safe, 'nums': nums, 'line': line, 'crease': crease}

    if True:
        for k, v in new.items():
            print(f"Line {k+1}: {v['line']} | Safe: {v['safe']} | Crease: {v['crease']}")

    safety = sum([1 for k, v in new.items() if v['safe']])
    print(f"Total safe lines: {safety}")

# The answer 323 is too high and wrong.
# the answer 103 is too low and wrong, and was just >= 3 instead of just > 3
# The answer 257 is correct! i had to add in a != b and then remove >= 3 to just > 3 that was a terrible idea.
# this took about 45 mins to solve part 1. will break before part 2.


# PART 2.
# print(data)
new = {}
for ele, line in enumerate(data):
    nums = list(map(int, line.split()))
    new[ele] = {'line': line, 'nums': nums}

# for k, v in new.items():
#     print(f"{k}: {v}")

def checker(nums):
    safe = True
    crease = None
    for i in range(len(nums)-1):
        if not safe: break
        a, b = nums[i], nums[i+1]
        if not crease:
            if a < b: crease = 'up'
            elif a > b: crease = 'down'
            # check no more than 3 diff
            if abs(a - b) > 3:
                safe = False
            # check that there is a diff
            if a == b:
                safe = False
            continue

        n_crease = None
        if a < b: n_crease = 'up'
        elif a > b: n_crease = 'down'

        # make sure crease is same
        if n_crease != crease:
            safe = False
        # check no more than 3 diff
        if abs(a - b) > 3:
            safe = False
        # check that there is a diff
        if a == b:
            safe = False
    return safe, i


safety = 0
# with open("/home/dude/advent/advent/2024/day2_debug.txt", 'w') as f:
#     for k, v in new.items():
#         # print("----------------------")
#         # print(f"Line {k}: {v['nums']}\n")
#         nums = v['nums']
#         safe, idx = checker(nums)
#         if not safe:
#             print("\n----------------------", file=f)
#             print(f"Line {k}: {v['nums']}\n", file=f)
#             print(f"Original nums: {nums}", file=f)
#             new_nums = nums.copy()
#             print(f"NOT SAFE! review broke on idx:{idx}", file=f)
#             new_nums.pop(idx-1)
#             print(f"Removed {nums[idx-1]} at index {idx-1} | New nums: {new_nums}", file=f)
#             new_safe, new_idx = checker(new_nums)
#             if not new_safe:
#                 print(f"Still not safe, damned thing! idx:{new_idx}", file=f)
#                 new_new_nums = nums.copy()
#                 new_new_nums.pop(idx)
#                 print(f"Trying removing {nums[idx]} at index {idx} | New nums: {new_new_nums}", file=f)
#                 new_new_safe, new_new_idx = checker(new_new_nums)
#                 if not new_new_safe:
#                     print(f"Ugh, still not safe on idx:{new_new_idx}!", file=f)
#                     new_new_new_nums = nums.copy()
#                     new_new_new_nums.pop(idx+1)
#                     print(f"Trying removing {nums[idx+1]} at index {idx+1} | New nums: {new_new_new_nums}", file=f)
#                     new_new_new_safe, new_new_new_idx = checker(new_new_new_nums)
#                     if not new_new_new_safe:
#                         print(f"WHAT THE HELL STILL NOT SAFE ON {new_new_new_idx}!!!", file=f)
#                     else:
#                         print("that fixed it! 3rd times a charm!", file=f)
#                         safe = True
#                 else:
#                     print("that fixed it! 2nd times a charm!", file=f)
#                     safe = True
#             else:
#                 print("that fixed it!", file=f)
#                 safe = True
#         else:
#             # print("Already safe, no changes needed.")
#             pass
        
#         # print(f"Line {k+1}: {v['line']} | Safe: {safe}")
#         if safe:
#             safety += 1

#     print("\n\n----------------------", file=f)
#     print(f"Answer: {safety}", file=f)
#     print("----------------------", file=f)

# print(f"Total safe lines after removing one crease: [326<] {safety} [<999]")
# first answer is 310 : lets go! -- 310 is too low.
# second answer is 326 and its still too low.

# part 2 - 2
with open("/home/dude/advent/advent/2024/day2_debug.txt", 'w') as f:
    for k, v in new.items():
        # print("----------------------")
        # print(f"Line {k}: {v['nums']}\n")
        nums = v['nums']
        safe, idx = checker(nums)
        if not safe:
            for i in range(len(nums)):
                new_nums = nums.copy()
                new_nums.pop(i)
                new_safe, new_idx = checker(new_nums)
                if new_safe:
                    print("\n----------------------", file=f)
                    print(f"Line {k}: {v['nums']}\n", file=f)
                    print(f"Original nums: {nums}", file=f)
                    print(f"Removed {nums[i]} at index {i} | New nums: {new_nums}", file=f)
                    safe = True
                    break
        if safe:
            safety += 1

print(f"Total safe lines after removing one crease: {safety}")
# FIRST TRY! 328 was correct! part 2 - 2 in clean mode was correct.