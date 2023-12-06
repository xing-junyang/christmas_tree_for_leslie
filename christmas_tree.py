# This code is written by xingjunyang.
import turtle
import math


# Draw one ribbon at one time. Use sin function to draw.
def draw_one_ribbon(centre_x, centre_y, height, width, color, precision, pensize):
    turtle.speed(10)
    turtle.pensize(pensize)
    turtle.pencolor(color)
    turtle.penup()
    for i in range(0, precision):
        if i == 1:
            turtle.pendown()
        angle = ((i - precision / 2) / precision * 240) / 180 * math.pi
        x = centre_x + width * math.sin(angle)
        y = centre_y + height * (i / precision)
        turtle.goto(x, y)
    turtle.penup()


# Draw all ribbons.
def draw_ribbon():
    print("Drawing ribbons...", end='')
    draw_one_ribbon(-18, 43, 75, 125, "#DD0000", 50, 3)
    draw_one_ribbon(-12, 120, 50, 92, "#EE0000", 60, 3)
    draw_one_ribbon(-10, 180, 40, 60, "#FF0000", 70, 3)
    print("Done.")


# Draw a tetra-cuspid star.
def draw_one_star(centre_x, centre_y, height, width, rotation, pen_color, fill_color, precision):
    turtle.speed(10)
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.pensize(2)
    turtle.penup()
    for i in range(0, precision):
        if i == 1:
            turtle.pendown()
            turtle.begin_fill()
        angle = (i / precision) * 2 * math.pi
        rotate_angle = (rotation / 180) * math.pi
        x = centre_x + width * math.pow(math.cos(angle), 3)
        y = centre_y + height * math.pow(math.sin(angle), 3)
        x_r = math.cos(rotate_angle) * x - math.sin(rotate_angle) * y
        y_r = math.sin(rotate_angle) * x + math.cos(rotate_angle) * y
        turtle.goto(x_r, y_r)

    turtle.end_fill()
    turtle.penup()


# Draw a heart.
def draw_one_heart(centre_x, centre_y, height, width, rotation, color, precision):
    turtle.speed(10)
    turtle.pencolor(color)
    turtle.pensize(3)
    turtle.penup()
    for i in range(0, precision):
        if i == 1:
            turtle.pendown()
        angle = (i / precision) * 2 * math.pi
        rotate_angle = (rotation / 180) * math.pi
        x = centre_x + width * 16 * pow(math.sin(angle), 3)
        y = centre_y + height * (17 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) -
                                 math.cos(4 *
                                          angle))
        x_r = math.cos(rotate_angle) * x - math.sin(rotate_angle) * y
        y_r = math.sin(rotate_angle) * x + math.cos(rotate_angle) * y
        turtle.goto(x_r, y_r)
    turtle.penup()


# Draw a Clover.
def draw_one_clover(centre_x, centre_y, height, width, rotation, pen_color, fill_color, precision):
    turtle.speed(10)
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.pensize(1)
    turtle.penup()
    for i in range(0, precision):
        if i == 1:
            turtle.pendown()
            turtle.begin_fill()
        angle = (i / precision) * 2 * math.pi
        rotate_angle = (rotation / 180) * math.pi
        rho = 2 * math.sin(2 * (rotate_angle + angle))
        x = centre_x + rho * width * math.cos(angle)
        y = centre_y + rho * height * math.sin(angle)
        turtle.goto(x, y)
    turtle.end_fill()
    turtle.penup()


# Draw a star at the top of the tree.
def draw_top_star():
    print("Drawing top star...", end='')
    draw_one_star(0, 300, 30, 20, 0, "yellow", "#F7D613", 100)
    print("Done.")


