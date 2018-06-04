import numpy as np

class Oscilator:
    def __init__(self, A, f, t):
        self.A = A
        self.f = f
        self.t = t

class Sin(Oscilator):
    def __init__(self, A, f, t, phaseOff=0, lfo=None):
        super().__init__(A,f,t)
        self.phaseOff = phaseOff
        self.lfo = lfo

    def generate(self):
        if self.lfo is None:
            return self.A * np.sin((2 * np.pi * self.f * self.t) + self.phaseOff)
        else:
            return (self.A + self.lfo) * Sin(1, self.f, self.t, self.phaseOff).generate()

class Cos(Oscilator):
    def __init__(self, A, f, t, phaseOff=0, lfo=None):
        super().__init__(A,f,t)
        self.phaseOff = phaseOff
        self.lfo = lfo

    def generate(self):
        if self.lfo is None:
            return Sin(self.A,self.f,self.t,self.phaseOff + (np.pi/2)).generate()
        else:
            return (self.A + self.lfo) * Cos(1, self.f, self.t, self.phaseOff).generate()

class Square(Oscilator):
    def __init__(self, A, f, t, N=64):
        super().__init__(A,f,t)
        self.N = N

    def generate(self):
        o = np.zeros(self.t.size)
        for n in range(1,self.N):
            o += (1/(2*n - 1)) * sin(self.A, self.f * (2*n - 1), self.t)
        return o

class Sawtooth(Oscilator):
    def __init__(self, A, f, t, N=64):
        super().__init__(A,f,t)
        self.N = N

    def generate(self):
        o = np.zeros(t.size)
        for n in range(1,self.N):
            o += (1/n) * sin(self.A, n, self.t)
        return o

class Triangle(Oscilator):
    def __init__(self, A, f, t, N=64):
        super().__init__(A,f,t)
        self.N = N

    def generate(self):
        o = np.zeros(t.size)
        for n in range(0,N):
            o += (((-1)**n) / ((2*n+1)**2)) * sin(self.A, self.f * (2*n + 1), self.t)
        return o

class Noise:
    def __init__(self, t):
        self.t = t

    def generate(self):
        return np.random.rand(self.t.size)
