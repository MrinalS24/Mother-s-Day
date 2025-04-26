import pgzrun

WIDTH = 1400
HEIGHT = 800

engine = Actor("engine")
rbed_1 = Actor("bed_red")
gbed_2 = Actor("bed_green")
rbed_3 = Actor("bed_red")
gbed_4 = Actor("bed_green")
rbed_5 = Actor("bed_red")
gbed_6 = Actor("bed_green")

photo_1 = Actor("mothers_day")

engine.pos = (0,650)
rbed_1.pos = (-350,730)
gbed_2.pos = (-660,730)

def draw():
    screen.clear()
    screen.fill("black")
    engine.draw()
    rbed_1.draw()
    gbed_2.draw()
    photo_1.draw()
    """rbed_3.draw()
    gbed_4.draw()
    rbed_5.draw()
    gbed_6.draw()"""

def update():
    engine.x += 3
    rbed_1.x += 3
    gbed_2.x += 3
    photo_1.pos = (rbed_1.pos[0], rbed_1.pos[1]- 110)















pgzrun.go()