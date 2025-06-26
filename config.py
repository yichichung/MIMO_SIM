# config.py

Nt = 4  # Transmit antennas
Nr = 4  # Receive antennas
modulation = 'BPSK'  # or 'QPSK'
snr_dBs = list(range(0, 21, 2))  # SNR in dB: 0 to 20
num_symbols = 10000  # symbols per SNR point
receiver_type = 'ZF'  # or 'MMSE'
