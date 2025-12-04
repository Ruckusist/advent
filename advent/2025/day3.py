def opener(day):
    with open(f'/home/dude/advent/advent/2025/data/day{day}.txt', 'r') as f:
        return [x.strip() for x in f.readlines()]

data = opener(3)

if False :
    data = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()


def part1():
    jolts = 0
    for line in data:
        print(line)
        flag1 = '0'
        flag2 = '0'
        for e, c in enumerate(line):
            # do end of line check up  front.
            if e == len(line) - 1:
                if int(c) > int(flag2):
                    flag2 = c
                # print(f'Line max: {flag2}')
                continue

            if e == 0: flag1 = c; continue
            
            if int(c) > int(flag1):
                flag1 = c
                flag2 = '0'
            
            elif int(c) > int(flag2):
                flag2 = c

        j = int(flag1 +flag2)
        jolts += j
        print(f"l: ...{line[-5:]} | max: {flag1} 2nd max: {flag2} | jolts: {j}")
    print(f'Total jolts: {jolts}')


def part2():
    print(['part2 lets go...'])
    jolts = 0
    
    for line in data:
        line = list(line)
        flags = ['1' for _ in range(12)]
        final = []
        print('line:\n', line)
        print(f"line len: ",  len(line))
        print(f'Flags len: ', len(flags))
        
        for ele, ch in enumerate(line):
            for e, f in enumerate(flags.copy()):
                if int(ch) > int(f):
                    flags[e] = ch
                    if e != len(flags) - 1:
                        for i in range(e+1, len(flags)):
                            flags[i] = '1'
                            print(f"replaced flag: {f} with !1 at i: {i}")
                    print(f"replaced f: {f} with ch: {ch} at e: {e}")
                    break
            # end of line check
            if ele >= (len(line) - len(flags)):
                print(f"e: {ele} ch: {ch} flags: {flags}")
                final.append(flags.pop(0))
                print(f'final countdown... {final}')
                

        assert '0' not in final, "Final contains zero!"
        j = int(''.join(final))
        jolts += j
        print(f"jolts for line: {j}")
        

    print(f"final: {jolts}")

if __name__ == '__main__':
    # part1()

    part2()

# 170546494793820 is too high answer 1
# 168819308369418 is too low answer 2
# 170546480624128 is too high answer 3
# 170546479624128 is wrong answer 4 no more help.
# 170546480624128 i think i answered 5 and 3 the same. damnit.
# 170147128753455  this is the right answer
