from gpiozero import LED, Button
from signal import pause

led = LED(8)
button = Button(25, pull_up=True)

def toggle_led():
    led.toggle()

button.when_pressed = toggle_led

print("Mission 2_2: 버튼을 누를 때마다 LED가 토글됩니다.")
pause()
