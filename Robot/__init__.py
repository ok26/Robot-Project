import cv2, serial, sys, tty
import RPi.GPIO as GPIO

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,352)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser.reset_input_buffer()
tty.setcbreak(sys.stdin)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO_pins = [29,31,32,33,35,36]   #In order:  LwheelF, LwheelB, RwheelB, RwheelF, ENA(LEFT MOTOR), ENB(RIGHT MOTOR)

for pin in GPIO_pins:
    GPIO.setup(pin,GPIO.OUT)

ENA = GPIO.PWM(35, 60)
ENB = GPIO.PWM(36, 60)

