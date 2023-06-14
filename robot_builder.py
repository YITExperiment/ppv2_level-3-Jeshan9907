import turtle as t

def rectangle (horizontal, vertical, color) :
    t.pendown ()
    t.pensize (1)
    t.color (color)
    t.begin_fill()
    for counter in range (1,3):
        t. forward (horizontal)
        t.right (90)
        t. forward (vertical)
        t.right (90)
t.end_fill()
t.penup()

t.penup()
t.speed('slow')
t.bgcolor('dodger blue')

#feet
t.goto (-100, -150)
rectangle (50,20, 'blue')
t.end_fill()
t.penup()
t.goto (-30,-150)
rectangle (50,20, 'blue')
t.end_fill()
t.penup()

#legs.
t.goto (-25, -50)
rectangle (15, 100, 'grey')
t.goto (-55,-50)
t.end_fill()
t.penup()
rectangle(-15, 100, 'grey')
t.end_fill()
t.penup()

#body
t.goto (-90,100)
rectangle (100, 150, 'red')
t.end_fill()
t.penup()

#arms
t.goto (-150, 70)
rectangle (60, 15, 'grey')
t.end_fill()
t.penup()
t.goto (-150,110)
rectangle (15, 40, 'grey')
t.end_fill()
t.penup()

t.goto (10, 70)
rectangle (60, 15, 'grey')
t.end_fill()
t.penup()
t.goto (55,110)
rectangle (15, 40, 'grey')
t.end_fill()
t.penup()

#neck
t.goto(-50,120)
rectangle(15,20,'gray')
t.end_fill()
t.penup()

#head
t.goto(-85,170)
rectangle(80,50,'red')
t.end_fill()
t.penup()

#eyes
t.goto (-60, 160)
rectangle (30, 10, 'white')
t.end_fill()
t.penup()
t.goto (-55, 155)
rectangle (5, 5, 'black')
t.end_fill()
t.penup()
t.goto (-40,155)
rectangle (5, 5, 'black')
t.end_fill()
t.penup()

#mouth
t.goto (-65,135)
t.right(0)
rectangle (40,5, 'black')
t.end_fill()
t.penup()


t.hideturtle()




