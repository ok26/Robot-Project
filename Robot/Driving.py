from Robot import ENA, ENB, GPIO_pins  #ENA: LEFT,  ENB: RIGHT
import RPi.GPIO as GPIO

class Wheel:
    def __init__(self, rwheel, lwheel):
        self.rwheel_f = int(rwheel[0])
        self.rwheel_b = int(rwheel[1])
        self.lwheel_f = int(lwheel[0])
        self.lwheel_b = int(lwheel[1])
        
        self.forward = False
        self.backward = False
        self.left = False
        self.right = False
        
        self.ENA_dc = 50
        self.ENB_dc = 50

        
    def slow_lturn(self):
        if self.ENB_dc != 30:
            ENB.ChangeDutyCycle(30)
            self.ENB_dc = 30
        if not GPIO.input(self.rwheel_f):
            GPIO.output(self.rwheel_f, True)
    
    def slow_rturn(self):
        if self.ENA_dc != 30:
            ENA.ChangeDutyCycle(30)
            self.ENA_dc = 30
        if not GPIO.input(self.lwheel_f):
            GPIO.output(self.lwheel_f, True)
            
    def slow_forward(self):
        if self.ENA_dc != 30:
            ENA.ChangeDutyCycle(30)
            self.ENA_dc = 30
        if self.ENB_dc != 30:
            ENB.ChangeDutyCycle(30)
            self.ENB_dc = 30
        if not GPIO.input(self.lwheel_f):
            GPIO.output(self.lwheel_f, True)
        if not GPIO.input(self.rwheel_f):
            GPIO.output(self.rwheel_f, True)
    
    def slow_forward_rturn(self):
        if self.ENB_dc != 20:
            ENB.ChangeDutyCycle(20)
            self.ENB_dc = 20
        if self.ENA_dc != 40:
            ENA.ChangeDutyCycle(40)
            self.ENA_dc = 40
        if not GPIO.input(self.lwheel_f):
            GPIO.output(self.lwheel_f, True)
        if not GPIO.input(self.rwheel_f):
            GPIO.output(self.rwheel_f, True)
        
    def slow_forward_lturn(self):
        if self.ENB_dc != 40:
            ENB.ChangeDutyCycle(40)
            self.ENB_dc = 40
        if self.ENA_dc != 20:
            ENA.ChangeDutyCycle(20)
            self.ENA_dc = 20
        if not GPIO.input(self.lwheel_f):
            GPIO.output(self.lwheel_f, True)
        if not GPIO.input(self.lwheel_f):
            GPIO.output(self.rwheel_f, True)

    def check_stop(self):
        if not self.forward and not (self.left or self.right):
            if GPIO.input(self.rwheel_f):
                GPIO.output(self.rwheel_f, False)
            if GPIO.input(self.lwheel_f):
                GPIO.output(self.lwheel_f, False)
            
        if not self.left and not self.forward:
            if GPIO.input(self.rwheel_f):
                GPIO.output(self.rwheel_f, False)
            
        if not self.right and not self.forward:
            if GPIO.input(self.lwheel_f):
                GPIO.output(self.lwheel_f, False)


        