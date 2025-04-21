# Raspberry Pi GPIO 제어 미션 (Python 버전)

유튜브 : https://youtu.be/1c1uZc7WrLY 

이 프로젝트는 Raspberry Pi의 GPIO 핀과 Python을 이용하여 다양한 형태로 LED를 제어하는 실습입니다.  
버튼 입력을 받아 실시간 반응하거나 LED 상태를 토글하며, 기본적인 디지털 회로 동작 원리를 익힐 수 있습니다.

---

## 📁 파일 구성

| 파일명 | 미션 내용 |
|-----------|------------------------------|
| `mission2_1.py` | 버튼이 눌린 동안만 LED 켜기 |
| `mission2_2.py` | 버튼이 눌릴 때마다 LED 토글 |
| `mission2_3.py` | 버튼이 눌리면 domino4 1회 실행 |
| `mission2_4.py` | 버튼이 눌릴 때마다 4-bit 카운터 값 증가시키기 (LED 4개로 이진 출력) |

---

## 🔧 사용 핀 구성

- **버튼 입력 핀**: GPIO 25
- **LED 출력 핀들**:
  - GPIO 8 (LSB)
  - GPIO 7
  - GPIO 16
  - GPIO 20 (MSB)

모든 코드는 `BCM 핀 넘버링` 기준입니다.

---

## ▶️ 실행 방법

```bash
python3 mission2_1.py
```
모든 미션 파일은 위처럼 Python으로 실행할 수 있으며, Ctrl + C로 종료할 수 있습니다.

⸻

## 🛠️ 미션별 상세 설명

mission2_1.py - 버튼이 눌린 동안만 LED 켜기
	•	버튼이 눌려 있는 동안 LED가 켜지고, 손을 떼면 꺼지는 구조입니다.
	•	실시간 입력 처리 연습에 적합합니다.
```python
while True:
    led.value = button.is_pressed
```


⸻

mission2_2.py - 버튼 누를 때마다 LED 토글
	•	버튼을 누를 때마다 LED의 상태가 반전됩니다.
	•	이전 상태 기억, 토글 구현을 이해하는 데 적합합니다.
```python
while True:
    button.wait_for_press()
    led.toggle()
```


⸻

mission2_3.py - 버튼 누르면 domino4 1회 실행
	•	버튼을 누르면 LED 4개가 순차적으로 켜졌다 꺼지는 애니메이션처럼 작동합니다.
	•	도미노처럼 흐르는 효과 구현
```python
for led in leds:
    led.on()
    sleep(0.1)
# ...
```



⸻

mission2_4.py - 버튼 누를 때마다 4-bit 이진 카운터 출력
	•	버튼을 누를 때마다 0부터 15까지 1씩 증가하며, 이를 이진수로 표현해 LED 4개에 출력합니다.
	•	기본적인 이진수 연산과 카운터 로직을 학습하기에 적합합니다.
```python
bits = [(counter >> i) & 1 for i in range(4)]
```


⸻

💡 실습 목적
	•	GPIO 출력/입력 개념 이해
	•	버튼 인터럽트 처리
	•	LED 시퀀싱 및 비트 연산
	•	실시간 반응형 프로그램 설계

⸻

📦 설치 필요 패키지

pip install gpiozero

⸻

📸 회로 구성
	•	LED에는 저항(330Ω~1kΩ)을 직렬로 연결
	•	버튼에는 풀다운 저항(10kΩ) 연결
	•	브레드보드와 점퍼선을 활용해 구성

⸻
