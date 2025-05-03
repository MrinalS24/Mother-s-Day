import pgzrun

WIDTH = 1400
HEIGHT = 600

engine = Actor("engine")
rbed_1 = Actor("bed_red")
gbed_2 = Actor("bed_green")
rbed_3 = Actor("bed_red")
gbed_4 = Actor("bed_green")
rbed_5 = Actor("bed_red")
gbed_6 = Actor("bed_green")
rbed_7 = Actor("bed_red")

photo_1 = Actor("mothers_day")
photo_2 = Actor("first")
photo_3 = Actor("second")
photo_4 = Actor("third")
photo_5 = Actor("fourth")
photo_6 = Actor("fifth")
photo_7 = Actor("sixth")

firework = Actor("firework")

engine.pos = (0,450)
rbed_1.pos = (-350,530)
gbed_2.pos = (-660,530)
rbed_3.pos = (-970,530)
gbed_4.pos = (-1280,530)
rbed_5.pos = (-1590,530)
gbed_6.pos = (-1900,530)
rbed_7.pos = (-2210,530)

photo_1.pos = (-2210,420)
photo_2.pos = (-350,420)
photo_3.pos = (-660,420)
photo_4.pos = (-970,420)
photo_5.pos = (-1280,360)
photo_6.pos = (-1590,360)
photo_7.pos = (-1900,360)

firework.pos = (700,300)

def draw():
    screen.clear()
    screen.fill("black")
    if rbed_7.x >= 700:
        firework.draw()
        screen.draw.text("Dear Mama, thank ou for being the best mama ever! .",(150,100), color = "white", fontsize = 35)
        screen.draw.text("Thank you for listening to me, helping me and just being there",(150,150), color = "white", fontsize = 35)
        screen.draw.text("Thank you for taking care of us and putting up with our fights and tantrums",(150,200), color = "white", fontsize = 35)
        screen.draw.text("I love you so much! Happy Mother's Day!",(150,250), color = "white", shadow = (1, 1), scolor = "grey", fontsize = 35)
    engine.draw()
    rbed_1.draw()
    gbed_2.draw()
    rbed_3.draw()
    gbed_4.draw()
    rbed_5.draw()
    gbed_6.draw()
    rbed_7.draw()
    photo_1.draw()
    photo_2.draw()
    photo_3.draw()
    photo_4.draw()
    photo_5.draw()
    photo_6.draw()
    photo_7.draw()
    
def update():
    engine.x += 3
    rbed_1.x += 3
    gbed_2.x += 3
    rbed_3.x += 3
    gbed_4.x += 3
    rbed_5.x += 3
    gbed_6.x += 3
    if rbed_7.x <= 700:
        rbed_7.x += 3
    photo_1.x = (rbed_7.pos[0])
    photo_2.x = (rbed_1.pos[0])
    photo_3.x = (gbed_2.pos[0])
    photo_4.x = (rbed_3.pos[0])
    photo_5.x = (gbed_4.pos[0])
    photo_6.x = (rbed_5.pos[0])
    photo_7.x = (gbed_6.pos[0])

        















pgzrun.go()
