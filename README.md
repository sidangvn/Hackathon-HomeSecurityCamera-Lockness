# Lockness

Inspiration
Our team shares a common fact, that is dreaming. Although everyone has various dreams, we dream to be a programmer who can develop not only
themselves but mainly the community as well. Lockness is our one of the major step to reach our dream. We made Lockness not just with love,
but also with smartness. Since this is our first hackathon and we have a long way to go, we are already excited and curious about the next
level that we are aiming to take our Lockness to. We got our first curious on this topic base when we started participating in 
IEEE-Robotics division's meetings. Artificial Intelligence is one of our major interest in this field and we want to benefit the community
using it. As we kept thinking, we thought to make a security camera that is not just a security camera, but also a companion. We thought 
of connecting these ideas using a raspberry pi or a laptop webcam which could detect intruders using 100 frames to compare and alert the 
user via a text message. In addition, we wanted Lockness to be able to interact with the user based on daily activities by recognizing the 
time and using voice notifications. This is basically where our inspiration came from.

What it does
To put it in a little detail, when the user turns on the Lockness, it starts to detect to see if there is any activity and if so, it 
will send a text message to the user's phone saying that there is some suspicious activity. Also, when the Lockness is turned on by the 
user, it gives a welcome speech. And, since it knows the time, it gives daily notifications at morning, noon, and at various times in 
the form of speech.

How we built it
This program mimics the function of artificial intelligence (A.I.) that can be used for smart home security with a Raspberry Pi or a 
computer webcam. The API Twilio is used to allow the user to receive a text message from the program to the user's phone when activity 
is detected between every 100 frames. Also, the program can help you with your daily routine by reminding you to wake up, sleep, and eat,
like a companion. To run this Python script, install Python, OpenCV library, Twilio package, pyttsx3 library, scikit image package, 
numpy and matplotlib packages, any python script editor, and a laptop or a computer with a webcam. Although our first inspiration was 
to do this with Raspberry Pi, we managed to get only the old version of Raspberry Pi where there is no camera and cannot be used to do
this project. So, we used a laptop's webcam to do it. To set up the text message system, we created an account on Twilio. Using machine
learning, we managed to let it decide whether there is an activity or not by comparing 100 frames. Since it has the date and time 
package, it will use its voice ability to give daily notifications like to eat, sleep, and more.

Challenges we ran into
As we are sophomores, we haven't learned a lot about the programming field and have expertise in it. Also, Artificial Intelligence is 
a newly developing field where there are so many possibilities available for the outcome. This was a great challenge for us to overcome.
It took us a while but being a part of IEEE-Robotics division and by learning a lot by using YouTube and other various online resources,
we were able to accomplish this.

Accomplishments that we're proud of
Like we have already mentioned, it took us a while to complete Lockness. As sophomores, we are really proud to welcome Lochness to one
of our challenging creation as it uses Artificial Intelligence and some complications which are usually not familiar among Sophomores.


What we learned
We learned a lot about team building as we went through this process of making Lockness. We realized that each one of us had a different
idea about it which required a lot of teamwork to complete it successfully without getting lost in thoughts.

What's next for Lockness
After this hackathon, we are going to team up again and learn further about Artificial Intelligence and additionally Machine Learning as 
well and upgrade our Lockness. We are planning to make a voice assistant and create facial recognition using Raspberry Pi 4.

Built With
python
twilio
scikit-image
opencv
pyttsx3
numpy
Try it out
