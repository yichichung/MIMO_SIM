# plot.py
import matplotlib.pyplot as plt

def plot_ber(snr_dBs, ber_list):
    plt.semilogy(snr_dBs, ber_list, marker='o')
    plt.xlabel("SNR (dB)")
    plt.ylabel("Bit Error Rate (BER)")
    plt.title("BER vs SNR for MIMO System")
    plt.grid(True, which='both')
    plt.tight_layout()
    plt.show()
