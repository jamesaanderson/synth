import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import pyaudio

import oscilators

# ADSR (Attack-Destroy-Sustain-Release) Envelope
# outputs a(t), amplitude as a function of time
def envelope(t, start, final, rate):
   dur = t[t.size-1]
   return (final - start) * np.power(t/dur,rate) + start

# Frequency Modulation (FM) Synthesis
def fm(amp_mod, amp_carr, f_mod, f_carr, t, phase_mod=0, phase_carr=0):
    return amp_carr * np.sin((2 * np.pi * f_carr + sin(amp_mod, f_mod, t, phase_mod)) * t + phase_carr)

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

wave = oscilators.Sin(0.3,261.63,samples,lfo=oscilators.Sin(0.3,15,samples).generate())

# osc = lfo(0.3,0.3,261.63,samples,20)

# write(fm(0.3,0.3,amp,146.832,samples),SPS,'test.wav')
# write(triangle(0.3,261.63,samples),SPS,'test.wav')
write(wave.generate(),SPS,'test.wav')
# play(wave,SPS)

# plt.plot(samples,fm(0.3,0.3,5,100,samples))
# plt.show()
