import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import io

recognizer = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("speak something...")
        audio = recognizer.listen(source)
        try:
            english_text = recognizer.recognize_google(audio)
            print("you said: ", english_text)
            if english_text.lower() == "break":
                print("Terminating the program...")
                break  # Break out of the loop if "stop" is detected
        except sr.UnknownValueError:
            print("could not understand your audio")
            continue
        except sr.RequestError:
            print("could not request results")

    translated_text = GoogleTranslator(source='auto', target='te').translate(english_text)
    print(translated_text)

    voice = gTTS(translated_text, lang='te')
    mp3_fp = io.BytesIO()
    voice.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

