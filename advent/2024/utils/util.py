def opener(day_num):
    with open(f"/home/dude/advent/advent/2024/data/day{day_num}.txt", 'r') as file:
        return file.read()