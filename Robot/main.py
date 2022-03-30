from Robot.Camera import find_centroid, move_camera
from Robot import ENA, ENB, ser
from Robot.Driving import Wheel

def check_Y(Y, Wheels):
    if Y >= 50 and Y <= 110:
        return True
                        
    elif Y > 110:
        Wheels.forward = False
        Wheels.backward = False
        Wheels.left = False
        Wheels.right = False
        Wheels.check_stop()
        ser.write(str(4).encode("utf-8"))
        return False
    elif Y < 50:
        return False
    

def run():
    counter = 0
    ENA.start(50)
    ENB.start(50)
    Wheels = Wheel((33,32),(29,31))
    
    while True:
        cX, cY, shape = find_centroid()
        if shape == 0:
            break
        else:
            if ser.in_waiting > 0:
                X = ser.read()
                Y = ser.read()
                X = int.from_bytes(X, byteorder="big")
                Y = int.from_bytes(Y, byteorder="big")
                
                if X >= 110:
                    Wheels.left = True
                    Wheels.right = False
                    Wheels.forward = check_Y(Y, Wheels)
                    
                        
                elif X <= 70:
                    Wheels.right = True
                    Wheels.left = False
                    Wheels.forward = check_Y(Y, Wheels)
                    
                else:
                    Wheels.left = False
                    Wheels.right = False
                    Wheels.forward = check_Y(Y, Wheels)
                    
                Wheels.check_stop()
                    
                if Wheels.forward and Wheels.right:
                    Wheels.slow_forward_rturn()
                elif Wheels.forward and Wheels.left:
                    Wheels.slow_forward_lturn()
                elif Wheels.forward:
                    Wheels.slow_forward()
                elif Wheels.right:
                    Wheels.slow_rturn()
                elif Wheels.left:
                    Wheels.slow_lturn()
                        
                
            if counter == 2:
                counter = 0
                move_camera(cX, cY, shape)
            counter += 1
            
    print(Wheels.forward, Wheels.left, Wheels.right)
    Wheels.forward = False
    Wheels.backward = False
    Wheels.left = False
    Wheels.right = False
    Wheels.check_stop()
    ENA.stop()
    ENB.stop()