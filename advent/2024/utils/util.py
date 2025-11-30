def opener(day_num):
    # Dont share your input data files.
    with open(f"/home/dude/advent/advent/2024/data/day{day_num}.txt", 'r') as file:
        return file.readlines()