import noisereduce as nr
import soundfile as sf
import numpy as np


def noiseReduce(file_name):
    data, rate = sf.read('./heartbeat_data/'+file_name + '.wav')
    data = np.array(data)
    noise_reduced = nr.reduce_noise(audio_clip=data, noise_clip=data, prop_decrease=1.0, verbose=True)
    sf.write('./heartbeat_noseReduce_data/'+ file_name + '_nr_v.wav', noise_reduced, rate)
