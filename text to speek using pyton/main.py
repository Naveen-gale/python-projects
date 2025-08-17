def speak():
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak("Hello, this is a text to speech test.")