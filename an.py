import sounddevice as sd
from scipy.io.wavfile import write

fs = 20000 # Sample rate
t = 1.0
seconds = 12*t  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('rec.wav', fs, myrecording)  # Save as WAV file 

import numpy as np
from scipy.fft import *
from scipy.io import wavfile

def freq(file, start_time, end_time):

    # Open the file and convert to mono
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass

    # Return a slice of the data from start_time to end_time
    dataToRead = data[int(start_time * sr ) : int(end_time * sr ) + 1]

    # Fourier Transform
    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)

    # Uncomment these to see the frequency spectrum as a plot
    # plt.plot(xf, np.abs(yf))
    # plt.show()

    # Get the most dominant frequency and return it
    idx = np.argmax(np.abs(yf))
    freq = xf[idx]
    return freq

o = "0"
i = 0.0
while(i<12*t):
    if(round(freq('rec.wav',i,i+0.3*t)/50) ==16):
        break
    i += 0.3*t
i+=0.3*t
i += 1
n = round(freq('rec.wav',i,i+0.3*t)/25) - 13
x = (n%3 != 0)
inv = n//3 + x
while(inv):
    inv -= 1
    i += 1
    if(inv != 0):
        b = round(freq('rec.wav',i,i+0.3*t)/50) - 8
        o += bin(b).replace("0b","").zfill(3)
    else:
        b = round(freq('rec.wav',i,i+0.3*t)/50) - 8
        o += bin(b).replace("0b","").zfill(n%3)
        break
inv = 2
rds = ""
while(inv):
    inv -= 1
    i += 1
    b = round(freq('rec.wav',i,i+0.3*t)/50) - 8
    rds += bin(b).replace("0b","").zfill(3)

l1=list(o)
l = [eval(i) for i in l1]
from functools import reduce
import operator as op
p=reduce(op.xor, [i for i,bit in enumerate(l) if bit])
redundant_string=bin(p)[2:]
for i in range(6-len(redundant_string)):
    redundant_string="0"+redundant_string
p = int(rds,2)
q = int(redundant_string,2)
y = p^q

print("Transmitted string: ",o[1:])
o = o[:y]+str(1-eval(o[y]))+o[y+1:]
o = o[1:]
if(y!=0):
    print("Bit error at: ",y)
print("Intended string: ",o)

