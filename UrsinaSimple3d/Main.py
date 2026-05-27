from ursina import *
import random
import time
import json

app = Ursina()
cube = Entity(model='cube', color=color.green, scale=(2,2,2))    # создаём кубик и звук
color_sound = Audio('assets/sounds/zvuk2.wav', autoplay=False)
id_cube = random.randint(3000, 8000)

last_press = 0

def update():                # управление кубика
    global last_press
    if held_keys['a']:
        cube.rotation_y += 1
    if held_keys['d']:
        cube.rotation_y -= 1
    if held_keys['w']:
        cube.rotation_x += 1
    if held_keys['s']:
        cube.rotation_x -= 1
    if held_keys['space']:
        if time.time() - last_press > 0.2:
            cube.color = color.random_color()
            color_sound.play()
            last_press = time.time()
    if held_keys['backspace']:      # сбросить?
        cube.color = color.green
        cube.rotation_y = 90
        cube.rotation_x = 90

def cube_color():
    color_sound.play()
    cube.color = color.random_color()

button_color = Button(text='color [space]', color=color.azure, scale=(0.2, 0.1), on_click=cube_color, x=-0.7, y=-0.4)

def cube_reset():
    color_sound.play()
    cube.rotation_y = 90
    cube.rotation_x = 90
    cube.color = color.green

button_reset = Button(text='reset [backspace]', color=color.azure, scale=(0.3, 0.1), on_click=cube_reset, x=0.7, y=-0.4)

def cube_save():
    data = {
        "id": id_cube,
        "color": {
            "r": cube.color.r,
            "g": cube.color.g,
            "b": cube.color.b
        },
        "rotation": {
            "rotation_y": cube.rotation_y,
            "rotation_x": cube.rotation_x
        },
    }

    with open(f"{id_cube}.json", "w", encoding="UTF=8") as f:
        json.dump(data, f, ensure_ascii=False, indent=8)

button_save = Button(text='save', color=color.azure, scale=(0.2, 0.1), on_click=cube_save, x=0, y=-0.4)

app.run()