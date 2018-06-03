import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import pyaudio

# A - max amplitude
# f - frequency in Hz
# phaseOff - initial phase offset in radians
def sin(A, f, t, phaseOff=0):
    return (A * np.sin((2 * np.pi * f * t) + phaseOff)).astype(np.float32)

# cos is sin with a phase shift of pi/2
def cos(A, f, t):
    return sin(A,f,t,np.pi/2)

def square(A, f, t, N=64):
    o = np.zeros(t.size)
    for n in range(1,N):
        o += (1/(2*n - 1)) * sin(A, f * (2*n - 1), t)
    return o

def sawtooth(A, f, t, N=64):
    o = np.zeros(t.size)
    for n in range(1,N):
        o += (1/n) * sin(A, f*n, t)
    return o

def triangle(A, f, t, N=64):
    o = np.zeros(t.size)
    for n in range(0,N):
        o += (((-1)**n) / ((2*n+1)**2)) * sin(A, f * (2*n + 1), t)
    return o

def noise(t):
    return np.random.rand(t.size)

# ADSR (Attack-Destroy-Sustain-Release) Envelope
# outputs a(t), amplitude as a function of time
def envelope(t, start, final, rate):
   dur = t[t.size-1]
   return (final - start) * np.power(t/dur,rate) + start

def write(audio, sps, out):
    wavfile.write(out, sps, audio) 

def play(audio, sps):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sps,
                    output=True)
    stream.write(audio.tostring())

    stream.stop_stream()
    stream.close()

    p.terminate()

SPS = 44100 # 44.1 kHz or 44100 samples per second (48 kHz other alternative)
DURATION_S = 60

samples = np.arange(DURATION_S * SPS) / SPS
amp = envelope(samples,0,0.3,2)
wave = sin(amp,261.63,samples)

write(wave,SPS,'test.wav')
# write(triangle(0.3,261.63,samples),SPS,'test.wav')
# play(wave,SPS)
