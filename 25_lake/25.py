import wave
from PIL import Image

canvas = Image.new('RGB', (300, 300))
for i in range(25):
    input = wave.open('lake%i.wav' % (i + 1,))
    subimg = Image.fromstring("RGB", (60, 60), input.readframes(input.getnframes()))
    canvas.paste(subimg, ((i % 5) * 60, (i / 5) * 60))

canvas.save('out.png')
