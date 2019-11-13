import pyttsx3
filename = "output.wav"
engine = pyttsx3.init() #object creation
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
text = input('Enter the text : ')
engine.say(text)
engine.runAndWait()

#Saving File
engine.save_to_file("Hello", filename) #yet not implemented
