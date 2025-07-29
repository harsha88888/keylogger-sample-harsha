import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename='mic.wav', duration=10, fs=44100):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    write(filename, fs, audio)
