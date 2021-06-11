def get_next(x, y):
    if x == 3 and y == 3:
        return 4, 0
    if x == 11 and y == 3:
        return 0, 0
    elif x == 3:
        return 0, y+1
    elif x == 11:
        return 4, y+1
    else:
        return x+1, y

def all_buttons():
    currX = 0
    currY = 0
    while True:
        yield currX, currY
        currX, currY = get_next(currX, currY)
        if currX == 0 and currY == 0:
            break

for x,y in all_buttons():
    print("%s, %s all" % (x,y))
