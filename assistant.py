import pyttsx3
import datetime
import speech_recognition as sr
import random
import time
file = "game.txt"
game = open(file,'r')
games = (game.read()).split("\n")

engine = pyttsx3.init('sapi5')#Initializing the voice given by microsoft
voices = engine.getProperty('voices')#getting voice

engine.setProperty('voice',voices[0].id)#setting the male voice of david for use
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #it takes audio from microphone and returns a string
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening.............")
        #r.pause_threshold = 1
        
        audio = r.listen(source)

        try:
            print("Recognizing..............")
            query = r.recognize_google(audio, language="en-in")
            print(f"you said.......{query}\n")
        except Exception as e:
            print(f"say that again please........{e}")
            return "None"
        return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=5 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<16):
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello Sir I am Friday How can i help you!")

def gameEngine(l):
    t = "yes"
    score = 0
    k=0
    while((t!="no") and k<len(l)):  
        l2 = []        
        b = str(l[k])
        k=k+1
        c = list(b)
        d = random.randint(3,4)
        for i in range(d):
            h = random.randint(0,len(c)-1)
            if(h in l2):
                i = i-1
            else:
                l2.append(h)
                i = i+1
        speak("The word is......")
        print(f"Word number {k} : ",end=" ")
        for j in range(len(c)):
            if(j in l2):
                print("__",end = " ")
            else:
                print(c[j],end = " ")
        print("Guess the correct word : ")
        start = time.time() 
        f = takeCommand()
        end = time.time()
        s = end-start
        if(s<=20):
        
            if(f.lower()==b):
                score = score +10
                print(f":) Correct Guess! Score : {score}")
                speak("Wohoo! Correct Guess......")
                speak(f"Your score is {score}")
            else:
                score = score -5     
                print(f":( Wrong Guess! Score : {score}")
                speak(f"Ahhhhh! Wrong Guess ")
                speak(f"Your score is {score}")
        else:
            print("Sorry You missed it the time is over.........")
            speak("Sorry you are out of time  try another question")
            score = score-5
        speak("Would you like to continue")
        t = takeCommand()
    print('-'*15,"Game Over",'-'*15,'\n')
    return score



if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand()
        if (("game" in query) or ('play' in query)):
            speak("Welcome to the game of word master")
            print('*'*15,"||Welcome to Word Master ||",'*'*15,'\n')  
            run = gameEngine(games)
            print(f"Your Final score is : {run}\n")
            print("*"*15,"Thanks For Playing","*"*15)
            speak(f"Your Final score is : {run}\n")
            speak("Thanks For Playing")



    