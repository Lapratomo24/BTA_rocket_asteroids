"""
Task 1: Importing Modules

Import the sys module, which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
Import the time function from the time module to measure time durations.
Import the sqrt function from the math module to calculate the square root of a number.
Import all (use *) functions and classes from the tkinter module to use them without specifying the tkinter prefix.
Import all (use *) functions from the random module to have access to them without specifying the random prefix.
"""

# write your code here

import sys
from time import time
from math import sqrt
from tkinter import *
from random import *

import pygame
pygame.init()

frame_rate = 15
asteroid_chance = 5
time_limit = 60
bonus_score = 300
bonus = 0
end = time() + time_limit

# asteroid
asteroid_id = list()
asteroid_radius_lst = list()
asteroid_speed = list()
asteroid_img_lst = list()

asteroid_radius = 30
max_asteroid_speed = 10
gap_between_ast_roc = 10
score: int = 0

"""
Task 2: Create an Application Window and Set Parameters

Set the height of the window to 700 pixels. 
Set the width of the window to 1400 pixels.
Create a Tkinter Tk() object window to represent the main window of the application.
Set the title of the window to "BTA Rocket".
"""

# write your code here
height = 700
width = 1400
window = Tk()
window.title = "BTA Rocket"

"""
Task 3: Creating the Canvas and Background

1. Create a canvas c with parameters:
window: the window where the canvas will be placed,
width and height: the width and height of the canvas,
bg='blue': the background color of the canvas.

2. Load the background image background_img from the specified file path.

3. Place the background image at coordinates (0, -150) on the canvas with parameters:
image=background_img: the background image,
anchor=NW: anchor the image to the northwest corner of the canvas.
"""

# write your code here
c = Canvas(window, width=width, height=height, bg='blue')
background_img = PhotoImage(file='background.png')
c.create_image(0, -150, image=background_img, anchor=NW)

c.pack()
rocket_r = 30
mid_x = width / 2
mid_y = height / 2
rocket_speed = 10

"""
Task 4: Creating the Player

1. Load the rocket image rocket_img from the specified file path.

2. Create an oval representing the rocket's body with parameters:
20, 44, 148, 84: the coordinates of the top-left and bottom-right corners of the oval,
outline='red': the outline color of the oval.

3. Place the rocket image at coordinates (-80, -5) on the canvas with parameters:
image=rocket_img: the rocket image,
anchor=NW: anchor the image to the northwest corner of the canvas.
"""

# write your code here
rocket_img = PhotoImage(file='rocket.png')
rocket_oval = c.create_oval(20, 44, 148, 84, outline='red')
rocket_image = c.create_image(-80, -5, image=rocket_img, anchor=NW)

c.move(rocket_oval, mid_x, mid_y)
c.move(rocket_image, mid_x, mid_y)

"""
Task 5: Creating the Text

1. Place the text "Time" at coordinates (50, 30) on the canvas with parameters:
text='TIME': the text "TIME",
fill='white': the text color.

2. Place the text "SCORE" at coordinates (150, 30) on the canvas with parameters:
text='SCORE': the text "SCORE",
fill='white': the text color.

3. Create variables time_text and score_text to store the identifiers of the text objects for time and score respectively, placed at coordinates (50, 50) and (150, 50) on the canvas with white color.
"""

