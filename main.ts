// "تقنية عملي نهائي ١٤٤٦ + عهد جاري المطيري"
basic.showString("welcome")
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showNumber(randint(3, 8))
})
let add = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    add += 1
    basic.showNumber(add)
})
let player = game.createSprite(0, 1)
input.onButtonPressed(Button.B, function on_button_pressed_B() {
    player.move(1)
})
