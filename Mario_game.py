
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
    update_score()
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
    if delta_x < 50 and delta_y < 30:
        mario_is_alive = False
        game_over()

def collision_check():
    while mario_is_alive:
        collision()
        time.sleep(0.01)

def create_floor(color):

    floor.hideturtle()
    floor.penup()
    floor.goto(-wn_width/2,-50)
    floor.pendown()
    floor.fillcolor(color)
    floor.begin_fill()
    floor.goto(-wn_width/2,-wn_height/2)
    floor.goto(wn_width/2,-wn_height/2)
    floor.goto(wn_width/2, -50)
    floor.goto(-wn_width/2,-50)
    floor.end_fill()

def update_score():
   global score
   score_text = "Score: " + str(score)
   score_writer.clear()
   score += 1
   score_writer.write(score_text, font=("Arial", 30, "normal"))
score = 0
mario_is_alive = True

def game_over():
    score_writer.penup()
    score_writer.clear()
    score_text = "GAME OVER."
    score_writer.write(score_text, font=("Arial", 30, "normal"))
    score_writer.goto(200,100)
    score_text2 = "Final Score: " + str(score-1)
    score_writer.write(score_text2, font=("Arial", 30, "normal"))

#Turtle Setup
wn_width=1000
wn_height=600
mario_start_x = -wn_width/3
wn = turtle.Screen()
wn.setup(width=wn_width, height=wn_height)
#score writer setup
score_writer = turtle.Turtle()
score_writer.penup()
score_writer.goto(200,200)
score_writer.hideturtle()
score_writer.pendown()

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
floor.hideturtle()
floor.setheading(0)
floor.penup()
floor.speed(0)

# change to custom image for the characters
mario_image = "mario.gif"
turtle.register_shape(mario_image)
mario.shape(mario_image)

bowser_image = "bowser.gif"
turtle.register_shape(bowser_image)
bowser.shape(bowser_image)
ground_color= 0 


user_color_list = ["red", "green", "blue"]
while ground_color <1 or ground_color > 3:
    ground_color = int(input("choose a color: \n 1 for red \t 2 for green \t 3 for blue \n"))

create_floor(user_color_list[ground_color-1])


collision_thread = threading.Thread(target=collision_check)
collision_thread.start()
bowser_thread = threading.Thread(target = bowser_thread_entry)
bowser_thread.start()





wn.onkeypress(jump, "space")
wn.listen()

wn.mainloop()
    