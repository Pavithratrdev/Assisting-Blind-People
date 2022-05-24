import speech_recognition as sr
def sampledata():
    data = sr.Recognizer()
    with sr.Microphone() as source:
        #print("speak")
        audio = data.record(source, duration=10)
       # print("Done")
        text = data.recognize_google(audio, language="en-IN")
        return str(text)
        #print(text)

#print(r.recognize_google(audio)
#sampledata()