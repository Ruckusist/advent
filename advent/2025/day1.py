def opener(day):
    with open(f"/home/ruckus/code/advent/advent/2025/data/day{day}.txt", 'r') as file:
        data = file.readlines()
    return [x.strip() for x in data]


data = opener(1)

if False:
    data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".splitlines()
    print("Using test data")

class Dial:
    def __init__(self, max_num=99):
        self.start = 50
        self.current = 50
        self.max = max_num

    def turn_l(self):
        if self.current == 0:
            self.current = self.max
        else:
            self.current -= 1

    def turn_r(self):
        if self.current == self.max:
            self.current = 0
        else:
            self.current += 1

    def turn(self, direction, steps):
        click = 0
        for _ in range(steps):
            if direction == 'L':
                self.turn_l()
            elif direction == 'R':
                self.turn_r()
            else:
                raise ValueError("Invalid direction")
            if self.current == 0:
                click += 1
        return self.current, click

def main():
    dial = Dial()
    print(f" - The dial starts by pointing at {dial.current}")
    counter = 0
    for instruction in data:
        print(instruction)
        direction = list(instruction)[0]
        steps = int(instruction[1:])
        result, click = dial.turn(direction, steps)
        if click: counter += click
        print(f" - The dial is rotated {direction}{steps}, new position: {result}")

    print(f" # Final position: {dial.current}")
    print(f" # The dial pointed at 0 a total of {counter} times")

if __name__ == "__main__":
    main()

# day1   00:25:04   00:31:05
# finished in 31 mins. 2858 gold and 3129 silver stars
