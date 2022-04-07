import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

path = "./sample/sample.wav"
y, sr = librosa.load(path)

D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
plt.plot(D.flatten())
plt.show()