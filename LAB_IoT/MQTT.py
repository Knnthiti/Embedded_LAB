import RPi.GPIO as GPIO
import time

# Pin setup
TRIG = 23
ECHO = 24

LED_RED = 17
LED_YELLOW = 27
LED_GREEN = 22

# GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

def measure_distance():
    # ส่ง pulse trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # รอ echo start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # รอ echo end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # คำนวณเวลา และระยะทาง (cm)
    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2
    return distance

def led_control(distance):
    # ปิดทุกดวงก่อน
    GPIO.output(LED_RED, False)
    GPIO.output(LED_YELLOW, False)
    GPIO.output(LED_GREEN, False)

    # ระยะทางเป็นช่วง
    if distance < 10:        # ใกล้มาก
        GPIO.output(LED_RED, True)
    elif distance < 30:      # ระยะกลาง
        GPIO.output(LED_YELLOW, True)
    else:                    # ไกล/ปลอดภัย
        GPIO.output(LED_GREEN, True)

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")
        led_control(dist)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup()