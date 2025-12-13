def opener(day):
    with open(f"/home/ruckus/code/advent/advent/2025/data/day{day}.txt", 'r') as file:
        data = file.readlines()
    return [x.strip() for x in data]


data = opener(2)

if False:
    data = ["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]

if False:
    data = ["11-12, 22-23, 1111111-1111112, 1212-1213, 123123-123124, 12341234-12341235, 99999999-100000000, 12345678-12345679, 12344321-12344322, 123321-123322, 456654-456655, 789987-789988, 1122-1123, 3344-3345, 5566-5567, 7788-7789"]

# print(data)

data = data[0].split(",")

def check_digit(dig):
    print("Checking digits[1]:", dig)
    str_dig = str(dig)
    str_len = len(str_dig)
    if str_len % 2 != 0:
        # print("Odd length, skipping")
        return False, int(dig)
    mid = str_len // 2
    x = int(str_dig[:mid])
    y = int(str_dig[mid:])
    if x == y:
        print(" - pattern found:", x, y)
    return x == y, int(dig)

def check_digit_2(dig):
    print(f"checking digits[2]: {dig}")
    flag = False
    str_dig = str(dig)

    for i in range(len(str_dig)//2):
        if flag: break
        comp = str_dig[:i+1]
        against = str_dig[i+1:]
        # print(f" - comp: {comp}  |  ag: {against}")

        sub_flag = False
        for e, i in enumerate(range(0, len(against), len(comp))):
            if e > 0 and not sub_flag:
                # print("   -- breaking, subflag false")
                break
            comp2 = against[i:i+len(comp)]
            # print(f" - - e: {e} | i: {i} | comp2 {comp2} | flag: {comp==comp2}")

            if comp == comp2:
                sub_flag = True
            else:
                sub_flag = False
                break

            if len(comp2) + e*len(comp) == len(against):
                flag = True
                print("  -- interior repeating pattern found!")
                break
        if sub_flag:
            flag = True
            print("  -- repeating pattern found!")
    return flag, int(dig)


total = 0
for r in data:
    x, y = r.split("-")
    for i in range(int(x), int(y) + 1):
        v1, val1 = check_digit(i)
        if v1:
            total += val1
            # print("Valid:", val1)
        else:
            v2, val2 = check_digit_2(i)
            if v2:
                total += val2
            # print("Valid:", val2)
        # break
    # break

print("Total:", total)