# Draw stars around the tree.
def draw_starry_background():
    print("Drawing stars...", end='')
    draw_one_star(100, 200, 10, 10, 45, "yellow", "yellow", 100)
    draw_one_star(100, 140, 10, 10, -45, "#FFD700", "#FFD700", 100)
    draw_one_star(0, 200, 10, 10, -30, "#EEEE00", "#EEEE00", 100)
    draw_one_star(-20, 185, 10, 10, 30, "#FFB90F", "#FFB90F", 100)
    draw_one_star(-80, 145, 10, 10, 30, "#EEDD82", "#EEDD82", 100)
    draw_one_star(90, 143, 10, 10, -20, "#CD9B1D", "#CD9B1D", 100)
    draw_one_star(0, 240, 10, 10, -15, "#F7D613", "#F7D613", 100)
    print("Done.")


# Draw heart.
def draw_heart():
    print("Drawing heart...", end='')
    draw_one_heart(0, 150, 20, 20, 0, "#CD0000", 365)
    print("Done.")


# Draw clover.
def draw_clover():
    draw_one_clover(0, 300, 15, 15, 45, "yellow", "yellow", 100)


# Draw tree leaves border and fill it with color.
def draw_tree_border():
    print("Drawing tree border and filling...", end='')
    turtle.speed(10)
    turtle.pensize(4)
    turtle.penup()

    # Level 4
    turtle.pencolor("#008B00")
    turtle.fillcolor("#008B00")
    turtle.begin_fill()
    turtle.goto(100, 90)
    turtle.pendown()
    turtle.setheading(290)
    turtle.circle(200, 30)
    turtle.setheading(135)
    turtle.circle(32, 90)
    turtle.setheading(135)
    turtle.circle(32, 90)
    turtle.setheading(135)
    turtle.circle(32, 90)
    turtle.setheading(135)
    turtle.circle(32, 90)
    turtle.setheading(135)
    turtle.circle(32, 90)
    turtle.setheading(135)
    turtle.circle(32, 90)
    turtle.setheading(135)
    turtle.circle(32, 90)
    turtle.setheading(40)
    turtle.circle(200, 30)
    turtle.speed(3)
    turtle.goto(100, 90)
    turtle.speed(10)
    turtle.penup()
    turtle.end_fill()

    # Level 3
    turtle.pencolor("#00AB00")
    turtle.fillcolor("#00AB00")
    turtle.begin_fill()
    turtle.goto(75, 150)
    turtle.pendown()
    turtle.setheading(290)
    turtle.circle(200, 30)
    turtle.setheading(135)
    turtle.circle(31.5, 90)
    turtle.setheading(135)
    turtle.circle(31.5, 90)
    turtle.setheading(135)
    turtle.circle(31.5, 90)
    turtle.setheading(135)
    turtle.circle(31.5, 90)
    turtle.setheading(135)
    turtle.circle(31.5, 90)
    turtle.setheading(135)
    turtle.circle(31.5, 90)
    turtle.setheading(40)
    turtle.circle(200, 30)
    turtle.speed(3)
    turtle.goto(75, 150)
    turtle.speed(10)
    turtle.penup()
    turtle.end_fill()

    # Level 2
    turtle.pencolor("#00CD00")
    turtle.fillcolor("#00CD00")
    turtle.begin_fill()
    turtle.goto(40, 220)
    turtle.pendown()
    turtle.setheading(290)
    turtle.circle(200, 30)
    turtle.setheading(135)
    turtle.circle(28, 90)
    turtle.setheading(135)
    turtle.circle(28, 90)
    turtle.setheading(135)
    turtle.circle(28, 90)
    turtle.setheading(135)
    turtle.circle(28, 90)
    turtle.setheading(135)
    turtle.circle(28, 90)
    turtle.setheading(40)
    turtle.circle(200, 30)
    turtle.speed(3)
    turtle.goto(40, 220)
    turtle.speed(10)
    turtle.penup()
    turtle.end_fill()

    # Level 1
    turtle.pencolor("#00E000")
    turtle.fillcolor("#00E000")
    turtle.begin_fill()
    turtle.goto(5, 290)
    turtle.pendown()
    turtle.setheading(285)
    turtle.circle(200, 30)
    turtle.setheading(135)
    turtle.circle(20, 90)
    turtle.setheading(135)
    turtle.circle(20, 90)
    turtle.setheading(135)
    turtle.circle(20, 90)
    turtle.setheading(135)
    turtle.circle(20, 90)
    turtle.setheading(45)
    turtle.circle(200, 30)
    turtle.speed(3)
    turtle.goto(5, 290)
    turtle.speed(10)
    turtle.penup()
    turtle.end_fill()

    print("Done.")


