from scipy.io import wavfile

path  = "./sample/sample.wav"
fs, data = wavfile.read(path)

print(fs, data.shape)
print(data)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,3))
plt.plot(data, lw=1)
plt.xlabel('sample')
plt.ylabel('data')
plt.xlim(0, len(data))
plt.show()