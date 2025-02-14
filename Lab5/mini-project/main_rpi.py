from helper_functions import camera, computer_vision,sensehat
### TO-DO: You may require more imports
from time import sleep
import base64


def main():
    camera_i = camera.get_camera() #DO NOT MODIFY, function call must work as is 
    sense = sensehat.get_sensehat() #DO NOT MODIFY, function call must work as is 
    
    get_background = input("Enter '1' if a background image is saved in data/images/background.png \nEnter '2' if you need a background image\n")
    
    if get_background == '1':
        take_background_image = False #TO-DO: Should be a user input
    else:
        take_background_image = True

    if take_background_image:
        ### TO-DO: Countdown image capture of background
        print("Get out of the scene")
        print("Background image will be taken in 10 seconds...")
        for i in range (9,0,-1):
            print("%d\n" %i)
            sleep(1)
        preview = False
        countdown=0
        camera.capture_image(camera_i,"data/images/background.png", countdown_time=countdown, preview=preview) #DO NOT MODIFY, function call must work as is 
        base64.encode("data/images/background.png")
    userInput = input("Would you like to arm the system? Y/N: ")
    if userInput == 'Y':
        arm_system = True #TO-DO: Should be a user input
    else:
        arm_system = False

    if arm_system:
        interval = input("Enter the interval between test images in seconds: ")
        interval = int(interval)
        t1 = input("Enter the threshold t1: ")
        t1 = int(t1)
       
       ### TO-DO: Countdown to monitoring
        print("Monitoring will be taken in 10 seconds...")
        for i in range (9,0,-1):
            print("%d\n" %i)
            sleep(1)
        count = 0
        while True: #DO NOT MODIFY, function call must work as is 
            camera.capture_image(camera_i,"data/images/image%s.jpg" % count, countdown_time = interval) #DO NOT MODIFY, function call must work as is 
            person_detected = computer_vision.person_detected("data/images/background.png","data/images/image%s.jpg" % count, t1)  #DO NOT MODIFY, function call must work as is 
            if person_detected: #DO NOT MODIFY, function call must work as is 
                print("Person Detected") #DO NOT MODIFY, function call must work as is 
                sensehat.alarm(sense,interval)  #DO NOT MODIFY, function call must work as is 
            else:
                print("No Person Detected") #DO NOT MODIFY, function call must work as is 
            count += 1


if __name__ == "__main__":
    main()
