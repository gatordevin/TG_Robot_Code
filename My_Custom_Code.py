# Mecanum code for the google coral
# Author: Danny Dasilva
# License: Public Domain 



from app.Robot import Controller, Py_Hat
from app.Autonomous import Autonomous
import math
from time import sleep
import os


def my_custom_autonomous():
    controller = Controller()
    deadzone = controller.deadzone()
    hat = Py_Hat(address=96)
    while True:
        if not controller.has_controller():
            # handle disconnect
            #loop through all the pins and set them to 0
            hat.motor(2, deadzone)
       
        else:
            #print("Controlerl connected")
            controller.event_get()
            forward = controller.set_axis("leftstick")
            strafe = controller.set_axis("leftstickx")
            turn = controller.set_axis("rightstickx")
            rightVert = controller.set_axis("rightstick")
            A = controller.set_button('A')
            Y = controller.set_button('Y')
            x, y = controller.gamepad.get_hat(0)

            hat.motor(4,-forward-turn-strafe)
            hat.motor(5,-forward-turn+strafe)
            hat.motor(6,forward-turn+strafe)
            hat.motor(7,forward-turn-strafe)
            hat.motor(0,x)
            if(A):
                hat.motor(1,-1)
            elif(Y):
                hat.motor(1,1)
            else:
                hat.motor(1,0)
            hat.motor(2,-y)
            hat.motor(3,-y)

def my_custom_teleop():

    #controller class
    controller = Controller()

    # initialize Pi Hat
    hat = Py_Hat(address=96)

    # configure deadzone
    deadzone = controller.deadzone()

    # Configure min and max servo angle as well  as init
    servo_min = 0  
    servo_max = 360
    servo = 0


    while True:
        if not controller.has_controller():
            # handle disconnect
            #loop through all the pins and set them to 0
            for pin in range(4):
                hat.motor(pin, deadzone)
       
        else:
            #print("Controlerl connected")
            controller.event_get()
            
            B = controller.set_button('B')
            X = controller.set_button('X')
            A = controller.set_button('A')
            Y = controller.set_button('Y')
            LB = controller.set_button('LB')
            RB = controller.set_button('RB')
            LT = controller.set_axis('LT')
            RT = controller.set_axis('RT')
            Home = controller.set_button('Home')
            Start = controller.set_button('Start')
            Back = controller.set_button('Back')



            
            #  Arm A motor
            if LB == 1:
                hat.motor(4, 1)
                print("Motor Arm 1 forward")
            elif RB == 1:
                hat.motor(4, -1)
                print("Motor Arm 1 back")
            else:
                hat.motor(4, deadzone)


            #  Arm B motor
            if LT > .75:
                hat.motor(5, 1)
                print("Motor Arm 2 forward")
            elif RT > .75:
                hat.motor(5, -1)
                print("Motor Arm 2 back")
            else:
                hat.motor(5, deadzone)



            # Servo 1
            if LT > .75:
                servo = min(servo + .2, servo_max)
                hat.servo(6, servo)
                print("servo 1 active")
            elif RT > .75:
                servo = max(servo - .2, servo_min)
                hat.servo(6, servo)
                print("servo 1 active")
            

            # Servo 2
            if X == 1:
                servo = min(servo + .2, servo_max)
                hat.servo(7, servo)
                print("servo 2 active")

            
            elif Y == 1:
                servo = max(servo - .2, servo_min)
                hat.servo(7, servo)
                print("servo 2 active")



            forward = controller.set_axis("leftstick")
            turn = controller.set_axis("rightstickx")
            strafe = controller.set_axis("leftstickx")
            print(strafe)
            hat.motor(0, -forward + strafe - turn)
            hat.motor(1, forward - strafe - turn)
            hat.motor(2, forward + strafe - turn)
            hat.motor(3, -forward - strafe - turn)


            # motor_1  back right
            # motor_2  front left
            # motor_3  back left
            # motor_4  front right

            # Reset Deadzone
            if Start == Y == Home == 1:
                deadzone = controller.control_loop(.01, hat)
            
            # sleep for smooth loops
            sleep(.02)













