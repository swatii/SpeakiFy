def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    import speech_recognition as sr 
  
    #AUDIO_FILE = ("example.wav") 
    AUDIO_FILE = speech_file

    r = sr.Recognizer() 

    with sr.AudioFile(AUDIO_FILE) as source: 
      audio = r.record(source)   

    msg = ""
    #print msg

    try: 
      #print("The audio file contains: " + r.recognize_google(audio)) 
      msg = r.recognize_google(audio)

    except sr.UnknownValueError: 
      print("Google Speech Recognition could not understand audio") 

    except sr.RequestError as e: 
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

    print msg
    return msg



def rec():

  import pyaudio
  import wave
  from array import array


  FORMAT=pyaudio.paInt16
  CHANNELS=2
  RATE=44100
  CHUNK=1024
  RECORD_SECONDS=5
  FILE_NAME="RECORDING.wav"

  audio=pyaudio.PyAudio() #instantiate the pyaudio

  #recording prerequisites
  stream=audio.open(format=FORMAT,channels=CHANNELS, 
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

  #starting recording
  frames=[]

  for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
    data=stream.read(CHUNK)
    data_chunk=array('h',data)
    vol=max(data_chunk)
    if(vol>=1000):
        #print("something said")
        frames.append(data)
    else:
        print("nothing")
  #print("\n")


  #end of recording
  stream.stop_stream()
  stream.close()
  audio.terminate()
  #writing to file
  wavfile=wave.open(FILE_NAME,'wb')
  wavfile.setnchannels(CHANNELS)
  wavfile.setsampwidth(audio.get_sample_size(FORMAT))
  wavfile.setframerate(RATE)
  wavfile.writeframes(b''.join(frames))#append frames recorded to file
  wavfile.close()

  msg = transcribe_file(FILE_NAME)
  return msg
