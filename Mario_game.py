
# import packages
import turtle
import random
import threading
import time


# move bowser to the beginning of the floor offscreen
def reset_bowser():
    bowser.speed(0)
    bowser.hideturtle()
    bowser.setpos((wn_width/2)+200, 0)
    bowser.showturtle()


def move_bowser():
    bowser_speed = random.randint(1,3)
    bowser.speed(bowser_speed)
    bowser.setpos(-wn_width/2-200,0)

def reset_move_bowser():
    reset_bowser()
    move_bowser()

def go_right():
 mario.shape("mario.gif")
 mario.setheading(0)
 mario.fd(10)

def jump():
    mario.speed(3)
    mario.goto(mario_start_x,200)
    wn.ontimer(mario_floor,400)

def mario_floor():
    mario.goto(mario_start_x,0)

def bowser_thread_entry():
    count = 0
    while mario_is_alive:
        reset_move_bowser()
        count += 1

def collision():
    global mario_is_alive
    delta_x = abs(mario.xcor()-bowser.xcor())
    delta_y = abs(mario.ycor()-bowser.ycor()) 
    print(delta_x, delta_y)
    if delta_x < 50 and delta_y < 30:
        mario_is_alive = False

def collision_check():
    while mario_is_alive:
        collision()
        time.sleep(0.01)

mario_is_alive = True

#Turtle Setup
wn_width=1000
wn_height=600
mario_start_x = -wn_width/3
wn = turtle.Screen()
wn.setup(width=wn_width, height=wn_height)
# create characters and stage
mario = turtle.Turtle()
mario.setheading(0)
mario.penup()
mario.goto(mario_start_x,0)

bowser = turtle.Turtle()
bowser.setheading(0)
bowser.penup()
bowser.speed(0)
bowser.hideturtle()

floor = turtle.Turtle()
floor.setheading(0)
floor.penup()

# change to custom image for the characters
mario_image = "mario.gif"
turtle.register_shape(mario_image)
mario.shape(mario_image)

bowser_image = "bowser.gif"
turtle.register_shape(bowser_image)
bowser.shape(bowser_image)

# set up the floor
floor.speed(0)
floor.hideturtle()
floor.penup()
floor.goto(-1000,-50) # change floor to different value later (x, THIS ONE)
floor.pendown()
floor.forward(2000)

collision_thread = threading.Thread(target=collision_check)
collision_thread.start()
bowser_thread = threading.Thread(target = bowser_thread_entry)
bowser_thread.start()





wn.onkeypress(jump, "space")
wn.listen()

wn.mainloop()
    