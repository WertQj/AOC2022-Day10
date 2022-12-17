xs, cycles, start = [], 0, 20


def crt_constructor():
    i = 0
    theta = []
    while i < 6:
        theta.append([])
        while len(theta[i]) < 40:
            theta[i].append(".")
        i += 1
    return theta


crt = crt_constructor()


def drawing(cycle, x, screen):
    pixel = cycle % 40
    row = cycle // 40
    if pixel in range(x, x+3):
        screen[row][pixel] = "#"


def cycling(x, screen):
    global xs, cycles, start
    cycles += 1
    drawing(cycles, x, screen)
    if cycles == start:
        xs.append(x * start)
        start += 40


def processing():
    x = 1
    with open("input.txt", mode="r", encoding="UTF-8") as commands:
        while True:
            command = commands.readline()
            if command == "":
                break

            if command.startswith("n"):
                cycling(x, crt)
                continue

            if command.rfind(" "):
                cycling(x, crt)
                cycling(x, crt)
                x += int(command[command.rfind(" "):])


processing()


for _ in crt:
    alpha = "".join(_)
    print(alpha)
