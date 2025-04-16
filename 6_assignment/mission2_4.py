from gpiozero import LED, Button
from time import sleep
from signal import pause

# 4비트 LED 설정 (LSB → MSB 순서)
led_pins = [8, 7, 16, 20]
leds = [LED(pin) for pin in led_pins]

# 버튼 설정
button = Button(25, pull_up=True)

# 카운터 함수 정의
def counter():
    for i in range(16):  # 0 ~ 15
        bits = [ (i >> bit) & 1 for bit in range(4) ]  # 4비트 분리

        for led, bit in zip(leds, bits):
            if bit:
                led.on()
            else:
                led.off()

        sleep(1)

    # 마지막에 모두 OFF
    for led in leds:
        led.off()

# 버튼 누르면 실행
button.when_pressed = counter

print("Mission 2_4: 버튼을 누르면 0~15까지 4비트 이진값이 LED로 출력됩니다.")
pause()