# write your code here
c.create_text(50, 30, text='Time', fill='white')
c.create_text(150, 30, text='score', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')

additional_time_label = Label(window)

asteroid_img = [PhotoImage(file='asteroid_1.png'),
                PhotoImage(file='asteroid_2.png'),
                PhotoImage(file='asteroid_3.png'),
                PhotoImage(file='asteroid_4.png'),
                PhotoImage(file='asteroid_5.png'),
                PhotoImage(file='asteroid_6.png')]


"""
Task 6: Rocket Movement

1. Function named move_rocket that takes an event parameter representing the key event triggered by the user is already defined. def move_rocket(event):
2. Inside the function, check which arrow key was pressed using the event.keysym attribute.
3. If the 'Up' arrow key is pressed, move both the rocket oval and image objects upwards on the canvas by a value determined by the variable rocket_speed.
4. If the 'Down' arrow key is pressed, move both the rocket oval and image objects downwards on the canvas by a value determined by the variable rocket_speed.
5. If the 'Left' arrow key is pressed, move both the rocket oval and image objects to the left on the canvas by a value determined by the variable rocket_speed.
6. If the 'Right' arrow key is pressed, move both the rocket oval and image objects to the right on the canvas by a value determined by the variable rocket_speed.

Code Explanation:
- event.keysym: Determines which arrow key was pressed by the user.
- c.move(object, x, y): Moves the specified object (rocket oval or image) by the specified amount along the x and y axes on the canvas.
- rocket_speed: Represents the speed at which the rocket moves in pixels per event trigger.
"""

# write your code here
def move_rocket(event):
    if event.keysym == 'Up':
        c.move(rocket_image, 0, -rocket_speed)
        c.move(rocket_oval, 0, -rocket_speed)
    elif event.keysym == 'Down':
        c.move(rocket_image, 0, rocket_speed)
        c.move(rocket_oval, 0, rocket_speed)
    elif event.keysym == 'Left':
        c.move(rocket_image, -rocket_speed, 0)
        c.move(rocket_oval, -rocket_speed, 0)
    elif event.keysym == 'Right':
        c.move(rocket_image, rocket_speed, 0)
        c.move(rocket_oval, rocket_speed, 0)

def create_asteroid():
    x = width
    y = randint(0, height)
    r = asteroid_radius
    idl = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    asteroid_id.append(idl)
    asteroid_radius_lst.append(r)
    asteroid = choice(asteroid_img)

    bub_img = c.create_image(x - 2*r, y - 2*r, image=asteroid, anchor=NW)
    asteroid_img_lst.append(bub_img)
    asteroid_speed.append(randint(2, max_asteroid_speed))
    print(asteroid_speed)
    window.after(2000, create_asteroid)


def move_asteroids():
    for i in range(len(asteroid_id)):
        c.move(asteroid_id[i], -asteroid_speed[i], 0)
        c.move(asteroid_img_lst[i], -asteroid_speed[i], 0)
    window.after(frame_rate, move_asteroids)


def get_object_coords_by_id(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y


def del_asteroid(i):
    del asteroid_radius_lst[i]
    del asteroid_speed[i]
    c.delete(asteroid_id[i])
    c.delete(asteroid_img_lst[i])
    del asteroid_img_lst[i]
    del asteroid_id[i]


def clean_up_asteroid():
    for i in range(len(asteroid_id) - 1, -1, -1):
        x, y = get_object_coords_by_id(asteroid_id[i])
        if x < -gap_between_ast_roc:
            del_asteroid(i)


def distance(id1, id2):
    x1, y1 = get_object_coords_by_id(id1)
    x2, y2 = get_object_coords_by_id(id2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def collision():
    for bub in range(len(asteroid_id) - 1, -1, -1):
        if distance(rocket_oval, asteroid_id[bub]) < (rocket_r + asteroid_radius_lst[bub]):
            pygame.mixer.music.pause()
            pygame.mixer.Sound('boom.mp3').play()
            pygame.mixer.music.unpause()
            del_asteroid(bub)
            add_score()
            add_bonus_time()
    window.after(frame_rate, collision)


def add_score():
    global score
    score += 50


def show_score():
    global score
    c.itemconfig(score_text, text=str(score))


def update_score():
    global score
    show_score()
    window.after(500, update_score)


def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))


def update_time():
    show_time(int(end - time()))
    window.after(500, update_time)
    check_time()


def show_bonus_time_label():
    additional_time_label.configure(text='Bonus time: ' + str(time_limit))
    additional_time_label.place(x=mid_x - 50, y=50)
    window.after(1000, hide_bonus_time_label)


def hide_bonus_time_label():
    additional_time_label.place_forget()


def add_bonus_time():
    global bonus
    global end
    print(1)
    if (int(score / bonus_score)) > bonus:
        print(2)
        bonus += 1
        end += time_limit
        show_bonus_time_label()


def check_time():
    print(0)
    if time() >= end:
        print(00)
        messagebox.showinfo('Gameover', 'Gameover\nScore:' + str(score))
        window.destroy()
        sys.exit()


"""
Task 7: Adding Background Music

Import the Pygame library and initialize it using the pygame.init() function.
Load the background music file using the pygame.mixer.music.load() function. Specify the file path as an argument to the function.
Start playing the background music in an infinite loop using the pygame.mixer.music.play() function. Specify the value -1 as an argument to play the music indefinitely.
Set the volume level of the background music using the pygame.mixer.music.set_volume() function. Specify a value from 0.0 (mute) to 1.0 (full volume) as an argument to the function. In this case, set the volume level to 0.1 to provide a subtle audio backdrop for the game environment.
"""

# write your code here
pygame.mixer.music.load('space_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

window.after(frame_rate, create_asteroid)
window.after(frame_rate, move_asteroids)
c.bind_all('<Key>', move_rocket)
window.after(frame_rate, collision)
window.after(frame_rate, clean_up_asteroid)
show_score()
show_time(int(end - time()))
update_time()
update_score()
window.update()

pygame.mixer.music.stop()

window.mainloop()
