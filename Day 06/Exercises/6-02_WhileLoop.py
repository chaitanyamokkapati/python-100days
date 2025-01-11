# While loop - Do something Repeatedly
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for n in range(6):
    jump()

no_hurd = 6
while no_hurd > 0:
    jump()
    no_hurd -=1