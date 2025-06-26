# modulation.py
import numpy as np

def modulate(bits, scheme='BPSK'):
    if scheme == 'BPSK':
        return 2 * bits - 1  # 0 → -1, 1 → +1
    else:
        raise NotImplementedError("Only BPSK implemented for now.")

def demodulate(symbols, scheme='BPSK'):
    if scheme == 'BPSK':
        return (np.real(symbols) > 0).astype(int)
    else:
        raise NotImplementedError("Only BPSK implemented for now.")
