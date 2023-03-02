import speech_recognition as sr #mic
import pyttsx3 #text-to speech (tts)
import webbrowser as wb #bukak web
import keyboard as k

#setup tts
x = pyttsx3.Engine('sapi5')
def speak(audio):
    x.say(audio)
    x.runAndWait()


#setup mic
r = sr.Recognizer()

while True:
    if k.is_pressed('x'):
        with sr.Microphone() as mic:
            print('listening')
            audio = r.listen(mic, phrase_time_limit=4)
    
            try: 
 
                    query = r.recognize_google(audio)
                    query = query.lower()

                    print(query)
            
                
                    if 'youtube' in query:
                        wb.open_new('https://www.youtube.com')
                        speak('opening youtube like you want sir')
                    elif 'instagram' in query:
                        wb.open_new('https://www.instagram.com')
                    elif 'facebook' in query:
                        wb.open_new('https://www.facebook.com')
                    elif 'tiktok' in query:
                        wb.open_new('https://www.tiktok.com')
            
            except sr.UnknownValueError():
                    print('failed to hear')

