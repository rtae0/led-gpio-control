from gpiozero import LED, Button
from signal import pause

# 핀 설정
led = LED(8)
button = Button(25, pull_up=True)  # 풀업 회로이므로 pull_up=True

# 동작 설정
button.when_pressed = led.on       # 버튼 누르면 켜기
button.when_released = led.off     # 버튼 떼면 끄기

print("Mission 1: 버튼 눌림 여부에 따라 LED를 On/Off 합니다.")
pause()  # 프로그램 계속 실행 상태 유지
