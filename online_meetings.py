#This program checks your name announcement in any online meeting .
# Just run this program near the online meeting device this program will remind you that somebody wants to hear you with alarm
#I haven't tried it in same device where online meetings were running

#importing required classes
import speech_recognition as sr
import playsound
#initiating speech recognizer
r = sr.Recognizer()
#taking input about what to hear from meeting
name = input("Name : ")

#this program will hear sound until it hears your name.
while True:
    #taking audio input from source
    with sr.Microphone() as source:
        print("Listening from meeting")
        audio = r.listen(source)
    #Error and exception handling.
    try:
        #assigning recognized text in recon variable
        recon = r.recognize_google(audio) 
        #checking if name input and recognized text are same
        if r.recognize_google(audio)  == name:
            print("Somebody called you in meeting.")
            #file location for alarm or warning sound to make you easier
            playsound.playsound("C:\\Users\\Noname\\Downloads\\now.mp3")  #You can put 15sec audio file that reminds you.
            break
            #breaking while statement if the condition meets
        else:
            print("Not yet.")
        #it prints not yet until your name is called in meeting.You can remove it.I placed it just to see if my program runs
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
