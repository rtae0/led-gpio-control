# GPIO LED 순차 점등 제어 스크립트

이 프로젝트는 Raspberry Pi의 GPIO 핀을 이용해 4개의 LED를 순차적으로 점등(깜빡이게)하는 Bash 스크립트입니다.  
간단한 쉘 스크립트를 통해 GPIO 핀을 제어하고, LED 동작을 직접 눈으로 확인할 수 있습니다.

---

## 🧾 사용한 핀

| 핀 번호 | 용도         |
|--------|--------------|
| GPIO 18 | 첫 번째 LED |
| GPIO 19 | 두 번째 LED |
| GPIO 20 | 세 번째 LED |
| GPIO 21 | 네 번째 LED |

---

## 🛠️ 실행 방법

1. 스크립트에 실행 권한을 부여합니다.

```bash
chmod +x domino
```
2.	스크립트를 실행합니다.
```bash
./domino
```
LED가 순차적으로 1초 간격으로 켜졌다가 꺼지는 동작을 반복합니다.

실행 중지를 원하면 터미널에서 Ctrl + C 를 누르세요.
---
## 💡 코드 설명
```bash
# GPIO 18~21번 핀을 출력 모드로 설정
pinctrl set 18 op
pinctrl set 19 op
pinctrl set 20 op
pinctrl set 21 op
```
• 4개의 핀을 모두 출력 모드(output) 로 설정하여 LED를 제어할 수 있도록 준비합니다.
```bash
while true; do
    pinctrl set 18 dh
    sleep 1
    pinctrl set 18 dl

    pinctrl set 19 dh
    sleep 1
    pinctrl set 19 dl

    pinctrl set 20 dh
    sleep 1
    pinctrl set 20 dl

    pinctrl set 21 dh
    sleep 1
    pinctrl set 21 dl
done
```
	•	무한 루프를 통해 각 GPIO 핀을 1초 간격으로 high(켜기) → low(끄기) 로 설정합니다.
	•	이로 인해 LED가 차례대로 깜빡이며 반복 동작하게 됩니다.