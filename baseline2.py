import pyaudio
import audioop

THRESHOLD = 500
CHUNK = 250

pa = pyaudio.PyAudio()
stream = pa.open(
    format = pyaudio.paInt16,
                            channels = 1,
                            rate = 4000,
                            input = True,
                            input_device_index = 5,
                            frames_per_buffer = CHUNK)
while True:
    data = stream.read(CHUNK)
    amplitude = audioop.rms(data,2)
    if amplitude > THRESHOLD:
        print("voice detected, amplitude = ")
        print amplitude
        break
