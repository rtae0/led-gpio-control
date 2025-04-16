from gpiozero import LED, Button
from time import sleep
from signal import pause

# LED 4개 정의
leds = [LED(8), LED(7), LED(16), LED(20)]

# 버튼 정의
button = Button(25, pull_up=True)

# 도미노 점등 함수
def domino():
    for led in leds:
        led.on()
        sleep(1)
        led.off()

# 버튼 눌릴 때만 실행
button.when_pressed = domino

print("Mission 2_3: 버튼을 누르면 LED가 도미노처럼 점등됩니다.")
pause()
