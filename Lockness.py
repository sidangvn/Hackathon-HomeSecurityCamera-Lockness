'''
This program mimics the function of artificial intelligence (A.I.) that
can be used for smart home security with a Raspberry Pi or a computer webcam.
The API twilio is used to allow the user to receive a text message from the program to the user's phone
when activity is detected between every 30 frames.
Also, the program can help you with your daily routine by reminding you to wake up, sleep, and eat,
like a companion. 

Mangohacks - Miami - 2nd to 4th Feb 2018 -
Team members: Karishma - Krishna - Hlekhulani - Si Dang

*************************************************************************************************************
* To run this Python script, installing Python, some libraries, packages and API are needed!                *
*  - Download and install Python                                                                            *
*  - Install opencv library                                                                                 *
*  - Install Twilio package                                                                                 *
*  - Install pyttsx3 library                                                                                *
*  - Install scikit image package                                                                           *
*  - Install numpy and matplotlib packages                                                                  *
*  - Any Python script editor																				*
*  - A laptop or a computer with a webcam                                                                   *
*************************************************************************************************************                                                              
'''

import pyttsx3  #Python text to speech library
from datetime import datetime  #date and time package
import cv2 #opencv library 
import numpy as np  #number library
from twilio.rest import Client  #twilio API package
from skimage.measure import compare_ssim   #scikit image package

#twilio text message notification account's information
ACCOUNT_SID = 'ACd851bfcf7ce74642a916eee1d0a20e8d'
AUTH_TOKEN = '7d5586cca53ce112cdef5c166fc6ea47'
TWILIO_PHONE = '+17273502190 '   #sender phone number
RECEIVER_PHONE = '+18138175237'  #receiver phone number

#structural similarity method from skimage package
def ssim(A, B):
	return compare_ssim(A, B, data_range = A.max() - A.min()) #luminance, contrast and structure of frames are compared

client = Client(ACCOUNT_SID, AUTH_TOKEN) 

#webcam opening
cap = cv2.VideoCapture(0)

#variables for frames declaration
curr_frame = None
prev_frame = None
first_frame = True
frame_counter = 0
first_msg = True

now = datetime.now() #Present time is fetched
engine = pyttsx3.init() #initial python text to speech

#The welcome speech
engine.say('Hello everyone! I am Lockness! Welcome to my life. I am belong to the home security camera family, but I am smart. Actually, I am not as smart as the other echo machines, but I am an awesome machine in smaller scale! Cheeeeeeeeeers!')
engine.runAndWait()

time_counter = 0  #resets daily routine after midnight

while True:   
        
	#camera starts working
    if frame_counter == 0:
        prev_frame = curr_frame
    _, curr_frame = cap.read()

	#no Camera detected
    if curr_frame is None:
        break
        
    frame_counter = frame_counter + 1 #counting the frames to 30 frames (limit)
    
	#converts the capturing video to gray scale
    curr_frame = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
    
    if first_frame: 
        prev_frame = curr_frame
        first_frame = False #now first_frame is not the first_frame anymore
	
    if frame_counter == 100: #takes 100 frames as a period of difference
        ssim_index = ssim(curr_frame, prev_frame)
        if ssim_index < 0.98 and first_msg: #0.98 is the error differences between 2 frames by using the ssim method
            #Alert message information
            client.messages.create(to = RECEIVER_PHONE, from_ = TWILIO_PHONE, body = "Intruder Alert!")
            first_msg = False
        frame_counter = 0 #reset the frame counter

	#Voice speacks out - it is a male's voice lol!!
    if time_counter == 0 and now.hour == 6 and now.minute == 0: #6:00 am
        engine.say('Good morning! Have a nice day!')
        engine.runAndWait()
    time_counter = time_counter + 1 
    
    if time_counter == 1 and now.hour == 7 and now.minute == 0: #7:00 am
        engine.say('Have you had your breakfast yet?')
        engine.runAndWait()
    time_counter = time_counter + 1
    
    if time_counter == 2 and now.hour == 12 and now.minute == 0: #12:00 pm
        engine.say('Good afternoon! Do not forget your take your lunch.')
        engine.runAndWait()
    time_counter = time_counter + 1
    
    if time_counter == 3 and now.hour == 7 and now.minute == 0: #7:00 pm
        engine.say('Good everning! Have a yummy dinner.')
        engine.runAndWait()
    time_counter = time_counter + 1
    
    if time_counter == 4 and now.hour == 9 and now.minute == 0: #9:00 pm
        engine.say('Time to sleep! Good night and sweet dreams!')
        engine.runAndWait()
    time_counter = 0 #reset the time couter back to 0 when it is the end of the day
        
	#showing the current frames of the camera  
    cv2.imshow('Security Camera', curr_frame)
    
    #pressing the Q button on the keyboard for quitting app
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#End of the program