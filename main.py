#"تقنية عملي نهائي ١٤٤٦ + عهد جاري المطيري"
basic.show_string("welcome")

def on_gesture_shake():
    basic.show_number(randint(3, 8))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
add = 0

def on_button_pressed_a():
    global add
    add += 1
    basic.show_number(add)
input.on_button_pressed(Button.A, on_button_pressed_a)

player = game.create_sprite(0, 1)
def on_button_pressed_B():
    player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_B)
