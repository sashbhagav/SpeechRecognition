import speech_recognition as sr

r = sr.Recognizer()

# with sr.WaveFile("test.wav") as source:
#     audio = r.record(source)

#     try:
#         print("Transcribtion: {}".format(r.recognize(audio)))
#     except:
#         print("Could not recognize audio")


#If we want to directly hook the microphone up to this app then

with sr.Microphone() as source:
    audio = r.record(source)

    try:
        print("Transcribtion: {}".format(r.recognize(audio)))
    except:
        print("Could not recognize audio")