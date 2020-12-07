import turtle
import random
#Turtle Setup
wn = turtle.Screen()
mario = turtle.Turtle()
floor = turtle.Turtle()
turtle.hideturtle()
turtle.speed(0)
mario.setheading(0)
turtle.register_shape("mario.gif")
mario.shape("mario.gif")
mario.penup()
turtle.register_shape("bowser.gif")
bowser = turtle.Turtle
#variables
mario_landing = 300
mario_initial_velocity = 2
#Test
#turtle.screensize(2000000, 20000000)
#shape = ((10000, -200), (10000, -500), (-10000, -500), (-10000,-200))
#turtle.register_shape("floor", shape)
#turtle.clear()
#floor.setheading(90)
#floor.fillcolor("white")
#floor.shape("floor")
floor.speed(10)
floor.hideturtle()
floor.penup()
floor.goto(-500,-50) # change floor to different value later (x, THIS ONE)
floor.pendown()
floor.forward(1000)

def go_right():
 mario.shape("mario.gif")
 mario.setheading(0)
 mario.fd(10)
def jump():
    print(mario.pos())  # for debugging
    mario.setheading(0)
    mario_start_x = mario.xcor()
    mario_start_y = mario.ycor()
    mario_x = mario.xcor()
    mario_y = mario.ycor()

    while mario_y <mario_start_y + 50:
        mario.goto(mario_x+1, mario_y+2)
        mario_x = mario.xcor()
        mario_y = mario.ycor()
    while mario_y < mario_start_y + 80:
        mario.goto(mario_x + 2, mario_y+ 2)
        mario_x = mario.xcor()
        mario_y = mario.ycor()
    while mario_y < mario_start_y + 100:
        mario.goto(mario_x+2, mario_y+ 3)
        mario_x = mario.xcor()
        mario_y = mario.ycor()
    while mario_y > mario_start_y + 80:
         mario.goto(mario_x+2, mario_y -3)
         mario_x = mario.xcor()
         mario_y = mario.ycor()
    while mario_y > mario_start_y + 50:
        mario.goto(mario_x+1, mario_y - 2)
        mario_x = mario.xcor()
        mario_y = mario.ycor()
    print(mario.pos())  # for debugging
    while mario_y > mario_start_y:
        mario.goto(mario_x+1, mario_y - 2)
        mario_x = mario.xcor()
        mario_y = mario.ycor()
def forward():
    mario.setheading(90)
    mario.forward(20)
 
def collision():
    mario.hideturtle()
    mario.goto(0, -200)
    mario.showturtle()
#def recalculate_landing():
    #mario_landing height(time) = -4.9(16 in feet) t^2 + (velocity)t + current height



#screen.ontimer(recalculate_landing, 10)
#while mario_y > -300:
     #mario.goto(mario_landing, -300)
     #while 
#mario_count = 0
#while mario_count < 1000:
#    mario_x = mario.xcor()
#    mario_y = mario.ycor()
#    mario.goto(mario_x+1, mario_y+2)
#    mario_count += 1



mario.goto(200,400)

bowsers = []
for i in range(1):
    bowser = turtle.Turtle()
    bowser.speed(0)
    bowser.shape("bowser.gif") #not sure about this line
    bowser.penup()
    bowser.goto(0, 40)
    bowser.speed = random.randint(10, 16)
    bowsers.append(bowser)
    while True:
    #update the screen
        wn.update()
        for bowser in bowsers:
            if (abs(mario.xcor()-bowser.xcor()))<25 and (abs(mario.ycor()-bowser.ycor()))<25:
                collison()
            x = bowser.xcor()
            x-= bowser.speed
            bowser.setx(x)
 
    #respawn of bowser 
    if x< -250 :
        y = random.randint(-300, -300)
        x = random.randint(400, 400)
        bowser.goto(x,y)




wn.onkeypress(jump, 'space')
wn.onkeypress(go_right, 'Right')
wn.listen()
wn.mainloop()
    