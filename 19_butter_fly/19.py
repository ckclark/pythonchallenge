from base64 import decode
import wave
decode(open('indian.wav.base64'), open('indian.wav', 'w'))

input = wave.open('indian.wav')
nframe = input.getnframes()
params = input.getparams()

output = wave.open('indian_out.wav', 'w')
output.setparams(params)

for i in range(nframe):
    frame = input.readframes(1)
    output.writeframes(frame[::-1])

output.close()
