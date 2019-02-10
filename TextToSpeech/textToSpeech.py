from gtts import gTTS 

import os 
 
testVar = raw_input("ENter message\n")
mytext = testVar
  
# Language in which you want to convert 
language = 'en'
  
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("welcome.mp3") 
  
# Playing the converted file 
#os.system("mpg321 welcome.mp3") 
