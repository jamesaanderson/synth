import numpy as np

class Oscilator:
    def __init__(self, A, f, t):
        self.A = A
        self.f = f
        self.t = t

class Sin(Oscilator):
    def __init__(self, A, f, t, phaseOff=0, lfo=None):
        super(A,f,t)
        self.phaseOff = phaseOff

    def generate():
        if lfo:
            return (A * np.sin((2 * np.pi * f * t) + phaseOff)).astype(np.int16)
        else:
            return (A + lfo) * Sin(1, f, t, phaseOff).generate()

class Cos(Oscilator):
    def __init__(self, A, f, t, phaseOff=0, lfo=None):
        super(A,f,t)
        self.phaseOff = phaseOff

    def generate():
        if lfo:
            return sin(A,f,t,phaseOff + (np.pi/2))
        else:
            return (A + lfo) * Sin(1, f, t, phaseOff).generate()

class Square(Oscilator):
    def __init__(self, A, f, t, N=64):
        super(A,f,t)
        self.N = N

    def generate():
        o = np.zeros(t.size)
        for n in range(1,N):
            o += (1/(2*n - 1)) * sin(A, f * (2*n - 1), t)
        return o

class Sawtooth(Oscilator):
    def __init__(self, A, f, t, N=64):
        super(A,f,t)
        self.N = N

    def generate():
        o = np.zeros(t.size)
        for n in range(1,N):
            o += (1/n) * sin(A, f*n, t)
        return o

class Triangle(Oscilator):
    def __init__(self, A, f, t, N=64):
        super(A,f,t)
        self.N = N

    def generate():
        o = np.zeros(t.size)
        for n in range(0,N):
            o += (((-1)**n) / ((2*n+1)**2)) * sin(A, f * (2*n + 1), t)
        return o

class Noise:
    def __init__(self, t):
        self.t = t

    def generate():
        return np.random.rand(t.size).astype(np.Int16)
