import turtle

# create a turtle object
t = turtle.Turtle()
# set the fill color to gray
black_eye = [(0.86894, -0.04163),
 (0.94978, -0.01997),
 (1.00303, 0.02832),
 (1.04503, 0.09633),
 (1.06366, 0.16154),
 (1.06765, 0.26533),
 (0.70437, 0.27332),
 (0.70704, 0.23073),
 (0.71901, 0.14956),
 (0.74296, 0.09101),
 (0.77224, 0.03113),
 (0.80151, -0.00746)]


eye = [(0.86894, -0.04163),
 (0.94444, -0.02362),
 (1.00423, 0.03157),
 (1.04791, 0.09595),
 (1.06631, 0.17183),
 (1.06631, 0.26841),
 (1.06401, 0.33739),
 (1.04534, 0.44086),
 (0.96357, 0.53946),
 (0.84557, 0.54434),
 (0.77428, 0.48685),
 (0.72829, 0.42017),
 (0.7145, 0.34889),
 (0.703, 0.27531),
 (0.7122, 0.18563),
 (0.73749, 0.10515),
 (0.77198, 0.03617),
 (0.80648, -0.00982)]

points = [(1.38822, -1.37829),
 (1.52127, -1.23983),
 (1.65287, -1.02241),
 (1.76158, -0.79354),
 (1.83024, -0.58756),
 (1.88746, -0.3358),
 (1.91035, -0.08977),
 (1.92751, 0.1391),
 (1.89318, 0.39085),
 (1.79591, 0.63116),
 (1.6357, 0.87719),
 (1.43258, 1.12895),
 (1.17005, 1.37136),
 (0.8935, 1.53347),
 (0.63126, 1.67174),
 (0.11631, 1.69559),
 (-0.22699, 1.68605),
 (-0.54646, 1.59546),
 (-0.83731, 1.41427),
 (-1.08525, 1.17587),
 (-1.30935, 0.88978),
 (-1.30935, 0.67522),
 (-1.14723, 0.67045),
 (-1.00419, 0.79442),
 (-0.83532, 0.91693),
 (-0.60354, 0.97322),
 (-0.30885, 0.96329),
 (-0.06713, 0.86064),
 (0.10505, 0.70171),
 (0.27392, 0.48648),
 (0.39312, 0.21165),
 (0.34676, 0.1057),
 (0.16465, -0.04993),
 (0.04214, -0.17906),
 (0.04545, -0.30158),
 (0.12492, -0.3976),
 (0.27723, -0.35124),
 (0.3865, -0.24529),
 (0.48252, -0.23204),
 (0.49908, -0.34462),
 (0.37656, -0.49693),
 (0.27884, -0.6464),
 (0.29608, -0.70388),
 (0.40147, -0.7422),
 (0.48387, -0.6943),
 (0.5701, -0.63107),
 (0.61609, -0.59849),
 (0.64483, -0.6464),
 (0.59118, -0.6943),
 (0.52028, -0.75945),
 (0.41872, -0.79777),
 (0.31716, -0.78819),
 (0.2386, -0.77095),
 (0.16073, -0.87164),
 (0.05477, -0.98091),
 (-0.10085, -1.067),
 (-0.28297, -1.10343),
 (-0.51806, -1.09349),
 (-0.75315, -1.05045),
 (-0.91871, -0.91469),
 (-1.06109, -0.7988),
 (-1.24652, -0.64317),
 (-1.37298, -0.62018),
 (-1.39789, -0.74282),
 (-1.30017, -0.95168),
 (-1.13806, -1.17578),
 (-0.99978, -1.33312),
 (-0.76138, -1.54769),
 (-0.50867, -1.68596),
 (-0.19874, -1.75748),
 (0.05396, -1.77179),
 (0.34958, -1.76702),
 (0.70242, -1.7098),
 (0.99327, -1.62875),
 (1.25075, -1.4714)]

scalefactor = 55

points = [(x * scalefactor,  y * scalefactor) for x, y in points]
eye = [(x * scalefactor,  y * scalefactor) for x, y in eye]
black_eye = [(x * scalefactor,  y * scalefactor) for x, y in black_eye]

t.color("gray")
t.fillcolor("gray")
t.pensize(0.1)
t.begin_fill()

# iterate through the points and draw lines between them
for i in range(len(points) - 1):
    t.penup()
    t.goto(points[i])
    t.pendown()
    t.goto(points[i+1])
# start filling the shape
t.begin_fill()
# close the shape by drawing a line back to the starting point
t.goto(points[0])
t.end_fill()


t.color("black")
t.fillcolor("black")
t.pensize(0.1)
t.begin_fill()


# iterate through the points and draw lines between them
for i in range(len(eye) - 1):
    t.penup()
    t.goto(eye[i])
    t.pendown()
    t.goto(eye[i+1])
# start filling the shape
t.begin_fill()
# close the shape by drawing a line back to the starting point
t.goto(eye[0])
t.end_fill()

t.color(0,0,0)
t.pensize(3)


# iterate through the points and draw lines between them
for i in range(len(points) - 1):
    t.penup()
    t.goto(points[i])
    t.pendown()
    t.goto(points[i+1])
# start filling the shape
t.begin_fill()
# close the shape by drawing a line back to the starting point
t.goto(points[0])

# keep the window open until it is closed
# end the fill
t.end_fill()

t.color(0,0,0)
t.pensize(0.001)
t.begin_fill()

# iterate through the points and draw lines between them
for i in range(len(black_eye) - 1):
    t.penup()
    t.goto(black_eye[i])
    t.pendown()
    t.goto(black_eye[i+1])
# start filling the shape
t.begin_fill()
# close the shape by drawing a line back to the starting point
t.goto(black_eye[0])
t.end_fill()


t.color(0,0,0)
t.pensize(3)


# iterate through the points and draw lines between them
for i in range(len(eye) - 1):
    t.penup()
    t.goto(eye[i])
    t.pendown()
    t.goto(eye[i+1])
# start filling the shape
t.begin_fill()
# close the shape by drawing a line back to the starting point

# keep the window open until it is closed
# end the fill
t.end_fill()

turtle.hideturtle()
turtle.mainloop()

