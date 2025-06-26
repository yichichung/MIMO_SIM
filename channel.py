# channel.py
import numpy as np

def generate_channel(Nr, Nt):
    return (np.random.randn(Nr, Nt) + 1j * np.random.randn(Nr, Nt)) / np.sqrt(2)

def add_noise(y, snr_dB):
    snr_linear = 10 ** (snr_dB / 10)
    sigma2 = 1 / snr_linear
    noise = np.sqrt(sigma2 / 2) * (np.random.randn(*y.shape) + 1j * np.random.randn(*y.shape))
    return y + noise