# Draw trunk border and fill it with color.
def draw_trunk_border():
    print("Drawing trunk...", end='')
    turtle.speed(3)
    turtle.pensize(4)
    turtle.penup()

    turtle.pencolor("#945200")
    turtle.fillcolor("#945200")

    turtle.goto(27, 40)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(270)
    turtle.circle(200, 30)
    turtle.setheading(160)
    turtle.circle(152, 40)
    turtle.setheading(60)
    turtle.circle(200, 30)

    turtle.end_fill()
    turtle.penup()
    print("Done.")


# Draw a colourful dot.
def draw_one_point(centre_x, centre_y, radius, color):
    turtle.penup()
    turtle.pencolor(color)
    turtle.pensize(2)
    turtle.fillcolor(color)
    turtle.goto(centre_x + radius, centre_y)
    turtle.setheading(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()


# Draw decoration.
def draw_decoration():
    print("Drawing decoration...", end='')
    turtle.speed(10)
    draw_one_point(5, 260, 3, "white")
    draw_one_point(-20, 230, 3, "white")
    draw_one_point(40, 190, 3, "white")
    draw_one_point(-55, 160, 3, "white")
    draw_one_point(-20, 170, 3, "white")
    draw_one_point(50, 150, 3, "white")
    draw_one_point(0, 125, 3, "white")
    draw_one_point(-70, 90, 3, "white")
    draw_one_point(65, 110, 3, "white")
    draw_one_point(-20, 90, 3, "white")
    draw_one_point(-100, 50, 3, "white")
    draw_one_point(-50, 40, 3, "white")
    draw_one_point(55, 30, 3, "white")
    draw_one_point(110, 20, 3, "white")

    draw_one_point(15, 230, 7, "#436EEE")
    draw_one_point(10, 180, 7, "#FFA500")
    draw_one_point(30, 165, 4, "#D02090")
    draw_one_point(34, 112, 7, "#7D26CD")
    draw_one_point(-40, 110, 7, "#F7B530")
    draw_one_point(-65, 120, 4, "#FF34B3")
    draw_one_point(65, 50, 5, "#CD661D")
    draw_one_point(100, 45, 6, "#00BFFF")
    draw_one_point(-100, 30, 7, "#EEEE00")
    draw_one_point(-75, 35, 4, "#8B4726")
    draw_one_clover(0, 40, 13, 13, 0, "#66CD00", "#66CD00", 100)
    print("Done.")


# Draw text.
def draw_text():
    print("Drawing text...", end='')
    turtle.speed(3)
    turtle.penup()
    turtle.goto(-300, 560)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.write('To Leslie:', font=('HeatherScriptTwo', 50, 'bold'))
    turtle.penup()
    turtle.speed(1)
    turtle.goto(-285, 500)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write('Eagerly awaiting the Christmas Day!', font=('SnellRoundhand', 40, 'bold'))
    print("Done.")


def main():
    turtle.setup(720, 960)
    turtle.getscreen().setworldcoordinates(-360, -300, 360, 660)
    turtle.title("christmas_tree_for_leslie")
    turtle.bgcolor("#81D8CF")
    draw_trunk_border()
    draw_tree_border()
    draw_decoration()
    draw_starry_background()
    draw_ribbon()
    draw_top_star()
    draw_heart()
    draw_text()
    print("ok")
    turtle.mainloop()


main()
