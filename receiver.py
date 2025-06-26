# receiver.py
import numpy as np

def zf_detector(H, y):
    W = np.linalg.pinv(H)
    return W @ y

def mmse_detector(H, y, snr_linear):
    Nt = H.shape[1]
    sigma2 = 1 / snr_linear
    W = np.linalg.inv(H.conj().T @ H + sigma2 * np.eye(Nt)) @ H.conj().T
    return W @ y
